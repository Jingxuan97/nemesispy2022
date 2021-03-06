"""
Present results of end to end comparisons
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
sys.path.append('/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/')
from nemesispy.radtran.forward_model import ForwardModel
from nemesispy.radtran.benchmarking.point_benchmarking_fortran import Nemesis_api
from nemesispy.backup_functions.hydrostatic import adjust_hydrostatH
import time

### Reference Opacity Data
lowres_files = ['/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/h2o',
         '/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/co2',
         '/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/co',
         '/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/ch4']
cia_file_path='/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/cia/exocia_hitran12_200-3800K.tab'
folder_name = 'testing'

lowres_files = ['/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/h2o',
         '/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/co2',
         '/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/co',
         '/Users/jingxuanyang/Desktop/Workspace/nemesispy2022/nemesispy/data/ktables/ch4']

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
#R_star = 463892759.99999994 # m

### Reference Spectral Input
# Stellar spectrum
stellar_spec = np.array([3.341320e+25, 3.215455e+25, 3.101460e+25, 2.987110e+25,
       2.843440e+25, 2.738320e+25, 2.679875e+25, 2.598525e+25,
       2.505735e+25, 2.452230e+25, 2.391140e+25, 2.345905e+25,
       2.283720e+25, 2.203690e+25, 2.136015e+25, 1.234010e+24,
       4.422200e+23])

# Spectral output wavelengths in micron
wave_grid = np.array([1.1425, 1.1775, 1.2125, 1.2475, 1.2825, 1.3175, 1.3525, 1.3875,
       1.4225, 1.4575, 1.4925, 1.5275, 1.5625, 1.5975, 1.6325, 3.6   ,
       4.5   ])

### Reference Atmospheric Model Input
# Height in m
H = np.array([      0.     ,  103738.07012,  206341.39335,  305672.8162 ,
        400037.91149,  488380.27388,  570377.57036,  646857.33242,
        718496.09845,  785987.95083,  851242.50591,  914520.46249,
        976565.39549, 1037987.38369, 1099327.5361 , 1158956.80091,
       1221026.73382, 1280661.28989, 1341043.14058, 1404762.36466])

# H = np.linspace(0,1404762.36466,20)

# Pressure in pa, note 1 atm = 101325 pa
P = np.array([2.00000000e+06, 1.18757212e+06, 7.05163779e+05, 4.18716424e+05,
       2.48627977e+05, 1.47631828e+05, 8.76617219e+04, 5.20523088e+04,
       3.09079355e+04, 1.83527014e+04, 1.08975783e+04, 6.47083012e+03,
       3.84228875e+03, 2.28149750e+03, 1.35472142e+03, 8.04414702e+02,
       4.77650239e+02, 2.83622055e+02, 1.68410823e+02, 1.00000000e+02])

# Temperature in Kelvin
T = np.array([2294.22993056, 2275.69702232, 2221.47726725, 2124.54056941,
       1996.03871629, 1854.89143353, 1718.53879797, 1599.14914582,
       1502.97122783, 1431.0218576 , 1380.55933525, 1346.97814697,
       1325.49943114, 1312.13831743, 1303.97872899, 1299.05347108,
       1296.10266693, 1294.34217288, 1293.29484759, 1292.67284408])

NMODEL = len(H)
NLAYER = 20

# Ground temperature in Kelvin and path angle
T_ground = 0
path_angle = 90

# Gas Volume Mixing Ratio, constant with height
gas_id = np.array([  1, 2,  5,  6, 40, 39])
iso_id = np.array([0, 0, 0, 0, 0, 0])
H2_ratio = 0.864
VMR_H2O = 1.0E-4 * 1
VMR_CO2 = 1.0E-4 * 1
VMR_CO = 1.0E-4 * 1
VMR_CH4 = 1.0E-4 * 1
VMR_He = (np.ones(NMODEL)-VMR_H2O-VMR_CO2-VMR_CO-VMR_CH4)*(1-H2_ratio)
VMR_H2 = (np.ones(NMODEL)-VMR_H2O-VMR_CO2-VMR_CO-VMR_CH4)*H2_ratio
NVMR = 6
VMR = np.zeros((NMODEL,NVMR))
VMR[:,0] = VMR_H2O
VMR[:,1] = VMR_CO2
VMR[:,2] = VMR_CO
VMR[:,3] = VMR_CH4
VMR[:,4] = VMR_He
VMR[:,5] = VMR_H2

### Benchmark Fortran forward model
folder_name = 'present'
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
file_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_path+'/'+folder_name) # move to designated process folder

API = Nemesis_api(name=folder_name, NLAYER=NLAYER, gas_id_list=gas_id,
    iso_id_list=iso_id, wave_grid=wave_grid)
API.write_files(path_angle=path_angle, H_model=H, P_model=P, T_model=T,
    VMR_model=VMR)
API.run_forward_model()
wave, yerr, fotran_spec = API.read_output()

### Benchmark Python forward model
FM = ForwardModel()
FM.set_planet_model(M_plt=M_plt, R_plt=R_plt, gas_id_list=gas_id,
    iso_id_list=iso_id, NLAYER=NLAYER)
FM.set_opacity_data(kta_file_paths=lowres_files, cia_file_path=cia_file_path)

# Test hydrostatic routine
new_H = adjust_hydrostatH(H=H,P=P,T=T,ID=gas_id,VMR=VMR,M_plt=M_plt,R_plt=R_plt)
python_spec = FM.run_point_spectrum(H_model=new_H, P_model=P,
    T_model=T, VMR_model=VMR, path_angle=path_angle, solspec=stellar_spec)

### Compare output
# Fortran model plot
fig, axs = plt.subplots(nrows=2,ncols=1,sharex=True,dpi=800)

axs[0].set_title('{:.2e} H2O {:.2e} CO2 {:.2e} CO {:.2e} CH4 \n {:.2e} He {:.2e} H2'.format(
    VMR_H2O,VMR_CO2,VMR_CO, VMR_CH4, VMR_He[0], VMR_H2[0]),fontsize=8)

# plot spectrum from Fortran code
axs[0].scatter(wave,fotran_spec,marker='x',color='k',linewidth=1,s=10,
    label='Fortran')
axs[0].plot(wave,fotran_spec,color='k',linewidth=0.5)

# plot spectrum from Python code
axs[0].scatter(wave,python_spec,marker='.',color='b',linewidth=1,s=10,
   label='Python')
axs[0].plot(wave,python_spec,color='b',linewidth=0.5,linestyle='--')

axs[0].legend(loc='upper left')
axs[0].grid()
axs[0].set_ylabel('Flux ratio')

# difference between fortran and python end to end
diff = (fotran_spec-python_spec)/fotran_spec
axs[1].scatter(wave_grid, diff, marker='.',color='r')
axs[1].set_ylabel('Relative diff')

# Plot config
plt.xlabel(r'wavelength($\mu$m)')
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.grid()
plt.tight_layout()
plt.savefig('{:.3e}H2O_{:.3e}CO2_{:.3e}CO_{:.3e}CH4_{:.3e}He_{:.3e}H2.pdf'.format(
    VMR_H2O,VMR_CO2,VMR_CO, VMR_CH4, VMR_He[0], VMR_H2[0]),dpi=400)
plt.savefig('comparison.pdf',dpi=400)
plt.show()