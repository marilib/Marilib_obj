#!/usr/bin/env python3
"""
Created on Thu Jan 20 20:20:20 2020

@author: DRUOT Thierry
"""

import numpy as np
from context import unit

data_dict = {
    "n_panel": {"unit":"int", "mag":1e4, "txt":"Number of individual panels"},
    "panel_area": {"unit":"m2", "mag":1e1, "txt":"Panel area"},
    "panel_mass": {"unit":"kg", "mag":1e1, "txt":"Panel mass"},
    "ground_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Required ground area over panel area"},
    "grey_energy_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Fraction of produced energy needed to build, maintain and recycle the production device"},
    "life_time": {"unit":"year", "mag":1e0, "txt":"Power plant reference life time"},
    "gross_power_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Ratio of produced power over solar input power"},
    "ref_yearly_sun_power": {"unit":"W/m2", "mag":1e0, "txt":"Yearly mean sun power at power plant location"},
    "load_factor": {"unit":"no_dim", "mag":1e0, "txt":"Ratio of yearly mean power over peak power"},
    "total_panel_area": {"unit":"m2", "mag":1e6, "txt":"Total area of the solar panels"},
    "foot_print": {"unit":"m2", "mag":1e6, "txt":"Ground footprint area of the power plant"},
    "net_power_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Power efficiency including grey energy spread over life time"},
    "nominal_peak_power": {"unit":"MW", "mag":1e2, "txt":"Output power with ref_yearly_sun_power is input"},
    "nominal_gross_power": {"unit":"MW", "mag":1e2, "txt":"Mean yearly output power"},
    "nominal_net_power": {"unit":"MW", "mag":1e2, "txt":"Mean yearly output power including grey energy spread over life time"},
    "gross_yearly_enrg": {"unit":"GWh", "mag":1e2, "txt":"Mean yearly energy production"},
    "net_yearly_enrg": {"unit":"GWh", "mag":1e2, "txt":"Mean yearly energy production including grey energy spread over life time"},
    "total_grey_enrg": {"unit":"GWh", "mag":1e3, "txt":"Total required grey energy over life time"},
}

one_hour = 3600.
one_day = one_hour * 24.
one_year = one_day * 365.


class StPowerPlant(object):

    def __init__(self, n_mirror, ref_sun_pw, reg_factor):
        self.type = "Cylindroparabolic mirror"
        self.regulation_factor = reg_factor
        self.n_mirror = n_mirror
        self.mirror_area = 68.
        self.ground_ratio = 4.0
        self.life_time = 25.

        self.gross_power_efficiency = 0.39
        self.storage_efficiency = 0.99
        self.grey_energy_ratio = 0.11

        self.ref_yearly_sun_power = ref_sun_pw
        self.load_factor = 0.38

        self.total_mirror_area = None
        self.total_foot_print = None

        self.nominal_peak_power = None
        self.nominal_mean_power = None
        self.mean_dayly_energy = None

        self.regulation_time = None
        self.retrieval_time = None
        self.regulated_power = None
        self.storage_capacity = None
        self.regulation_power_efficiency = None

        self.net_power_efficiency = None

        self.gross_yearly_enrg = None
        self.net_yearly_enrg = None

        self.total_grey_enrg = None

        self.update()

    def update(self):
        self.total_mirror_area = self.mirror_area * self.n_mirror
        self.total_foot_print = self.total_mirror_area * self.ground_ratio

        self.nominal_peak_power = self.ref_yearly_sun_power * self.total_mirror_area * self.gross_power_efficiency
        self.nominal_mean_power = self.nominal_peak_power * self.load_factor
        self.mean_dayly_energy = self.nominal_mean_power * one_day

        self.regulation_time = one_day * (self.load_factor + (1. - self.load_factor)*self.regulation_factor)
        self.retrieval_time = one_day * (1. - self.load_factor)*self.regulation_factor
        self.regulated_power = self.nominal_peak_power / (1. + self.regulation_factor*(1.-self.load_factor)/(self.load_factor*self.storage_efficiency))
        self.storage_capacity = (self.nominal_peak_power - self.regulated_power) * self.load_factor * self.storage_efficiency * one_day
        self.regulation_power_efficiency = self.regulated_power * self.regulation_time / self.mean_dayly_energy

        self.net_power_efficiency = self.gross_power_efficiency * self.regulation_power_efficiency * (1.-self.grey_energy_ratio)

        self.gross_yearly_enrg = self.regulated_power * self.regulation_time * 365.
        self.net_yearly_enrg = self.gross_yearly_enrg - self.gross_yearly_enrg * self.grey_energy_ratio

        self.total_grey_enrg = self.gross_yearly_enrg * self.grey_energy_ratio * self.life_time


st1 = StPowerPlant(7500., 250., 0.51)

