#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Mix ktables of different gases."""
import numpy as np
from numba import jit
from nemesispy.data.constants import C_LIGHT, K_B, PLANCK

@jit(nopython=True)
def interp_k(P_grid, T_grid, P_layer, T_layer, k_gas_w_g_p_t):
    """
    Adapted from chimera https://github.com/mrline/CHIMERA.
    Interpolates the k-tables to input atmospheric P & T for each wavenumber and
    g-ordinate for each gas with a standard bi-linear interpolation scheme.

    Parameters
    ----------
    P_grid : ndarray
        Pressure grid on which the k-coeffs are pre-computed.
    T_grid : ndarray
        Temperature grid on which the k-coeffs are pre-computed.
    P_layer : ndarray
        Atmospheric pressure grid.
    T_layer : ndarray
        Atmospheric temperature grid.
    k_gas_w_g_p_t : ndarray
        k-coefficient array, size = ngas x nwavenumber x ng x npress x ntemp

    Returns
    -------
    k_gas_w_g_l : ndarray
        The interpolated-to-atmosphere k-coefficients.
        Has dimension: Ngas x Nwavenumber x Ng x Nlayer.
    Notes
    -----
    Units: bar for pressure and K for temperature.
    Code breaks if P_layer/T_layer is out of the range of P_grid/T_grid.
    Mainly need to worry about max(T_layer)>max(T_grid).
    """
    Ngas, Nwave, Ng, Npress, Ntemp = k_gas_w_g_p_t.shape
    Nlayer = len(P_layer)
    k_gas_w_g_l = np.zeros((Ngas,Nwave,Ng,Nlayer))
    for ilayer in range(Nlayer): # loop through layers
        P = P_layer[ilayer]
        T = T_layer[ilayer]
        # Workaround when max atmosphere T is out of range of k table grid
        if T > T_grid[-1]:
            T = T_grid[-1]-1
        P_index_hi = np.where(P_grid >= P)[0][0]
        P_index_low = np.where(P_grid < P)[0][-1]
        T_index_hi = np.where(T_grid >= T)[0][0]
        T_index_low = np.where(T_grid < T)[0][-1]
        P_hi = P_grid[P_index_hi]
        P_low = P_grid[P_index_low]
        T_hi = T_grid[T_index_hi]
        T_low = T_grid[T_index_low]
        for igas in range(Ngas): # looping through gases
            for iwave in range(Nwave): # looping through wavenumber
                for ig in range(Ng): # looping through g-ord
                    arr = k_gas_w_g_p_t[igas,iwave,ig,:,:]
                    Q11 = arr[P_index_low,T_index_low]
                    Q12 = arr[P_index_hi,T_index_low]
                    Q22 = arr[P_index_hi,T_index_hi]
                    Q21 = arr[P_index_low,T_index_hi]
                    fxy1 = (T_hi-T)/(T_hi-T_low)*Q11+(T-T_low)/(T_hi-T_low)*Q21
                    fxy2 = (T_hi-T)/(T_hi-T_low)*Q12+(T-T_low)/(T_hi-T_low)*Q22
                    fxy = (P_hi-P)/(P_hi-P_low)*fxy1+(P-P_low)/(P_hi-P_low)*fxy2
                    k_gas_w_g_l[igas, iwave, ig, ilayer] = fxy
    return k_gas_w_g_l

