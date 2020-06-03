#!/usr/bin/env python3
"""


:author: DRUOT Thierry, MONROLIN Nicolas

"""

DATA_DICT = {
    "body_type": {"unit":"string", "mag":8, "txt":"Type of main body, 'fuselage' or 'blended'"},
    "wing_type": {"unit":"string", "mag":6, "txt":"Type of lifting body, 'classic' or 'blended'"},
    "wing_attachment": {"unit":"string", "mag":4, "txt":"Position of wing attachment, 'low' or 'high'"},
    "stab_architecture": {"unit":"string", "mag":6, "txt":"Type of stabilizers, 'classic', 't_tail' or 'h_tail'"},
    "tank_architecture": {"unit":"string", "mag":10, "txt":"Type of tank, 'wing_box', 'piggy_back' or 'pods'"},
    "number_of_engine": {"unit":"string", "mag":6, "txt":"Number of engine, 'twin' or 'quadri'"},
    "nacelle_attachment": {"unit":"string", "mag":4, "txt":"Position of nacelle attachment, 'wing', 'pod' or 'rear'"},
    "power_architecture": {"unit":"string", "mag":4, "txt":"Propulsive architecture, 'tf', 'extf', 'ef'"},
    "power_source": {"unit":"string", "mag":9, "txt":"Type power source, 'fuel', 'battery' or 'fuel_cell"},
    "fuel_type": {"unit":"string", "mag":9, "txt":"Type energy source, 'kerosene', 'methane', 'liquid_h2' or 'battery"},
    "width": {"unit":"m", "mag":1e0, "txt":"Width of the component"},
    "height": {"unit":"m", "mag":1e0, "txt":"Height of the component"},
    "length": {"unit":"m", "mag":1e1, "txt":"Length of the component"},
    "body_width": {"unit":"m", "mag":1e1, "txt":"Width of the component generating the boundary layer"},
    "body_length": {"unit":"m", "mag":1e1, "txt":"Length of the component generating the boundary layer"},
    "forward_limit": {"unit":"m", "mag":1e0, "txt":"Distance between fuselage nose and forward cabin wall"},
    "wall_thickness": {"unit":"m", "mag":1e0, "txt":"Fuselage wall total tchickness"},
    "tail_cone_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Fuselage tail cone length over fuselage diameter"},
    "tail_cone_length": {"unit":"m", "mag":1e1, "txt":"Length of the tapered rear part of the main body"},
    "projected_area": {"unit":"m2", "mag":1e2, "txt":"Cabin efficiency parameter ~ cabin length times fuselage width"},
    "frame_origin": {"unit":"m", "mag":1e1, "txt":"Position of the reference point of the component in the assembly"},
    "mass": {"unit":"kg", "mag":1e3, "txt":"Masse of the component"},
    "cg": {"unit":"m", "mag":1e1, "txt":"Position of the center of gravity of the component in the assembly"},
    "inertia_tensor": {"unit":"kg.m2", "mag":1e5, "txt":"Inertia tensor of the component in its reference point"},
    "gross_wet_area": {"unit":"m2", "mag":1e1, "txt":"Gross wetted area of the component"},
    "net_wet_area": {"unit":"m2", "mag":1e1, "txt":"Net wetted area of the component"},
    "aero_length": {"unit":"m", "mag":1e1, "txt":"Characteristic length of the component for friction drag estimation"},
    "form_factor": {"unit":"no_dim", "mag":1e0, "txt":"Form factor of the conponent for form and friction drag estimation"},
    "co2_metric_area": {"unit":"m2", "mag":1e2, "txt":"Refernce cabin area for Fuel Efficiency Metric estimation"},
    "furnishing_mass": {"unit":"kg", "mag":1e3, "txt":"Furnishing mass (seats, monuments, toilets, ...)"},
    "m_furnishing": {"unit":"kg", "mag":1e3, "txt":"Furnishing mass (seats, monuments, toilets, ...)"},
    "op_item_mass": {"unit":"kg", "mag":1e3, "txt":"Operator items mass (crews, water, food, ...)"},
    "m_op_item": {"unit":"kg", "mag":1e3, "txt":"Operator items mass (crews, water, food, ...)"},
    "container_pallet_mass": {"unit":"kg", "mag":1e3, "txt":"Container & pallet mass if any"},
    "wing_mass": {"unit":"kg", "mag":1e3, "txt":"Wing mass"},
    "body_mass": {"unit":"kg", "mag":1e3, "txt":"Main body mass"},
    "htp_mass": {"unit":"kg", "mag":1e3, "txt":"Horizontal stabilizer mass"},
    "vtp_mass": {"unit":"kg", "mag":1e3, "txt":"Vertical stabilizer mass"},
    "tank_mass": {"unit":"kg", "mag":1e3, "txt":"Tank mass"},
    "ldg_mass": {"unit":"kg", "mag":1e3, "txt":"Landing gear mass"},
    "system_mass": {"unit":"kg", "mag":1e3, "txt":"System mass"},
    "propeller_mass": {"unit":"kg", "mag":1e3, "txt":"Propeller mass if any"},
    "engine_mass": {"unit":"kg", "mag":1e3, "txt":"Engine mass"},
    "pylon_mass": {"unit":"kg", "mag":1e2, "txt":"Pylon mass if any"},
    "nominal_payload": {"unit":"kg", "mag":1e4, "txt":"Reference payload for design"},
    "maximum_payload": {"unit":"kg", "mag":1e4, "txt":"Maximum payload for design"},
    "cg_furnishing": {"unit":"m", "mag":1e1, "txt":"Position of the CG of furnishing in the assembly"},
    "cg_op_item": {"unit":"m", "mag":1e1, "txt":"Position of the CG of operator items in the assembly"},
    "max_fwd_req_cg": {"unit":"m", "mag":1e1, "txt":"Maximum forward position of the payload"},
    "max_fwd_mass": {"unit":"kg", "mag":1e4, "txt":"Mass corresponding to maximum forward position of the payload"},
    "max_bwd_req_cg": {"unit":"m", "mag":1e1, "txt":"Maximum backward position of the payload"},
    "max_bwd_mass": {"unit":"kg", "mag":1e4, "txt":"Mass corresponding to maximum backward position of the payload"},
    "n_pax_ref": {"unit":"int", "mag":1e2, "txt":"Reference number of passenger for design"},
    "n_pax_front": {"unit":"int", "mag":1e2, "txt":"Number of front seats in economy class"},
    "n_aisle": {"unit":"int", "mag":1e0, "txt":"Number of aisle in economy class"},
    "m_pax_nominal": {"unit":"int", "mag":1e2, "txt":"Reference mass allowance per passenger for design"},
    "m_pax_max": {"unit":"int", "mag":1e2, "txt":"Maximum mass allowance per passenger for design"},
    "cruise_disa": {"unit":"degK", "mag":1e0, "txt":"Temperature shift versus ISA in cruise for design"},
    "cruise_altp": {"unit":"ft", "mag":1e4, "txt":"Mean cruise altitude for design"},
    "cruise_mach": {"unit":"mach", "mag":1e0, "txt":"Cruise Mach number for design"},
    "design_range": {"unit":"NM", "mag":1e3, "txt":"Design range"},
    "cost_range": {"unit":"NM", "mag":1e2, "txt":"Reference range for cost evaluation"},
    "area": {"unit":"m2", "mag":1e2, "txt":"Geometric reference area of the lifting surface"},
    "span": {"unit":"m", "mag":1e1, "txt":"Spanwise dimension of the lifting surface"},
    "aspect_ratio": {"unit":"no_dim", "mag":1e1, "txt":"Aspect ratio of the lifting surface"},
    "taper_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Taper ratio of the lifting surface"},
    "sweep0": {"unit":"deg", "mag":1e0, "txt":"Leading edge sweep angle of the lifting surface"},
    "sweep25": {"unit":"deg", "mag":1e0, "txt":"Sweep angle at 25% of the chords of the lifting surface"},
    "sweep100": {"unit":"deg", "mag":1e0, "txt":"Trailing edge sweep angle of the lifting surface"},
    "dihedral": {"unit":"deg", "mag":1e0, "txt":"Dihedral angle of the lifting surface"},
    "setting": {"unit":"deg", "mag":1e0, "txt":"Setting angle of the lifting surface"},
    "hld_type": {"unit":"int", "mag":1e0, "txt":"Type of high lift devices (0,1,2,....,10)"},
    "induced_drag_factor": {"unit":"no_dim", "mag":1e0, "txt":"Inverse of Oswald factor of the lifting surface"},
    "axe_loc": {"unit":"m", "mag":1e1, "txt":"Position of the central chord of the lifting surface"},
    "axe_toc": {"unit":"no_dim", "mag":1e0, "txt":"Thickness to chord ratio of the central chord of the lifting surface"},
    "axe_c": {"unit":"m", "mag":1e1, "txt":"Central chord length of the lifting surface"},
    "root_loc": {"unit":"m", "mag":1e1, "txt":"Position of the root chord of the lifting surface"},
    "root_toc": {"unit":"no_dim", "mag":1e0, "txt":"Thickness to chord ratio of the root chord of the lifting surface"},
    "root_c": {"unit":"m", "mag":1e1, "txt":"Root chord length of the lifting surface"},
    "kink_loc": {"unit":"m", "mag":1e1, "txt":"Position of the kink chord of the lifting surface"},
    "kink_toc": {"unit":"no_dim", "mag":1e0, "txt":"Thickness to chord ratio of the kink chord of the lifting surface"},
    "kink_c": {"unit":"m", "mag":1e1, "txt":"Kink chord length of the lifting surface"},
    "tip_loc": {"unit":"m", "mag":1e1, "txt":"Position of the tip chord of the lifting surface"},
    "tip_toc": {"unit":"no_dim", "mag":1e0, "txt":"Thickness to chord ratio of the tip chord of the lifting surface"},
    "tip_c": {"unit":"m", "mag":1e1, "txt":"Tip chord length of the lifting surface"},
    "mac_loc": {"unit":"m", "mag":1e1, "txt":"Position of the mean aerodynamic chord of the lifting surface"},
    "mac": {"unit":"m", "mag":1e1, "txt":"Mean aerodynamic chord length of the lifting surface"},
    "toc": {"unit":"no_dim", "mag":1e0, "txt":"Thickness to chord ratio of the lifting surface"},
    "volume_factor": {"unit":"no_dim", "mag":1e0, "txt":"Volume coefficient of the horizontal stabilizer"},
    "thrust_volume_factor": {"unit":"no_dim", "mag":1e0, "txt":"Volume coefficient of the vertical stabilizer according to engine failure"},
    "wing_volume_factor": {"unit":"no_dim", "mag":1e0, "txt":"Volume coefficient of the vertical stabilizer according to wing"},
    "anchor_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Relative position of the reference point of the stabilization surface"},
    "lever_arm": {"unit":"m", "mag":1e1, "txt":"Lever arm of the stabilization surface, 25%cma wing to 25% cma surface"},
    "fuel_density": {"unit":"kg/m3", "mag":1e3, "txt":"Density of the used storage medium"},
    "shell_parameter": {"unit":"bar.l/kg", "mag":1e2, "txt":"Tank structural efficiency"},
    "shell_density": {"unit":"kg/m3", "mag":1e3, "txt":"Tank shell material density"},
    "fuel_pressure": {"unit":"bar", "mag":1e2, "txt":"Maximum over pressure of the fuel in the tank"},
    "structure_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Ratio of the total volume of the tank used for tank structure"},
    "surface_mass": {"unit":"kg/m2", "mag":1e1, "txt":"Mass of tank structure per tank surface unit"},
    "cantilever_volume": {"unit":"m3", "mag":1e1, "txt":"Tank volume outside of the main body"},
    "central_volume": {"unit":"m3", "mag":1e1, "txt":"Tank volume inside of the main body"},
    "fuel_cantilever_cg": {"unit":"m", "mag":1e1, "txt":"Position of the CG of the fuel volume which is outside of the main body"},
    "fuel_central_cg": {"unit":"m", "mag":1e1, "txt":"Position of the CG of the fuel volume which is in the main body"},
    "fuel_total_cg": {"unit":"m", "mag":1e1, "txt":"Position of the CG of the total fuel volume"},
    "max_volume": {"unit":"m3", "mag":1e1, "txt":"Total available volume for fuel"},
    "mfw_volume_limited": {"unit":"kg", "mag":1e3, "txt":"Maximum fuel mass according to available volume"},
    "volume": {"unit":"m3", "mag":1e1, "txt":"Volume of the component"},
    "wing_axe_c": {"unit":"m", "mag":1e0, "txt":"Wing chord length at component axis span wise position"},
    "wing_axe_x": {"unit":"m", "mag":1e1, "txt":"X wise position of the wing chord at component axis span wise position"},
    "lateral_margin": {"unit":"no_dim", "mag":1e0, "txt":"Lateral margin as a fraction of nacelle width"},
    "vertical_margin": {"unit":"no_dim", "mag":1e0, "txt":"vertical margin as a fraction of nacelle width"},
    "x_loc_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Fraction of the tank length behind the wing"},
    "span_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Relative span wise position of the tank"},
    "fuel_max_fwd_cg": {"unit":"m", "mag":1e1, "txt":"Maximum forward position of the fuel"},
    "fuel_max_fwd_mass": {"unit":"kg", "mag":1e3, "txt":"Fuel mass corresponding to mximum forward position"},
    "fuel_max_bwd_cg": {"unit":"m", "mag":1e1, "txt":"Maximum backward position of the fuel"},
    "fuel_max_bwd_mass": {"unit":"kg", "mag":1e3, "txt":"Fuel mass corresponding to mximum backward position"},
    "n_engine": {"unit":"int", "mag":1e0, "txt":"Numeric number of engine"},
    "reference_thrust": {"unit":"daN", "mag":1e5, "txt":"Engine reference thrust, thrust(sea level, ISA+15, Mach 0.25)/0.8"},
    "reference_power": {"unit":"kW", "mag":1e5, "txt":"Engine reference power, power(sea level, ISA+15, Mach 0.25)/0.8"},
    "reference_offtake": {"unit":"kW", "mag":1e4, "txt":"Refrence power offtake for design"},
    "MTO": {"unit":"no_dim", "mag":1e0, "txt":"Max Takeoff rating factor"},
    "MCN": {"unit":"no_dim", "mag":1e0, "txt":"Maxi Continuous rating factor"},
    "MCL": {"unit":"no_dim", "mag":1e0, "txt":"Max Climb rating factor"},
    "MCR": {"unit":"no_dim", "mag":1e0, "txt":"Max Cruise rating factor"},
    "FID": {"unit":"no_dim", "mag":1e0, "txt":"Flight idle rating factor"},
    "tune_factor": {"unit":"no_dim", "mag":1e0, "txt":"Factor on unitary engine thrust to match with reference thrust definition"},
    "engine_bpr": {"unit":"no_dim", "mag":1e0, "txt":"Reference By Pass Ratio of the engine"},
    "core_thrust_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Reference ratio of the total thrust delivered by the core"},
    "fan_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Classical fan efficiency"},
    "propeller_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Propeller like fan efficiency Thrust.Speed/shaft_power"},
    "rating": {"unit":"string", "mag":3, "txt":"Engine rating name ('MTO','MCN','MCL','MCR','FID'"},
    "bli_effect": {"unit":"string", "mag":3, "txt":"Taking into account boundary layer ingestion, 'yes' or 'no'"},
    "power": {"unit":"kW", "mag":1e3, "txt":"Engine input power (before controller)"},
    "motor_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Electric motor efficiency"},
    "controller_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Electric controller efficiency"},
    "generator_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Electric generator efficiency"},
    "rectifier_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Electric rectifier efficiency"},
    "wiring_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Electric wiring efficiency"},
    "motor_pw_density": {"unit":"kW/kg", "mag":1e1, "txt":"Electric motor power density"},
    "nacelle_pw_density": {"unit":"kW/kg", "mag":1e1, "txt":"Electric nacelle power density"},
    "controller_pw_density": {"unit":"kW/kg", "mag":1e1, "txt":"Electric controller power density"},
    "generator_pw_density": {"unit":"kW/kg", "mag":1e1, "txt":"Electric generator power density"},
    "rectifier_pw_density": {"unit":"kW/kg", "mag":1e1, "txt":"Electric rectifier power density"},
    "wiring_pw_density": {"unit":"kW/kg", "mag":1e1, "txt":"Electric wiring power density"},
    "cooling_pw_density": {"unit":"kW/kg", "mag":1e1, "txt":"Cooling power density"},
    "battery_density": {"unit":"kg/m3", "mag":1e3, "txt":"Battery density"},
    "battery_energy_density": {"unit":"kWh/kg", "mag":1e1, "txt":"Battery energy density"},
    "power_chain_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Global efficiency of the electric power chain"},
    "fuel_cell_pw_density": {"unit":"kW/kg", "mag":1e0, "txt":"Fuell cell power density"},
    "fuel_cell_efficiency": {"unit":"no_dim", "mag":1e0, "txt":"Fuell cell conversion efficiency"},
    "fuel_cell_mass": {"unit":"kg", "mag":1e3, "txt":"Fuell cell mass"},
    "global_energy_density": {"unit":"kWh:kg", "mag":1e0, "txt":"Global energy density, fuel + tank + fuel cell"},
    "power_chain_mass": {"unit":"no_dim", "mag":1e0, "txt":"Mass of power electric sub system"},
    "propeller_width": {"unit":"m", "mag":1e0, "txt":"Propeller diameter"},
    "propeller_disk_load": {"unit":"daN/m2", "mag":1e2, "txt":"Propeller disk load"},
    "hub_width": {"unit":"m", "mag":1e0, "txt":"Fan hub diameter"},
    "fan_width": {"unit":"m", "mag":1e0, "txt":"Fan diameter"},
    "nozzle_area": {"unit":"m2", "mag":1e0, "txt":"Nozzle area"},
    "fuel_flow": {"unit":"kg/s", "mag":1e0, "txt":"Fuel flow"},
    "fuel_heat": {"unit":"MJ/kg", "mag":1e1, "txt":"Fuel heating value"},
    "sec_type": {"unit":"string", "mag":6, "txt":"Type of Specific Energy Consumption, 'thrust' or 'power'"},
    "sec": {"unit":"kW/daN", "mag":1e0, "txt":"Specific Energy Consumption"},
    "sfc_type": {"unit":"string", "mag":6, "txt":"Type of Specific Fuel Consumption, 'thrust' or 'power'"},
    "tsfc": {"unit":"kg/daN/h", "mag":1e0, "txt":"Specific Fuel Consumption versus thrust"},
    "psfc": {"unit":"kg/kW/h", "mag":1e0, "txt":"Specific Fuel Consumption versus power"},
    "T41": {"unit":"Kelvin", "mag":1e3, "txt":"Temperature just after combustion chamber (turbine entry)"},
    "nei": {"unit":"int", "mag":1e0, "txt":"Number of engine inoperative, typically 0 or 1"},
    "disa": {"unit":"degK", "mag":1e1, "txt":"Temperature shift versus ISA conditions"},
    "altp": {"unit":"ft", "mag":1e4, "txt":"Target pressure altitude"},
    "mach": {"unit":"mach", "mag":1e0, "txt":"Mach number"},
    "thrust": {"unit":"daN", "mag":1e3, "txt":"Engine thrust"},
    "thrust_opt": {"unit":"daN", "mag":1e3, "txt":"Required engine thrust"},
    "kfn_opt": {"unit":"no_dim", "mag":1e0, "txt":"Ratio required thrust over effective engine thrust"},
    "speed_mode": {"unit":"string", "mag":4, "txt":"Constant CAS : 'cas' or constant Mach : 'mach'"},
    "kmtow": {"unit":"no_dim", "mag":1e0, "txt":"Ratio of MTOW defining the aircraft weight"},
    "kmlw": {"unit":"no_dim", "mag":1e0, "txt":"Ratio of MLW defining the aircraft weight"},
    "kvs1g": {"unit":"no_dim", "mag":1e0, "txt":"Applicable ratio of stalling speed at 1g"},
    "kvs1g_eff": {"unit":"no_dim", "mag":1e0, "txt":"Effective ratio of stalling speed at 1g"},
    "s2_min_path": {"unit":"%", "mag":1e0, "txt":"Minimum trajectory slope at 35ft for take off"},
    "s2_path": {"unit":"%", "mag":1e0, "txt":"Airplane trajectory slope at 35ft during take off"},
    "tofl_req": {"unit":"m", "mag":1e3, "txt":"Maximum take off field length required in given conditions"},
    "tofl_eff": {"unit":"m", "mag":1e3, "txt":"Effective take off field length in given conditions"},
    "app_speed_req": {"unit":"kt", "mag":1e2, "txt":"Maximum approach speed required in given conditions"},
    "app_speed_eff": {"unit":"kt", "mag":1e2, "txt":"Effective approach speed in given conditions"},
    "path_req": {"unit":"%", "mag":1e0, "txt":"Minimum trajectory slope required in given conditions"},
    "path_eff": {"unit":"%", "mag":1e0, "txt":"Effective trajectory slope in given conditions"},
    "vz_req": {"unit":"ft/min", "mag":1e2, "txt":"Minimum vertical speed required in given conditions"},
    "vz_eff": {"unit":"ft/min", "mag":1e2, "txt":"Effective vertical speed in given conditions"},
    "cx_correction": {"unit":"no_dim", "mag":1e-4, "txt":"Additive correction on airplane total drag coefficient"},
    "cruise_lodmax": {"unit":"no_dim", "mag":1e1, "txt":"Maximum lift over Drag ratio in cruise"},
    "cz_cruise_lodmax": {"unit":"no_dim", "mag":1e0, "txt":"Lift coefficient for maximum lift over Drag ratio in cruise"},
    "hld_conf_clean": {"unit":"no_dim", "mag":1e0, "txt":"Deflection parameter corresponding to high lift devices retracted, typically 0"},
    "czmax_conf_clean": {"unit":"no_dim", "mag":1e0, "txt":"Maximum lift coefficient with high lift devices retracted"},
    "hld_conf_to": {"unit":"no_dim", "mag":1e0, "txt":"Deflection parameter corresponding to high lift devices in take off configuration"},
    "czmax_conf_to": {"unit":"no_dim", "mag":1e0, "txt":"Maximum lift coefficient with high lift devices in take off configuration"},
    "hld_conf_ld": {"unit":"no_dim", "mag":1e0, "txt":"Deflection parameter corresponding to high lift devices in landing configuration, typically 1"},
    "czmax_conf_ld": {"unit":"no_dim", "mag":1e0, "txt":"Maximum lift coefficient with high lift devices in landing configuration"},
    "mtow": {"unit":"kg", "mag":1e5, "txt":"Maximum Take Off Weight"},
    "mzfw": {"unit":"kg", "mag":1e5, "txt":"Maximum Zero Fuel Weight"},
    "mlw": {"unit":"kg", "mag":1e5, "txt":"Maximum Landing Weight"},
    "owe": {"unit":"kg", "mag":1e5, "txt":"Operational Weight Empty"},
    "mwe": {"unit":"kg", "mag":1e5, "txt":"Manufacturer Weight Empty"},
    "mfw": {"unit":"kg", "mag":1e5, "txt":"Maximum Fuel Weight"},
    "hld_conf": {"unit":"no_dim", "mag":1e0, "txt":"Current deflection parameter corresponding to high lift devices configuration"},
    "v2": {"unit":"kt", "mag":1e2, "txt":"Airplane speed in CAS at 35ft during take off"},
    "mach2": {"unit":"mach", "mag":1e0, "txt":"Airplane speed in Mach number at 35ft during take off"},
    "limit": {"unit":"string", "mag":2, "txt":"Active limit during take off, can be 'fl':field length, 's2':second segment path"},
    "mach_opt": {"unit":"mach", "mag":1e0, "txt":"Optimal Mach number according to requirement"},
    "ttc_req": {"unit":"min", "mag":1e1, "txt":"Maximum time to climb required in given conditions"},
    "ttc_eff": {"unit":"min", "mag":1e1, "txt":"Effective time to climb in given conditions"},
    "altp1": {"unit":"ft", "mag":1e4, "txt":"Starting pressure altitude for climb trajectory, typically 1500ft"},
    "cas1": {"unit":"kt", "mag":1e2, "txt":"Calibrated Air Speed below altp1 during climb trajectory"},
    "altp2": {"unit":"ft", "mag":1e4, "txt":"Transtion pressure altitude from cas1 to cas2, typically 10000ft"},
    "cas2": {"unit":"kt", "mag":1e2, "txt":"Calibrated Air Speed above altp2"},
    "tow": {"unit":"kg", "mag":1e5, "txt":"Mission take off weight"},
    "range": {"unit":"NM", "mag":1e3, "txt":"Mission range"},
    "diversion_range": {"unit":"NM", "mag":1e1, "txt":"Range of diversion mission for reserve fuel evaluation"},
    "reserve_fuel_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Fraction of mission fuel for reserve fuel evaluation"},
    "reserve_enrg_ratio": {"unit":"no_dim", "mag":1e0, "txt":"Fraction of mission energy for reserve evaluation"},
    "holding_time": {"unit":"min", "mag":1e1, "txt":"Holding duration for reserve fuel evaluation"},
    "payload": {"unit":"kg", "mag":1e4, "txt":"Mission payload"},
    "time_block": {"unit":"h", "mag":1e1, "txt":"Mission block time"},
    "enrg_block": {"unit":"kWh", "mag":1e4, "txt":"Mission block energy"},
    "fuel_block": {"unit":"kg", "mag":1e4, "txt":"Mission block fuel"},
    "enrg_reserve": {"unit":"kWh", "mag":1e4, "txt":"Mission reserve energy"},
    "fuel_reserve": {"unit":"kg", "mag":1e3, "txt":"Mission reserve fuel"},
    "enrg_total": {"unit":"kWh", "mag":1e4, "txt":"Mission total energy"},
    "battery_mass": {"unit":"kg", "mag":1e3, "txt":"Required battery mass"},
    "fuel_total": {"unit":"kg", "mag":1e4, "txt":"Mission total fuel"},
    "irp": {"unit":"year", "mag":1e1, "txt":"Interest recovery period"},
    "period": {"unit":"year", "mag":1e1, "txt":"Utilization period"},
    "interest_rate": {"unit":"%", "mag":1e0, "txt":"Interest rate"},
    "specific_nacelle_cost": {"unit":"$/kg", "mag":1e1, "txt":"Specific maintenance cost per trip for tail cone mounted nacelle"},
    "labor_cost": {"unit":"$/h", "mag":1e1, "txt":"Labor cost"},
    "utilization": {"unit":"int", "mag":1e3, "txt":"Number of flights per year"},
    "engine_price": {"unit":"M$", "mag":1e1, "txt":"Price of one engine"},
    "gear_price": {"unit":"M$", "mag":1e1, "txt":"Price of landing gears"},
    "frame_price": {"unit":"M$", "mag":1e1, "txt":"Price of the airframe"},
    "energy_price": {"unit":"$/kWh", "mag":1e0, "txt":"Energy price"},
    "fuel_price": {"unit":"$/gal", "mag":1e0, "txt":"Fuel price"},
    "battery_price": {"unit":"$/kg", "mag":1e0, "txt":"Battery price"},
    "frame_cost": {"unit":"$/trip", "mag":1e3, "txt":"Airframe maintenance cost"},
    "engine_cost": {"unit":"$/trip", "mag":1e3, "txt":"Engine maintenance cost"},
    "cockpit_crew_cost": {"unit":"$/trip", "mag":1e3, "txt":"Cockpit crew cost"},
    "cabin_crew_cost": {"unit":"$/trip", "mag":1e3, "txt":"Cabin crew cost"},
    "landing_fees": {"unit":"$/trip", "mag":1e3, "txt":"Landing fees"},
    "navigation_fees": {"unit":"$/trip", "mag":1e3, "txt":"Navigation fees"},
    "catering_cost": {"unit":"$/trip", "mag":1e3, "txt":"Catering cost"},
    "pax_handling_cost": {"unit":"$/trip", "mag":1e3, "txt":"Passenger handling cost"},
    "ramp_handling_cost": {"unit":"$/trip", "mag":1e3, "txt":"Ramp handling cost"},
    "std_op_cost": {"unit":"$/trip", "mag":1e4, "txt":"Standard operating cost"},
    "cash_op_cost": {"unit":"$/trip", "mag":1e4, "txt":"Cash operating cost"},
    "direct_op_cost": {"unit":"$/trip", "mag":1e4, "txt":"Direct operating cost"},
    "fuel_cost": {"unit":"$/trip", "mag":1e4, "txt":"Fuel cost"},
    "aircraft_price": {"unit":"M$", "mag":1e5, "txt":"Aircraft price"},
    "total_investment": {"unit":"M$", "mag":1e4, "txt":"Total investmenent"},
    "interest": {"unit":"$/trip", "mag":1e3, "txt":"Interest"},
    "insurance": {"unit":"$/trip", "mag":1e3, "txt":"Insurance"},
    "depreciation": {"unit":"$/trip", "mag":1e3, "txt":"Depreciation"},
    "CO2_metric": {"unit":"kg/km/m0.48", "mag":1e0, "txt":"Fuel efficiency metric"},
    "CO2_index": {"unit":"g/kg", "mag":1e3, "txt":"Mass of carbon dioxide emitted per kg of fuel"},
    "CO_index": {"unit":"g/kg", "mag":1e-5, "txt":"Mass of carbon monoxide emitted per kg of fuel"},
    "H2O_index": {"unit":"g/kg", "mag":1e-5, "txt":"Mass of water emitted per kg of fuel"},
    "SO2_index": {"unit":"g/kg", "mag":1e-5, "txt":"Mass of sulfur dioxide emitted per kg of fuel"},
    "NOx_index": {"unit":"g/kg", "mag":1e-5, "txt":"Mass of nitrogen oxide emitted per kg of fuel"},
    "HC_index": {"unit":"g/kg", "mag":1e-5, "txt":"Mass of unburnt hydrocarbon emitted per kg of fuel"},
    "sulfuric_acid_index": {"unit":"g/kg", "mag":1e-5, "txt":"Mass of sulfuric acid emitted per kg of fuel"},
    "nitrous_acid_index": {"unit":"g/kg", "mag":1e-5, "txt":"Mass of nitrous acid emitted per kg of fuel"},
    "nitric_acid_index": {"unit":"g/kg", "mag":1e-5, "txt":"Mass of nitric acid emitted per kg of fuel"},
    "soot_index": {"unit":"int", "mag":1e12, "txt":"Number of soot particles emitted per kg of fuel"},
    "ktow": {"unit":"no_dim", "mag":1e0, "txt":"Ratio of TOW defining the aircraft weight for mission breguet range"},
    "crz_altp": {"unit":"ft", "mag":1e4, "txt":"Cruise altitude for design"},
    "crz_sar": {"unit":"NM/kg", "mag":1e0, "txt":"Cruise specific air range related to fuel"},
    "crz_esar": {"unit":"NM/kW", "mag":1e0, "txt":"Cruise specific air range related to power"},
    "crz_cz": {"unit":"no_dim", "mag":1e0, "txt":"Cruise lift coefficient"},
    "crz_lod": {"unit":"no_dim", "mag":1e0, "txt":"Cruise lift to drag ratio"},
    "crz_thrust": {"unit":"kN", "mag":1e0, "txt":"Total cruise thrust"},
    "crz_power": {"unit":"MW", "mag":1e0, "txt":"Total cruise power"},
    "crz_throttle": {"unit":"no_dim", "mag":1e0, "txt":"Cruise throttle versus MCR"},
    "crz_tsfc": {"unit":"kg/daN/h", "mag":1e0, "txt":"Cruise specific fuel consumption versus thrust"},
    "crz_psfc": {"unit":"kg/kW/h", "mag":1e0, "txt":"Cruise specific fuel consumption versus power"},
    "crz_sec": {"unit":"kW/daN", "mag":1e0, "txt":"Cruise specific energy consumption"},
    "max_sar_altp": {"unit":"ft", "mag":1e0, "txt":"Altitude of specific air range"},
    "max_sar": {"unit":"NM/kg", "mag":1e0, "txt":"Maximum specific air range"},
    "max_sar_cz": {"unit":"no_dim", "mag":1e0, "txt":"Lift coefficient for maximum specific air range"},
    "max_sar_lod": {"unit":"no_dim", "mag":1e0, "txt":"Lift to drag ratio for maximum specific air range"},
    "max_sar_thrust": {"unit":"kN", "mag":1e0, "txt":"Total thrust for maximum specific air range"},
    "max_sar_throttle": {"unit":"no_dim", "mag":1e0, "txt":"Throttle versus MCR for maximum specific air range"},
    "max_sar_tsfc": {"unit":"kg/daN/h", "mag":1e0, "txt":"Specific fuel consumption versus thrust for maximum specific air range"},
    "max_sar_psfc": {"unit":"kg/kW/h", "mag":1e0, "txt":"Specific fuel consumption versus power for maximum specific air range"},
    "max_esar_altp": {"unit":"ft", "mag":1e0, "txt":"Altitude of specific air range"},
    "max_esar": {"unit":"NM/kg", "mag":1e0, "txt":"Maximum specific air range"},
    "max_esar_cz": {"unit":"no_dim", "mag":1e0, "txt":"Lift coefficient for maximum specific air range"},
    "max_esar_lod": {"unit":"no_dim", "mag":1e0, "txt":"Lift to drag ratio for maximum specific air range"},
    "max_esar_thrust": {"unit":"kN", "mag":1e0, "txt":"Total thrust for maximum specific air range"},
    "max_esar_power": {"unit":"MW", "mag":1e0, "txt":"Total power for maximum specific air range"},
    "max_esar_throttle": {"unit":"no_dim", "mag":1e0, "txt":"Throttle versus MCR for maximum specific air range"},
    "max_esar_sec": {"unit":"kW/daN", "mag":1e0, "txt":"Specific energy consumption for maximum specific air range"},
    "wing_morphing" : {"unit":"string", "mag":19, "txt":"design of the wings : 'aspect_ratio_driven' or 'span_driven'"}
}