print("")
print("Power plant type = ",st1.type)
print("--------------------------------------------------")
print("Nominal peak power = ", "%8.1f" % unit.MW_W(st1.nominal_peak_power), " MW")
print("Nominal mean power = ", "%8.1f" % unit.MW_W(st1.nominal_mean_power), " MW")
print("Regulated power = ", "%8.1f" % unit.MW_W(st1.regulated_power), " MW")
print("Regulation time = ", "%8.1f" % unit.h_s(st1.regulation_time), " h")
print("Retrieval time = ", "%8.1f" % unit.h_s(st1.retrieval_time), " h")
print("Storage capacity = ", "%8.1f" % unit.MWh_J(st1.storage_capacity), " MWh")
print("Yearly gross production = ", "%8.1f" % unit.GWh_J(st1.gross_yearly_enrg), " GWh")
print("Yearly net production = ", "%8.1f" % unit.GWh_J(st1.net_yearly_enrg), " GWh")
print("Net power efficiency = ", "%8.3f" % st1.net_power_efficiency)
print("Total grey energy = ", "%8.1f" % unit.GWh_J(st1.total_grey_enrg), " GWh")
print("Total footprint = ", "%8.1f" % unit.km2_m2(st1.total_foot_print), " km2")



class PvPowerPlant(object):

    def __init__(self, n_panel, ref_sun_pw, reg_factor):
        self.type = "Photovoltaïc panel"
        self.regulation_factor = reg_factor
        self.n_panel = n_panel
        self.panel_area = 8.
        self.ground_ratio = 2.6
        self.life_time = 25.

        self.gross_power_efficiency = 0.15
        self.storage_efficiency = 0.80
        self.grey_energy_ratio = 0.11

        self.ref_yearly_sun_power = ref_sun_pw
        self.load_factor = 0.14

        self.total_panel_area = None
        self.total_foot_print = None

        self.nominal_peak_power = None
        self.nominal_mean_power = None
        self.mean_dayly_energy = None

        self.regulation_time = None
        self.retrieval_time = None
        self.regulated_power = None
        self.storage_capacity = None
        self.regulation_power_efficiency = None

        self.net_power_efficiency = None

        self.gross_yearly_enrg = None
        self.net_yearly_enrg = None

        self.total_grey_enrg = None

        self.update()

    def update(self):
        self.total_panel_area = self.panel_area * self.n_panel
        self.total_foot_print = self.total_panel_area * self.ground_ratio

        self.nominal_peak_power = self.ref_yearly_sun_power * self.total_panel_area * self.gross_power_efficiency
        self.nominal_mean_power = self.nominal_peak_power * self.load_factor
        self.mean_dayly_energy = self.nominal_mean_power * one_day

        self.regulation_time = one_day * (self.load_factor + (1. - self.load_factor)*self.regulation_factor)
        self.retrieval_time = one_day * (1. - self.load_factor)*self.regulation_factor
        self.regulated_power = self.nominal_peak_power / (1. + self.regulation_factor*(1.-self.load_factor)/(self.load_factor*self.storage_efficiency))
        self.storage_capacity = (self.nominal_peak_power - self.regulated_power) * self.load_factor * self.storage_efficiency * one_day
        self.regulation_power_efficiency = self.regulated_power * self.regulation_time / self.mean_dayly_energy

        self.net_power_efficiency = self.gross_power_efficiency * self.regulation_power_efficiency * (1.-self.grey_energy_ratio)

        self.gross_yearly_enrg = self.regulated_power * self.regulation_time * 365.
        self.net_yearly_enrg = self.gross_yearly_enrg - self.gross_yearly_enrg * self.grey_energy_ratio

        self.total_grey_enrg = self.gross_yearly_enrg * self.grey_energy_ratio * self.life_time



pv1 = PvPowerPlant(1e6, 250., 0.)

print("")
print("Power plant type = ",pv1.type)
print("--------------------------------------------------")
print("Nominal peak power = ", "%8.1f" % unit.MW_W(pv1.nominal_peak_power), " MW")
print("Nominal mean power = ", "%8.1f" % unit.MW_W(pv1.nominal_mean_power), " MW")
print("Regulated power = ", "%8.1f" % unit.MW_W(pv1.regulated_power), " MW")
print("Regulation time = ", "%8.1f" % unit.h_s(pv1.regulation_time), " h")
print("Retrieval time = ", "%8.1f" % unit.h_s(pv1.retrieval_time), " h")
print("Storage capacity = ", "%8.1f" % unit.MWh_J(pv1.storage_capacity), " MWh")
print("Yearly gross production = ", "%8.1f" % unit.GWh_J(pv1.gross_yearly_enrg), " GWh")
print("Yearly net production = ", "%8.1f" % unit.GWh_J(pv1.net_yearly_enrg), " GWh")
print("Net power efficiency = ", "%8.3f" % pv1.net_power_efficiency)
print("Total grey energy = ", "%8.1f" % unit.GWh_J(pv1.total_grey_enrg), " GWh")
print("Total footprint = ", "%8.1f" % unit.km2_m2(pv1.total_foot_print), " km2")





