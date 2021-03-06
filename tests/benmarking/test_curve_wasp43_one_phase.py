import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.interpolate
from nemesispy.radtran.forward_model import ForwardModel
from disc_benchmarking_fortran import Nemesis_api
import time

folder_name = 'test_curve_wasp43_one_phase'

### Reference Opacity Data
from helper import lowres_file_paths, cia_file_path

# Read GCM data
from nemesispy.data.gcm.process_gcm import (nlon,nlat,xlon,xlat,npv,pv,\
    tmap,h2omap,comap,co2map,ch4map,hemap,h2map,vmrmap,\
    tmap_mod,h2omap_mod,comap_mod,co2map_mod,ch4map_mod,\
    hemap_mod,h2map_mod,vmrmap_mod,phase_grid,\
    kevin_phase_by_wave,kevin_wave_by_phase,\
    pat_phase_by_wave,pat_wave_by_phase,\
    vmrmap_mod_new,tmap_hot)

### Reference Planet Input
M_plt = 3.8951064000000004e+27 # kg
R_plt = 74065.70 * 1e3 # m

### Reference Spectral Input
# Wavelength grid in micron
wave_grid = np.array([1.1425, 1.1775, 1.2125, 1.2475, 1.2825, 1.3175, 1.3525,
    1.3875,1.4225, 1.4575, 1.4925, 1.5275, 1.5625, 1.5975, 1.6325, 3.6   ,
    4.5   ])
# Stellar spectrum
wasp43_spec = np.array([3.341320e+25, 3.215455e+25, 3.101460e+25, 2.987110e+25,
    2.843440e+25, 2.738320e+25, 2.679875e+25, 2.598525e+25,2.505735e+25,
    2.452230e+25, 2.391140e+25, 2.345905e+25,2.283720e+25, 2.203690e+25,
    2.136015e+25, 1.234010e+24, 4.422200e+23])
# Orbital phase
phase_grid = np.array([ 22.5,  45. ,  67.5,  90. , 112.5, 135. , 157.5, 180. ,
    202.5, 225. , 247.5, 270. , 292.5, 315. , 337.5])
nwave = len(wave_grid)
nphase = len(phase_grid)

# Gas Volume Mixing Ratio, constant with height
gas_id = np.array([  1, 2,  5,  6, 40, 39])
iso_id = np.array([0, 0, 0, 0, 0, 0])
H2_ratio = 0.864
nmu = 5
NMODEL = 88
NLAYER = NMODEL

### Set up Python forward model
FM_py = ForwardModel()
FM_py.set_planet_model(M_plt=M_plt, R_plt=R_plt, gas_id_list=gas_id,
    iso_id_list=iso_id, NLAYER=NLAYER)
FM_py.set_opacity_data(kta_file_paths=lowres_file_paths,
    cia_file_path=cia_file_path)

phasenumber = 5
phase = phase_grid[phasenumber]
P_model = np.geomspace(20*1e5,1e-3,NLAYER)
one_phase =  FM_py.calc_disc_spectrum(phase=phase, nmu=nmu, P_model = P_model,
    global_model_P_grid=pv,
    global_T_model=tmap_mod, global_VMR_model=vmrmap_mod,
    mod_lon=xlon,
    mod_lat=xlat,
    solspec=wasp43_spec)

## Figure
fig, axs = plt.subplots(nrows=2,ncols=1,sharex=True,
    dpi=100)
axs[0].set_title('phase = {}'.format(phase))
axs[0].plot(wave_grid,one_phase,color='b',label='Python')
axs[0].scatter(wave_grid,kevin_phase_by_wave[phasenumber,:,0],color='r',marker='+',label='Data')
axs[0].plot(wave_grid,pat_phase_by_wave[phasenumber,:],color ='k',label='Fortran')
axs[0].legend()
axs[0].grid()

diff = (one_phase - pat_phase_by_wave[phasenumber,:])/one_phase
axs[1].scatter(wave_grid,diff,marker='.',color='b')
axs[1].grid()
print(diff)

plt.show()
# input()
plt.close()



# ### Set up figure
# fig, axs = plt.subplots(nrows=4,ncols=2,sharex='all',sharey='col',
#     figsize=[8,10],dpi=600)
# # add a big axis, hide frame
# fig.add_subplot(111,frameon=False)
# # hide tick and tick label of the big axis
# plt.tick_params(labelcolor='none',which='both',
#     top=False,bottom=False,left=False,right=False)
# plt.xlabel(r'Wavelength ($\mu$m)')

# for index,ilon in enumerate(ilon_list):

#     H = np.linspace(0,1e6,NMODEL)
#     P = pv
#     T = tmap[ilon,ilat,:]
#     VMR = vmrmap[ilon,ilat,:,:]

#     ## Run forward models
#     python_disc_spec = FM_py.calc_disc_spectrum_uniform(nmu=nmu,
#         P_model=P, T_model=T, VMR_model=VMR, solspec=wasp43_spec)

#     FM_fo.write_files(NRING=nmu, H_model=H, P_model=P, T_model=T,
#         VMR_model=VMR)
#     FM_fo.run_forward_model()
#     wave, yerr, fortran_disc_spec = FM_fo.read_output()
#     F_delH, F_totam, F_pres, F_temp, F_scaling = FM_fo.read_drv_file()
#     H_prf, P_prf, T_prf = FM_fo.read_prf_file()

#     ## Upper panel
#     # Fortran plot
#     axs[index,0].plot(wave_grid,fortran_disc_spec,color='k',linewidth=0.5,linestyle='-',
#         marker='x',markersize=2,label='Fortran')

#     # Python model plot
#     axs[index,0].plot(wave_grid,python_disc_spec,color='b',linewidth=0.5,linestyle='--',
#         marker='x',markersize=2,label='Python')

#     # Mark the path angle
#     axs[index,0].text(1.3,2.5e-3,"lon={}".format(xlon[ilon]))

#     ## Upper panel format
#     axs[index,0].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
#     axs[index,0].grid()
#     axs[index,0].set_ylabel('Flux ratio')
#     handles, labels = axs[index,0].get_legend_handles_labels()

#     ## Lower panel
#     diff = (fortran_disc_spec-python_disc_spec)/fortran_disc_spec
#     axs[index,1].plot(wave_grid, diff, color='r', linewidth=0.5,linestyle=':',
#         marker='x',markersize=2,)
#     axs[index,1].set_ylabel('Relative residual')
#     axs[index,1].set_ylim(-1e-2,1e-2)

#     ##??Lower panel format
#     axs[index,1].ticklabel_format(axis="y", style="sci", scilimits=(0,0))
#     axs[index,1].grid()

# # Plot config

# plt.tight_layout()

# fig.legend(handles, labels, loc='upper left', fontsize='x-small')

# plt.savefig('{}.pdf'.format(folder_name))