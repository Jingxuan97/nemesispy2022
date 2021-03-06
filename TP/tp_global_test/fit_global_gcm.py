# -*- coding: utf-8 -*-
# Read GCM data

import os
import numpy as np
import matplotlib.pyplot as plt
import pymultinest
from nemesispy.common.constants import R_SUN, R_JUP_E, AMU, AU, M_JUP, R_JUP, SIGMA_SB
from nemesispy.models.models import Model2
from nemesispy.AAwaitlist.utils import calc_mmw
from nemesispy.data.gcm.process_gcm import (nlon,nlat,xlon,xlat,npv,pv,\
    tmap,h2omap,comap,co2map,ch4map,hemap,h2map,vmrmap,\
    tmap_mod,h2omap_mod,comap_mod,co2map_mod,ch4map_mod,\
    hemap_mod,h2map_mod,vmrmap_mod,phase_grid,\
    kevin_phase_by_wave,kevin_wave_by_phase,\
    pat_phase_by_wave,pat_wave_by_phase,\
    vmrmap_mod_new,tmap_hot)

# Set Pressure range and resolution for fitting
NLAYER = 20
P_range = np.geomspace(20*1e5,1e-3*1e5,NLAYER)

tmap_interped = np.zeros((nlon,nlat,NLAYER))
for ilon in range(nlon):
    for ilat in range(nlat):
        tmap_interped[ilon,ilat,:] = np.interp(P_range,pv[::-1],tmap_mod[ilon,ilat,::-1])