class EolPowerPlant(object):

    def __init__(self, n_rotor, location):
        self.type = "Wind turbine"
        self.location = location
        self.n_rotor = n_rotor
        self.rotor_width = 90.
        self.rotor_peak_power = 10.e6
        self.life_time = 20.

        self.rotor_area = None
        self.load_factor = None
        self.rotor_footprint = None
        self.total_foot_print = None

        self.rotor_grey_enrg = None
        self.total_grey_enrg = None

        self.nominal_peak_power = None
        self.nominal_gross_power = None
        self.gross_yearly_enrg = None

        self.net_yearly_enrg = None
        self.nominal_net_power = None

        self.update()

    def update(self):
        self.load_factor = {"onshore":0.30,
                            "offshore":0.40
                            }.get(self.location, "Error, location is unknown")

        self.rotor_footprint = 0.25e6*(self.rotor_width/90.)

        self.rotor_area = 0.25*np.pi*self.rotor_width**2

        self.rotor_grey_enrg = {"onshore": unit.J_GWh(1.27) * (self.rotor_area / 6362.),
                                "offshore": unit.J_GWh(2.28) * (self.rotor_area / 6362.)
                                }.get(self.location, "Error, location is unknown")

        self.total_foot_print = self.rotor_footprint * self.n_rotor

        self.total_grey_enrg = self.rotor_grey_enrg * self.n_rotor

        self.nominal_peak_power = self.rotor_peak_power * self.n_rotor
        self.nominal_gross_power = self.nominal_peak_power * self.load_factor
        self.gross_yearly_enrg = self.nominal_gross_power * one_year

        self.net_yearly_enrg = (self.gross_yearly_enrg * self.life_time - self.total_grey_enrg) / self.life_time
        self.nominal_net_power = self.net_yearly_enrg / one_year



eol1 = EolPowerPlant(25, "onshore")

print("")
print("Power plant type = ",eol1.type)
print("--------------------------------------------------")
print("Nominal peak power = ", "%8.1f" % unit.MW_W(eol1.nominal_peak_power), " MW")
print("Nominal mean power = ", "%8.1f" % unit.MW_W(eol1.nominal_gross_power), " MW")
print("Yearly gross production = ", "%8.1f" % unit.GWh_J(eol1.gross_yearly_enrg), " GWh")
print("Yearly net production = ", "%8.1f" % unit.GWh_J(eol1.net_yearly_enrg), " GWh")
print("Total grey energy = ", "%8.1f" % unit.GWh_J(eol1.total_grey_enrg), " GWh")
print("Total footprint = ", "%8.1f" % unit.km2_m2(eol1.total_foot_print), " km2")






class NuclearPowerPlant(object):

    def __init__(self, n_core):
        self.type = "Nuclear reactor"
        self.n_core = n_core

        self.core_peak_power = 1.0e9
        self.load_factor = 0.7
        self.life_time = 50.

        self.grey_energy_ratio = 0.2
        self.total_foot_print = 1.e6

        self.total_grey_enrg = None

        self.nominal_peak_power = None
        self.nominal_gross_power = None
        self.gross_yearly_enrg = None

        self.net_yearly_enrg = None
        self.nominal_net_power = None

        self.update()

    def update(self):
        self.nominal_peak_power = self.core_peak_power * self.n_core
        self.nominal_gross_power = self.nominal_peak_power * self.load_factor
        self.gross_yearly_enrg = self.nominal_gross_power * one_year

        self.total_grey_enrg = self.gross_yearly_enrg * self.life_time * self.grey_energy_ratio

        self.net_yearly_enrg = self.gross_yearly_enrg * self.life_time * (1. - self.grey_energy_ratio) / self.life_time
        self.nominal_net_power = self.net_yearly_enrg / one_year



atom1 = NuclearPowerPlant(4)

print("")
print("Power plant type = ",atom1.type)
print("--------------------------------------------------")
print("Nominal peak power = ", "%8.1f" % unit.GW_W(atom1.nominal_peak_power), " GW")
print("Nominal mean power = ", "%8.1f" % unit.GW_W(atom1.nominal_gross_power), " GW")
print("Yearly gross production = ", "%8.1f" % unit.TWh_J(atom1.gross_yearly_enrg), " TWh")
print("Yearly net production = ", "%8.1f" % unit.TWh_J(atom1.net_yearly_enrg), " TWh")
print("Total grey energy = ", "%8.1f" % unit.TWh_J(atom1.total_grey_enrg), " TWh")
print("Total footprint = ", "%8.1f" % unit.km2_m2(atom1.total_foot_print), " km2")