@jit(nopython=True)
def k_overlap_two_gas(k_g1, k_g2, q1, q2, del_g):
    """
    This subroutine combines the absorption coefficient distributions of
    two overlapping gases. The overlap is implicitly assumed to be random
    and the k-distributions are assumed to have NG-1 mean values and NG-1
    weights. Correspondingly there are NG ordinates in total.

    Parameters
    ----------
    k_g1(ng) : ndarray
        k-coefficients for gas 1 at a particular wave bin and temperature/pressure.
    k_g2(ng) : ndarray
        k-coefficients for gas 2 at a particular wave bin and temperature/pressure.
    q1 : real
        Volume mixing ratio of gas 1
    q2 : real
        Volume mixing ratio of gas 2
    del_g(ng) :
        Gauss quadrature weights for the g-ordinates, assumed same for both gases.

    Returns
    -------
    k_g_combine(ng) : ndarray
        Combined k-distribution of both gases
    q_combined : real
        Combined Volume mixing ratio of both gases
    """
    ng = len(del_g)  #Number of g-ordinates
    k_g = np.zeros(ng)
    q_combined = q1 + q2

    if ((k_g1[ng-1]<=0.0) and (k_g2[ng-1]<=0.0)):
        # both gases have negligible opacities
        pass
    elif ( (q1<=0.0) and (q2<=0.0) ):
        # both gases have neglibible VMR
        pass
    elif ((k_g1[ng-1]==0.0) or (q1==0.0)):
        # gas 1 is negligible
        k_g[:] = k_g2[:] * q2/(q1+q2)
    elif ((k_g2[ng-1]==0.0) or (q2==0.0)):
        # gas 2 is negligible
        k_g[:] = k_g1[:] * q1/(q1+q2)
    else:
        # need to properly mix both gases
        nloop = ng * ng
        weight = np.zeros(nloop)
        contri = np.zeros(nloop)
        ix = 0
        for i in range(ng):
            for j in range(ng):
                weight[ix] = del_g[i] * del_g[j]
                contri[ix] = (k_g1[i]*q1 + k_g2[j]*q2)/(q1+q2)
                ix = ix + 1

        #getting the cumulative g ordinate
        g_ord = np.zeros(ng+1)
        g_ord[0] = 0.0
        for ig in range(ng):
            g_ord[ig+1] = g_ord[ig] + del_g[ig]

        if g_ord[ng]<1.0:
            g_ord[ng] = 1.0

        #sorting contri array
        isort = np.argsort(contri)
        contrib1 = contri[isort]
        weight1 = weight[isort]

        #creating combined g-ordinate array
        gdist = np.zeros(nloop)
        gdist[0] = weight1[0]
        for i in range(nloop-1):
            ix = i + 1
            gdist[ix] = weight1[ix] + gdist[i]

        ig = 0
        sum1 = 0.0
        for i in range(nloop):

            if( (gdist[i]<g_ord[ig+1]) & (ig<=ng-1) ):
                k_g[ig] = k_g[ig] + contrib1[i] * weight1[i]
                sum1 = sum1 + weight1[i]
            else:
                frac = (g_ord[ig+1]-gdist[i-1])/(gdist[i]-gdist[i-1])
                k_g[ig] = k_g[ig] + frac * contrib1[i] * weight1[i]
                sum1 = sum1 + weight1[i]
                k_g[ig] = k_g[ig] / sum1
                ig = ig + 1
                if(ig<=ng-1):
                    sum1 = (1.-frac)*weight1[i]
                    k_g[ig] = k_g[ig] + (1.-frac) * contrib1[i] * weight1[i]

        if ig==ng-1:
            k_g[ig] = k_g[ig] / sum1

    return k_g, q_combined

@jit(nopython=True)
def k_overlap_multiple_gas(k_gas_g, VMR, g_ord, del_g):
    ngas = k_gas_g.shape[0]
    k_g_combined,VMR_combined = k_gas_g[0,:],VMR[0]
    #mixing in rest of gases inside a loop
    for j in range(1,ngas):
        k_g_combined,VMR_combined\
            = k_overlap_two_gas(k_g_combined,k_gas_g[j,:],VMR_combined,VMR[j],del_g)
    return k_g_combined, VMR_combined

