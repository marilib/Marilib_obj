#!/usr/bin/env python3
"""
Created on Thu Jan 20 20:20:20 2020

:author: Conceptual Airplane Design & Operations (CADO team)
         Nicolas PETEILH, Pascal ROCHES, Nicolas MONROLIN, Thierry DRUOT
         Aircraft & Systems, Air Transport Department, ENAC
"""

import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import fsolve, least_squares

import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

import unit
import utils
from physical_data import PhysicalData
from models import DDM

from analyse_data import coloration, read_db, draw_reg, draw_hist, do_regression


#-----------------------------------------------------------------------------------------------------------------------
#
#  Analysis
#
#-----------------------------------------------------------------------------------------------------------------------


# Read data
#-------------------------------------------------------------------------------------------------------------------
path_to_data_base = "All_Data_v5.xlsx"

df,un = read_db(path_to_data_base)

# Remove A380-800 row and reset index
df = df[df['name']!='A380-800'].reset_index(drop=True)



# df1 = df[df['wing_span']<20].reset_index(drop=True).copy()    # Remove
df1 = df.copy()
un1 = un.copy()

df1 = df1[df1['name']!='GrobRangerG160'].reset_index(drop=True)
df1 = df1[df1['name']!='SF600ACanguro'].reset_index(drop=True)
df1 = df1[df1['name']!='VF600WMission'].reset_index(drop=True)

# #----------------------------------------------------------------------------------
# abs = "nominal_range"
# ord = "cruise_speed"
#
# df2 = df1[df1['airplane_type']=="general"].reset_index(drop=True).copy()    # Remove
# un2 = un1.copy()
#
# order = [1, 0]
# dict = do_regression(df2, un2, abs, ord, coloration, order)
#
# #----------------------------------------------------------------------------------
# abs = "nominal_range"
# ord = "cruise_speed"
#
# df2 = df1[df1['airplane_type']=="commuter"].reset_index(drop=True).copy()    # Remove
# un2 = un1.copy()
#
# order = [1, 0]
# dict = do_regression(df2, un2, abs, ord, coloration, order)
#
# #----------------------------------------------------------------------------------
# abs = "nominal_range"
# ord = "cruise_speed"
#
# df2 = df1[df1['cruise_speed']<1].reset_index(drop=True).copy()    # Remove
# un2 = un1.copy()
# un2[ord] = "mach"
#
# order = [2, 1, 0]
# dict = do_regression(df2, un2, abs, ord, coloration, order)

#----------------------------------------------------------------------------------
abs = "wing_area"
ord = "HTP_area"

order = [1, 0]
dict = do_regression(df1, un1, abs, ord, coloration, order)

# Coef =  [0.2398759  0.33909265]

#----------------------------------------------------------------------------------
abs = "wing_area"
ord = "VTP_area"

order = [2, 1]
dict = do_regression(df1, un1, abs, ord, coloration, order)

# Coef =  [-1.03984667e-04  1.83589484e-01]

#----------------------------------------------------------------------------------
abs = "fuselage_width"
ord = "total_length"

order = [2, 1]
dict = do_regression(df1, un1, abs, ord, coloration, order)

# Coef =  [0.35429986 8.55339511]



