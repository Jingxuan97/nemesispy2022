"""
Present results of end to end comparisons
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
sys.path.append('/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/')
from nemesispy.radtran.forward_model import ForwardModel
from nemesispy.radtran.fortran_wrapper import Nemesis_api
import time

### Reference Opacity Data
lowres_files = [
'/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/h2o',
'/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/co2',
'/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/co',
'/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/ch4']
cia_file_path='/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/cia/exocia_hitran12_200-3800K.tab'
folder_name = 'testing'


### Reference Constants
pi = np.pi
const = {
    'R_SUN': 6.95700e8,      # m solar radius
    'R_JUP': 7.1492e7,       # m nominal equatorial Jupiter radius (1 bar pressure level)
    'AU': 1.49598e11,        # m astronomical unit
    'k_B': 1.38065e-23,      # J K-1 Boltzmann constant
    'R': 8.31446,            # J mol-1 K-1 universal gas constant
    'G': 6.67430e-11,        # m3 kg-1 s-2 universal gravitational constant
    'N_A': 6.02214e23,       # Avagadro's number
    'AMU': 1.66054e-27,      # kg atomic mass unit
    'ATM': 101325,           # Pa atmospheric pressure
}

### Reference Planet Input
M_plt = 3.8951064000000004e+27 # kg
R_plt = 74065.70 * 1e3 # m
gas_id = np.array([  1, 2,  5,  6, 40, 39])
iso_id = np.array([0, 0, 0, 0, 0, 0])

T = np.array([2500.2 , 2319.3 , 2264.3 , 2251.7 , 2200.5 , 2100.1 , 1959.2 ,
       1814.4 , 1694.3 , 1598.8 , 1519.1 , 1449.7 , 1387.7 , 1332.5 ,
       1282.9 , 1237.7 , 1198.2 , 1165.8 , 1140.2 , 1122.5 , 1107.5 ,
       1096.4 , 1087.4 , 1083.2 , 1083.3 , 1082.9 , 1076.3 , 1065.7 ,
       1054.2 , 1042.6 , 1032.6 , 1024.7 , 1017.7 , 1010.  , 1001.9 ,
        991.91,  979.68,  966.51,  952.97,  939.26,  925.02,  909.57,
        892.74,  874.98,  857.56,  841.77,  828.64,  818.28,  811.49,
        807.76,  810.43,  817.1 ,  840.1 ])

P = np.array([1.7064e+07, 1.2054e+07, 8.5152e+06, 6.0152e+06, 4.2492e+06,
       3.0017e+06, 2.1204e+06, 1.4979e+06, 1.0581e+06, 7.4747e+05,
       5.2802e+05, 3.7300e+05, 2.6349e+05, 1.8613e+05, 1.3148e+05,
       9.2882e+04, 6.5613e+04, 4.6350e+04, 3.2742e+04, 2.3129e+04,
       1.6339e+04, 1.1542e+04, 8.1532e+03, 5.7595e+03, 4.0686e+03,
       2.8741e+03, 2.0303e+03, 1.4342e+03, 1.0131e+03, 7.1569e+02,
       5.0557e+02, 3.5714e+02, 2.5229e+02, 1.7822e+02, 1.2589e+02,
       8.8933e+01, 6.2823e+01, 4.4379e+01, 3.1350e+01, 2.2146e+01,
       1.5644e+01, 1.1051e+01, 7.8066e+00, 5.5146e+00, 3.8956e+00,
       2.7519e+00, 1.9440e+00, 1.3732e+00, 9.7006e-01, 6.8526e-01,
       4.8408e-01, 3.4196e-01, 2.4156e-01])
NMODEL = len(P)
H = np.linspace(0,1e5,NMODEL)
VMR = np.array([[4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01],
       [4.79650e-04, 4.64342e-04, 7.38846e-08, 1.32733e-07, 1.62329e-01,
        8.36727e-01]])

NLAYER = 20

### Reference Spectral Input
wave_grid = np.array([1.1425, 1.1775, 1.2125, 1.2475, 1.2825, 1.3175, 1.3525, 1.3875,
       1.4225, 1.4575, 1.4925, 1.5275, 1.5625, 1.5975, 1.6325, 3.6   ,
       4.5   ])

stellar_spec = np.array([3.341320e+25, 3.215455e+25, 3.101460e+25, 2.987110e+25,
       2.843440e+25, 2.738320e+25, 2.679875e+25, 2.598525e+25,
       2.505735e+25, 2.452230e+25, 2.391140e+25, 2.345905e+25,
       2.283720e+25, 2.203690e+25, 2.136015e+25, 1.234010e+24,
       4.422200e+23])

### Reference Atmospheric Model Input
# Gas Volume Mixing Ratio, constant with height
gas_id = np.array([  1, 2,  5,  6, 40, 39])
iso_id = np.array([0, 0, 0, 0, 0, 0])

### Benchmark Fortran forward model
folder_name = 'ftest'
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_path+'/'+folder_name) # move to designated process folder

start_time = time.time()
API = Nemesis_api(name=folder_name, NLAYER=NLAYER, gas_id_list=gas_id,
    iso_id_list=iso_id, wave_grid=wave_grid)
API.write_files(H_model=H, P_model=P, T_model=T,
    VMR_model=VMR)
API.run_forward_model()
wave, yerr, fotran_spec = API.read_output()
end_time = time.time()
print('runtime',end_time-start_time)