def k_overlap_new(k_gas_w_g_l, del_g, VMR):
    # k_overlap(nwave,ng,del_g,ngas,npoints,k_gas,f)
    """
    This subroutine combines the absorption coefficient distributions of
    several overlapping gases. The overlap is implicitly assumed to be random
    and the k-distributions are assumed to have NG-1 mean values and NG-1
    weights. Correspondingly there are NG ordinates in total.

    Parameters
    ----------
    k_gas_w_g_l : ndarray

        INPUTS :

            nwave :: Number of wavelengths
            ng :: Number of g-ordinates
            del_g :: Intervals of g-ordinates
            ngas :: Number of gases to combine
            npoints :: Number of p-T points over to run the overlapping routine
            k_gas(nwave,ng,ngas,npoints) :: K-distributions of the different gases
            f(ngas,npoints) :: fraction of the different gases at each of the p-T points


        OPTIONAL INPUTS: None

        OUTPUTS :

            k(nwave,ng,npoints) :: Combined k-distribution

        CALLING SEQUENCE:

            k = k_overlap(nwave,ng,del_g,ngas,npoints,k_gas,f)

        MODIFICATION HISTORY : Juan Alday (25/09/2019)

    """
    Ngas, Nwave, Ng, Nlayer = k_gas_w_g_l.shape
    k_wave_g_l = np.zeros((Nwave, Ng, Nlayer))

    if Ngas <= 1: # only one active gas
        k_wave_g_l[:,:,:] = k_gas_w_g_l[0,:,:,:]
    else:
        for ilayer in range(Nlayer): # each atmopsheric layer

            for igas in range(Ngas):



                if igas==0:

                    # k_gas1_w_g = np.zeros((Nwave, Ngas))
                    # k_gas2_w_g = np.zeros((Nwave, Ngas))

                    k_gas1_w_g = k_gas_w_g_l[igas,:,:,ilayer]
                    k_gas2_w_g = k_gas_w_g_l[igas+1,:,:,ilayer]
                    vmr_gas1 = VMR[ilayer,igas]
                    vmr_gas2 = VMR[ilayer,igas+1]
                    k_combined = np.zeros((Nwave,Ng))

                else:
                    k_gas1_w_g = k_combined
                    k_gas2_w_g = k_gas_w_g_l[igas+1,:,:,ilayer]












def k_overlap(k_gas_w_g_l):
    # k_overlap(nwave,ng,del_g,ngas,npoints,k_gas,f)
    """
    This subroutine combines the absorption coefficient distributions of
    several overlapping gases. The overlap is implicitly assumed to be random
    and the k-distributions are assumed to have NG-1 mean values and NG-1
    weights. Correspondingly there are NG ordinates in total.

    Parameters
    ----------
    k_gas_w_g_l : ndarray

        INPUTS :

            nwave :: Number of wavelengths
            ng :: Number of g-ordinates
            del_g :: Intervals of g-ordinates
            ngas :: Number of gases to combine
            npoints :: Number of p-T points over to run the overlapping routine
            k_gas(nwave,ng,ngas,npoints) :: K-distributions of the different gases
            f(ngas,npoints) :: fraction of the different gases at each of the p-T points


        OPTIONAL INPUTS: None

        OUTPUTS :

            k(nwave,ng,npoints) :: Combined k-distribution

        CALLING SEQUENCE:

            k = k_overlap(nwave,ng,del_g,ngas,npoints,k_gas,f)

        MODIFICATION HISTORY : Juan Alday (25/09/2019)

    """
    Ngas, Nwave, Ng, Nlayer =
    k_wave_g_l = np.zeros((Nwave, Ng, Nlayer))
    k = np.zeros((nwave,ng,npoints))

    if ngas<=1:  #There are not enough gases to combine
        k[:,:,:] = k_gas[:,:,:,0]
    else:

        for ip in range(npoints): #running for each p-T case

            for igas in range(ngas-1):

                #getting first and second gases to combine
                if igas==0:
                    k_gas1 = np.zeros((nwave,ng))
                    k_gas2 = np.zeros((nwave,ng))
                    k_gas1[:,:] = k_gas[:,:,ip,igas]
                    k_gas2[:,:] = k_gas[:,:,ip,igas+1]
                    f1 = f[igas,ip]
                    f2 = f[igas+1,ip]

                    k_combined = np.zeros((nwave,ng))
                else:
                    #k_gas1 = np.zeros((nwave,ng))
                    #k_gas2 = np.zeros((nwave,ng))
                    k_gas1[:,:] = k_combined[:,:]
                    k_gas2[:,:] = k_gas[:,:,ip,igas+1]
                    f1 = f_combined
                    f2 = f[igas+1,ip]

                    k_combined = np.zeros((nwave,ng))

                for iwave in range(nwave):

                    k_g_combined, f_combined = k_overlap_two_gas(k_gas1[iwave,:], k_gas2[iwave,:], f1, f2, del_g)
                    k_combined[iwave,:] = k_g_combined[:]

            k[:,:,ip] = k_combined[:,:]

    return k