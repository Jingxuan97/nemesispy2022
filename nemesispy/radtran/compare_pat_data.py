# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Phase curve simulation from Vivien's GCM model

# NPHASE x NWAVE
pat_phase_by_wave = np.array([[[ 6.000e-05,  6.600e-05],
        [ 5.500e-05,  6.100e-05],
        [ 6.600e-05,  5.800e-05],
        [ 8.600e-05,  5.600e-05],
        [ 5.300e-05,  5.700e-05],
        [ 9.000e-05,  5.300e-05],
        [ 2.000e-06,  5.500e-05],
        [ 2.900e-05,  5.200e-05],
        [ 3.500e-05,  5.600e-05],
        [-3.000e-06,  5.600e-05],
        [ 2.400e-05,  5.600e-05],
        [-3.000e-06,  5.500e-05],
        [ 2.200e-05,  5.800e-05],
        [ 4.800e-05,  5.800e-05],
        [ 8.700e-05,  6.300e-05],
        [-1.300e-05,  1.030e-04],
        [ 9.500e-05,  1.330e-04]],

       [[ 1.030e-04,  6.700e-05],
        [ 1.050e-04,  6.100e-05],
        [ 1.250e-04,  5.900e-05],
        [ 1.540e-04,  5.600e-05],
        [ 9.200e-05,  5.700e-05],
        [ 1.440e-04,  5.300e-05],
        [ 1.900e-05,  5.500e-05],
        [ 7.400e-05,  5.200e-05],
        [ 7.100e-05,  5.600e-05],
        [ 3.300e-05,  5.600e-05],
        [ 7.400e-05,  5.600e-05],
        [ 5.000e-05,  5.500e-05],
        [ 9.100e-05,  5.800e-05],
        [ 1.160e-04,  5.800e-05],
        [ 1.670e-04,  6.300e-05],
        [ 2.350e-04,  1.050e-04],
        [ 5.240e-04,  1.330e-04]],

       [[ 1.610e-04,  7.100e-05],
        [ 1.760e-04,  6.500e-05],
        [ 2.010e-04,  6.200e-05],
        [ 2.420e-04,  6.000e-05],
        [ 1.580e-04,  6.100e-05],
        [ 2.190e-04,  5.700e-05],
        [ 6.000e-05,  5.800e-05],
        [ 1.320e-04,  5.500e-05],
        [ 1.240e-04,  6.000e-05],
        [ 9.500e-05,  5.900e-05],
        [ 1.490e-04,  5.900e-05],
        [ 1.290e-04,  5.800e-05],
        [ 1.950e-04,  6.200e-05],
        [ 2.180e-04,  6.100e-05],
        [ 2.830e-04,  6.700e-05],
        [ 7.350e-04,  1.030e-04],
        [ 1.302e-03,  1.360e-04]],

       [[ 2.240e-04,  6.300e-05],
        [ 2.530e-04,  5.800e-05],
        [ 2.780e-04,  5.500e-05],
        [ 3.300e-04,  5.300e-05],
        [ 2.350e-04,  5.400e-05],
        [ 2.980e-04,  5.000e-05],
        [ 1.170e-04,  5.200e-05],
        [ 1.920e-04,  4.800e-05],
        [ 1.810e-04,  5.300e-05],
        [ 1.690e-04,  5.300e-05],
        [ 2.330e-04,  5.200e-05],
        [ 2.210e-04,  5.200e-05],
        [ 3.090e-04,  5.500e-05],
        [ 3.310e-04,  5.400e-05],
        [ 4.130e-04,  6.000e-05],
        [ 1.458e-03,  1.030e-04],
        [ 2.242e-03,  1.340e-04]],

       [[ 2.830e-04,  6.900e-05],
        [ 3.260e-04,  6.400e-05],
        [ 3.470e-04,  6.100e-05],
        [ 4.070e-04,  5.900e-05],
        [ 3.140e-04,  5.900e-05],
        [ 3.730e-04,  5.600e-05],
        [ 1.830e-04,  5.700e-05],
        [ 2.470e-04,  5.400e-05],
        [ 2.360e-04,  5.900e-05],
        [ 2.460e-04,  5.800e-05],
        [ 3.150e-04,  5.800e-05],
        [ 3.110e-04,  5.700e-05],
        [ 4.220e-04,  6.100e-05],
        [ 4.430e-04,  6.000e-05],
        [ 5.390e-04,  6.600e-05],
        [ 2.245e-03,  1.000e-04],
        [ 3.145e-03,  1.190e-04]],

       [[ 3.290e-04,  6.600e-05],
        [ 3.830e-04,  6.100e-05],
        [ 3.960e-04,  5.800e-05],
        [ 4.640e-04,  5.600e-05],
        [ 3.840e-04,  5.700e-05],
        [ 4.330e-04,  5.300e-05],
        [ 2.490e-04,  5.500e-05],
        [ 2.880e-04,  5.100e-05],
        [ 2.810e-04,  5.600e-05],
        [ 3.150e-04,  5.500e-05],
        [ 3.830e-04,  5.500e-05],
        [ 3.880e-04,  5.500e-05],
        [ 5.150e-04,  5.800e-05],
        [ 5.360e-04,  5.700e-05],
        [ 6.440e-04,  6.300e-05],
        [ 2.909e-03,  7.900e-05],
        [ 3.768e-03,  1.030e-04]],

       [[ 3.550e-04,  5.900e-05],
        [ 4.170e-04,  5.300e-05],
        [ 4.190e-04,  5.200e-05],
        [ 4.910e-04,  4.900e-05],
        [ 4.330e-04,  5.000e-05],
        [ 4.670e-04,  4.700e-05],
        [ 3.030e-04,  4.800e-05],
        [ 3.090e-04,  4.400e-05],
        [ 3.090e-04,  4.900e-05],
        [ 3.640e-04,  4.900e-05],
        [ 4.260e-04,  4.800e-05],
        [ 4.390e-04,  4.800e-05],
        [ 5.750e-04,  5.100e-05],
        [ 5.950e-04,  5.100e-05],
        [ 7.080e-04,  5.600e-05],
        [ 3.281e-03,  7.700e-05],
        [ 4.000e-03,  1.030e-04]],

       [[ 3.670e-04,  4.500e-05],
        [ 4.310e-04,  3.900e-05],
        [ 4.140e-04,  3.800e-05],
        [ 4.820e-04,  3.600e-05],
        [ 4.600e-04,  3.700e-05],
        [ 4.730e-04,  3.300e-05],
        [ 3.530e-04,  3.400e-05],
        [ 3.130e-04,  3.000e-05],
        [ 3.200e-04,  3.600e-05],
        [ 3.940e-04,  3.600e-05],
        [ 4.390e-04,  3.300e-05],
        [ 4.580e-04,  3.500e-05],
        [ 5.950e-04,  3.600e-05],
        [ 6.140e-04,  3.700e-05],
        [ 7.320e-04,  4.200e-05],
        [ 3.231e-03,  6.000e-05],
        [ 3.827e-03,  8.400e-05]],

       [[ 3.350e-04,  6.100e-05],
        [ 3.990e-04,  5.500e-05],
        [ 3.750e-04,  5.300e-05],
        [ 4.410e-04,  5.100e-05],
        [ 4.450e-04,  5.200e-05],
        [ 4.440e-04,  4.800e-05],
        [ 3.490e-04,  5.000e-05],
        [ 2.800e-04,  4.600e-05],
        [ 2.980e-04,  5.100e-05],
        [ 3.790e-04,  5.100e-05],
        [ 4.200e-04,  5.000e-05],
        [ 4.370e-04,  5.000e-05],
        [ 5.630e-04,  5.200e-05],
        [ 5.830e-04,  5.200e-05],
        [ 6.910e-04,  5.800e-05],
        [ 2.881e-03,  8.000e-05],
        [ 3.389e-03,  1.030e-04]],

       [[ 2.930e-04,  6.500e-05],
        [ 3.490e-04,  5.900e-05],
        [ 3.160e-04,  5.700e-05],
        [ 3.730e-04,  5.500e-05],
        [ 4.050e-04,  5.500e-05],
        [ 3.910e-04,  5.200e-05],
        [ 3.350e-04,  5.300e-05],
        [ 2.360e-04,  5.000e-05],
        [ 2.620e-04,  5.500e-05],
        [ 3.430e-04,  5.400e-05],
        [ 3.700e-04,  5.400e-05],
        [ 3.840e-04,  5.300e-05],
        [ 4.930e-04,  5.600e-05],
        [ 5.140e-04,  5.600e-05],
        [ 6.100e-04,  6.100e-05],
        [ 2.285e-03,  1.210e-04],
        [ 2.799e-03,  1.090e-04]],

       [[ 2.370e-04,  7.100e-05],
        [ 2.810e-04,  6.500e-05],
        [ 2.420e-04,  6.300e-05],
        [ 2.890e-04,  6.100e-05],
        [ 3.420e-04,  6.100e-05],
        [ 3.170e-04,  5.700e-05],
        [ 2.950e-04,  5.900e-05],
        [ 1.790e-04,  5.600e-05],
        [ 2.110e-04,  6.000e-05],
        [ 2.830e-04,  5.900e-05],
        [ 2.980e-04,  6.000e-05],
        [ 3.070e-04,  5.900e-05],
        [ 3.930e-04,  6.200e-05],
        [ 4.150e-04,  6.200e-05],
        [ 4.970e-04,  6.700e-05],
        [ 1.625e-03,  1.030e-04],
        [ 2.204e-03,  1.330e-04]],

       [[ 1.740e-04,  6.600e-05],
        [ 2.040e-04,  6.100e-05],
        [ 1.640e-04,  5.800e-05],
        [ 2.000e-04,  5.600e-05],
        [ 2.660e-04,  5.700e-05],
        [ 2.380e-04,  5.300e-05],
        [ 2.370e-04,  5.500e-05],
        [ 1.190e-04,  5.100e-05],
        [ 1.540e-04,  5.600e-05],
        [ 2.090e-04,  5.500e-05],
        [ 2.140e-04,  5.500e-05],
        [ 2.150e-04,  5.500e-05],
        [ 2.780e-04,  5.800e-05],
        [ 3.010e-04,  5.700e-05],
        [ 3.680e-04,  6.300e-05],
        [ 1.054e-03,  1.030e-04],
        [ 1.640e-03,  1.340e-04]],

       [[ 1.150e-04,  6.800e-05],
        [ 1.310e-04,  6.300e-05],
        [ 9.600e-05,  6.000e-05],
        [ 1.210e-04,  5.800e-05],
        [ 1.860e-04,  5.800e-05],
        [ 1.620e-04,  5.500e-05],
        [ 1.710e-04,  5.600e-05],
        [ 6.400e-05,  5.300e-05],
        [ 9.900e-05,  5.700e-05],
        [ 1.320e-04,  5.700e-05],
        [ 1.310e-04,  5.700e-05],
        [ 1.240e-04,  5.600e-05],
        [ 1.650e-04,  5.900e-05],
        [ 1.890e-04,  5.900e-05],
        [ 2.420e-04,  6.400e-05],
        [ 6.170e-04,  1.030e-04],
        [ 1.126e-03,  1.340e-04]],

       [[ 6.700e-05,  6.300e-05],
        [ 7.100e-05,  5.700e-05],
        [ 4.500e-05,  5.500e-05],
        [ 6.300e-05,  5.200e-05],
        [ 1.140e-04,  5.300e-05],
        [ 1.000e-04,  5.000e-05],
        [ 1.030e-04,  5.100e-05],
        [ 2.200e-05,  4.800e-05],
        [ 5.200e-05,  5.300e-05],
        [ 6.100e-05,  5.200e-05],
        [ 6.100e-05,  5.200e-05],
        [ 4.500e-05,  5.100e-05],
        [ 6.800e-05,  5.400e-05],
        [ 9.400e-05,  5.400e-05],
        [ 1.350e-04,  5.900e-05],
        [ 2.990e-04,  1.030e-04],
        [ 6.450e-04,  1.330e-04]],

       [[ 4.100e-05,  7.000e-05],
        [ 3.600e-05,  6.400e-05],
        [ 2.200e-05,  6.200e-05],
        [ 3.700e-05,  5.900e-05],
        [ 6.600e-05,  6.000e-05],
        [ 6.700e-05,  5.600e-05],
        [ 4.700e-05,  5.800e-05],
        [ 1.000e-06,  5.500e-05],
        [ 2.500e-05,  5.900e-05],
        [ 1.200e-05,  5.800e-05],
        [ 1.700e-05,  5.900e-05],
        [-5.000e-06,  5.800e-05],
        [ 9.000e-06,  6.100e-05],
        [ 3.600e-05,  6.100e-05],
        [ 7.000e-05,  6.600e-05],
        [ 8.300e-05,  1.030e-04],
        [ 2.470e-04,  1.330e-04]]])

# NWAVE x NPHASE
pat_wave_by_phase = np.array([[[ 6.000e-05,  6.600e-05],
        [ 1.030e-04,  6.700e-05],
        [ 1.610e-04,  7.100e-05],
        [ 2.240e-04,  6.300e-05],
        [ 2.830e-04,  6.900e-05],
        [ 3.290e-04,  6.600e-05],
        [ 3.550e-04,  5.900e-05],
        [ 3.670e-04,  4.500e-05],
        [ 3.350e-04,  6.100e-05],
        [ 2.930e-04,  6.500e-05],
        [ 2.370e-04,  7.100e-05],
        [ 1.740e-04,  6.600e-05],
        [ 1.150e-04,  6.800e-05],
        [ 6.700e-05,  6.300e-05],
        [ 4.100e-05,  7.000e-05]],

       [[ 5.500e-05,  6.100e-05],
        [ 1.050e-04,  6.100e-05],
        [ 1.760e-04,  6.500e-05],
        [ 2.530e-04,  5.800e-05],
        [ 3.260e-04,  6.400e-05],
        [ 3.830e-04,  6.100e-05],
        [ 4.170e-04,  5.300e-05],
        [ 4.310e-04,  3.900e-05],
        [ 3.990e-04,  5.500e-05],
        [ 3.490e-04,  5.900e-05],
        [ 2.810e-04,  6.500e-05],
        [ 2.040e-04,  6.100e-05],
        [ 1.310e-04,  6.300e-05],
        [ 7.100e-05,  5.700e-05],
        [ 3.600e-05,  6.400e-05]],

       [[ 6.600e-05,  5.800e-05],
        [ 1.250e-04,  5.900e-05],
        [ 2.010e-04,  6.200e-05],
        [ 2.780e-04,  5.500e-05],
        [ 3.470e-04,  6.100e-05],
        [ 3.960e-04,  5.800e-05],
        [ 4.190e-04,  5.200e-05],
        [ 4.140e-04,  3.800e-05],
        [ 3.750e-04,  5.300e-05],
        [ 3.160e-04,  5.700e-05],
        [ 2.420e-04,  6.300e-05],
        [ 1.640e-04,  5.800e-05],
        [ 9.600e-05,  6.000e-05],
        [ 4.500e-05,  5.500e-05],
        [ 2.200e-05,  6.200e-05]],

       [[ 8.600e-05,  5.600e-05],
        [ 1.540e-04,  5.600e-05],
        [ 2.420e-04,  6.000e-05],
        [ 3.300e-04,  5.300e-05],
        [ 4.070e-04,  5.900e-05],
        [ 4.640e-04,  5.600e-05],
        [ 4.910e-04,  4.900e-05],
        [ 4.820e-04,  3.600e-05],
        [ 4.410e-04,  5.100e-05],
        [ 3.730e-04,  5.500e-05],
        [ 2.890e-04,  6.100e-05],
        [ 2.000e-04,  5.600e-05],
        [ 1.210e-04,  5.800e-05],
        [ 6.300e-05,  5.200e-05],
        [ 3.700e-05,  5.900e-05]],

       [[ 5.300e-05,  5.700e-05],
        [ 9.200e-05,  5.700e-05],
        [ 1.580e-04,  6.100e-05],
        [ 2.350e-04,  5.400e-05],
        [ 3.140e-04,  5.900e-05],
        [ 3.840e-04,  5.700e-05],
        [ 4.330e-04,  5.000e-05],
        [ 4.600e-04,  3.700e-05],
        [ 4.450e-04,  5.200e-05],
        [ 4.050e-04,  5.500e-05],
        [ 3.420e-04,  6.100e-05],
        [ 2.660e-04,  5.700e-05],
        [ 1.860e-04,  5.800e-05],
        [ 1.140e-04,  5.300e-05],
        [ 6.600e-05,  6.000e-05]],

       [[ 9.000e-05,  5.300e-05],
        [ 1.440e-04,  5.300e-05],
        [ 2.190e-04,  5.700e-05],
        [ 2.980e-04,  5.000e-05],
        [ 3.730e-04,  5.600e-05],
        [ 4.330e-04,  5.300e-05],
        [ 4.670e-04,  4.700e-05],
        [ 4.730e-04,  3.300e-05],
        [ 4.440e-04,  4.800e-05],
        [ 3.910e-04,  5.200e-05],
        [ 3.170e-04,  5.700e-05],
        [ 2.380e-04,  5.300e-05],
        [ 1.620e-04,  5.500e-05],
        [ 1.000e-04,  5.000e-05],
        [ 6.700e-05,  5.600e-05]],

       [[ 2.000e-06,  5.500e-05],
        [ 1.900e-05,  5.500e-05],
        [ 6.000e-05,  5.800e-05],
        [ 1.170e-04,  5.200e-05],
        [ 1.830e-04,  5.700e-05],
        [ 2.490e-04,  5.500e-05],
        [ 3.030e-04,  4.800e-05],
        [ 3.530e-04,  3.400e-05],
        [ 3.490e-04,  5.000e-05],
        [ 3.350e-04,  5.300e-05],
        [ 2.950e-04,  5.900e-05],
        [ 2.370e-04,  5.500e-05],
        [ 1.710e-04,  5.600e-05],
        [ 1.030e-04,  5.100e-05],
        [ 4.700e-05,  5.800e-05]],

       [[ 2.900e-05,  5.200e-05],
        [ 7.400e-05,  5.200e-05],
        [ 1.320e-04,  5.500e-05],
        [ 1.920e-04,  4.800e-05],
        [ 2.470e-04,  5.400e-05],
        [ 2.880e-04,  5.100e-05],
        [ 3.090e-04,  4.400e-05],
        [ 3.130e-04,  3.000e-05],
        [ 2.800e-04,  4.600e-05],
        [ 2.360e-04,  5.000e-05],
        [ 1.790e-04,  5.600e-05],
        [ 1.190e-04,  5.100e-05],
        [ 6.400e-05,  5.300e-05],
        [ 2.200e-05,  4.800e-05],
        [ 1.000e-06,  5.500e-05]],

       [[ 3.500e-05,  5.600e-05],
        [ 7.100e-05,  5.600e-05],
        [ 1.240e-04,  6.000e-05],
        [ 1.810e-04,  5.300e-05],
        [ 2.360e-04,  5.900e-05],
        [ 2.810e-04,  5.600e-05],
        [ 3.090e-04,  4.900e-05],
        [ 3.200e-04,  3.600e-05],
        [ 2.980e-04,  5.100e-05],
        [ 2.620e-04,  5.500e-05],
        [ 2.110e-04,  6.000e-05],
        [ 1.540e-04,  5.600e-05],
        [ 9.900e-05,  5.700e-05],
        [ 5.200e-05,  5.300e-05],
        [ 2.500e-05,  5.900e-05]],

       [[-3.000e-06,  5.600e-05],
        [ 3.300e-05,  5.600e-05],
        [ 9.500e-05,  5.900e-05],
        [ 1.690e-04,  5.300e-05],
        [ 2.460e-04,  5.800e-05],
        [ 3.150e-04,  5.500e-05],
        [ 3.640e-04,  4.900e-05],
        [ 3.940e-04,  3.600e-05],
        [ 3.790e-04,  5.100e-05],
        [ 3.430e-04,  5.400e-05],
        [ 2.830e-04,  5.900e-05],
        [ 2.090e-04,  5.500e-05],
        [ 1.320e-04,  5.700e-05],
        [ 6.100e-05,  5.200e-05],
        [ 1.200e-05,  5.800e-05]],

       [[ 2.400e-05,  5.600e-05],
        [ 7.400e-05,  5.600e-05],
        [ 1.490e-04,  5.900e-05],
        [ 2.330e-04,  5.200e-05],
        [ 3.150e-04,  5.800e-05],
        [ 3.830e-04,  5.500e-05],
        [ 4.260e-04,  4.800e-05],
        [ 4.390e-04,  3.300e-05],
        [ 4.200e-04,  5.000e-05],
        [ 3.700e-04,  5.400e-05],
        [ 2.980e-04,  6.000e-05],
        [ 2.140e-04,  5.500e-05],
        [ 1.310e-04,  5.700e-05],
        [ 6.100e-05,  5.200e-05],
        [ 1.700e-05,  5.900e-05]],

       [[-3.000e-06,  5.500e-05],
        [ 5.000e-05,  5.500e-05],
        [ 1.290e-04,  5.800e-05],
        [ 2.210e-04,  5.200e-05],
        [ 3.110e-04,  5.700e-05],
        [ 3.880e-04,  5.500e-05],
        [ 4.390e-04,  4.800e-05],
        [ 4.580e-04,  3.500e-05],
        [ 4.370e-04,  5.000e-05],
        [ 3.840e-04,  5.300e-05],
        [ 3.070e-04,  5.900e-05],
        [ 2.150e-04,  5.500e-05],
        [ 1.240e-04,  5.600e-05],
        [ 4.500e-05,  5.100e-05],
        [-5.000e-06,  5.800e-05]],

       [[ 2.200e-05,  5.800e-05],
        [ 9.100e-05,  5.800e-05],
        [ 1.950e-04,  6.200e-05],
        [ 3.090e-04,  5.500e-05],
        [ 4.220e-04,  6.100e-05],
        [ 5.150e-04,  5.800e-05],
        [ 5.750e-04,  5.100e-05],
        [ 5.950e-04,  3.600e-05],
        [ 5.630e-04,  5.200e-05],
        [ 4.930e-04,  5.600e-05],
        [ 3.930e-04,  6.200e-05],
        [ 2.780e-04,  5.800e-05],
        [ 1.650e-04,  5.900e-05],
        [ 6.800e-05,  5.400e-05],
        [ 9.000e-06,  6.100e-05]],

       [[ 4.800e-05,  5.800e-05],
        [ 1.160e-04,  5.800e-05],
        [ 2.180e-04,  6.100e-05],
        [ 3.310e-04,  5.400e-05],
        [ 4.430e-04,  6.000e-05],
        [ 5.360e-04,  5.700e-05],
        [ 5.950e-04,  5.100e-05],
        [ 6.140e-04,  3.700e-05],
        [ 5.830e-04,  5.200e-05],
        [ 5.140e-04,  5.600e-05],
        [ 4.150e-04,  6.200e-05],
        [ 3.010e-04,  5.700e-05],
        [ 1.890e-04,  5.900e-05],
        [ 9.400e-05,  5.400e-05],
        [ 3.600e-05,  6.100e-05]],

       [[ 8.700e-05,  6.300e-05],
        [ 1.670e-04,  6.300e-05],
        [ 2.830e-04,  6.700e-05],
        [ 4.130e-04,  6.000e-05],
        [ 5.390e-04,  6.600e-05],
        [ 6.440e-04,  6.300e-05],
        [ 7.080e-04,  5.600e-05],
        [ 7.320e-04,  4.200e-05],
        [ 6.910e-04,  5.800e-05],
        [ 6.100e-04,  6.100e-05],
        [ 4.970e-04,  6.700e-05],
        [ 3.680e-04,  6.300e-05],
        [ 2.420e-04,  6.400e-05],
        [ 1.350e-04,  5.900e-05],
        [ 7.000e-05,  6.600e-05]],

       [[-1.300e-05,  1.030e-04],
        [ 2.350e-04,  1.050e-04],
        [ 7.350e-04,  1.030e-04],
        [ 1.458e-03,  1.030e-04],
        [ 2.245e-03,  1.000e-04],
        [ 2.909e-03,  7.900e-05],
        [ 3.281e-03,  7.700e-05],
        [ 3.231e-03,  6.000e-05],
        [ 2.881e-03,  8.000e-05],
        [ 2.285e-03,  1.210e-04],
        [ 1.625e-03,  1.030e-04],
        [ 1.054e-03,  1.030e-04],
        [ 6.170e-04,  1.030e-04],
        [ 2.990e-04,  1.030e-04],
        [ 8.300e-05,  1.030e-04]],

       [[ 9.500e-05,  1.330e-04],
        [ 5.240e-04,  1.330e-04],
        [ 1.302e-03,  1.360e-04],
        [ 2.242e-03,  1.340e-04],
        [ 3.145e-03,  1.190e-04],
        [ 3.768e-03,  1.030e-04],
        [ 4.000e-03,  1.030e-04],
        [ 3.827e-03,  8.400e-05],
        [ 3.389e-03,  1.030e-04],
        [ 2.799e-03,  1.090e-04],
        [ 2.204e-03,  1.330e-04],
        [ 1.640e-03,  1.340e-04],
        [ 1.126e-03,  1.340e-04],
        [ 6.450e-04,  1.330e-04],
        [ 2.470e-04,  1.330e-04]]])

my_phase_by_wave = np.array([[3.13794596e-04, 3.09622763e-04, 3.83853527e-04, 4.49050191e-04,
        4.95989718e-04, 4.81940931e-04, 2.75498916e-04, 2.78806473e-04,
        2.81366153e-04, 3.18926404e-04, 3.78816859e-04, 4.60090975e-04,
        5.40122293e-04, 6.43779578e-04, 7.17540021e-04, 3.16315470e-03,
        4.45062891e-03],
       [2.60747977e-04, 2.56933610e-04, 3.21259206e-04, 3.78645128e-04,
        4.17691821e-04, 4.04907080e-04, 2.30195412e-04, 2.33097532e-04,
        2.35903853e-04, 2.68297863e-04, 3.19736081e-04, 3.89579405e-04,
        4.58886110e-04, 5.50128604e-04, 6.15438551e-04, 2.86463139e-03,
        4.06667647e-03],
       [1.98327167e-04, 1.92769400e-04, 2.47150322e-04, 2.99610507e-04,
        3.29775166e-04, 3.13423587e-04, 1.73268912e-04, 1.75577904e-04,
        1.78616428e-04, 2.04458638e-04, 2.45273714e-04, 3.01071165e-04,
        3.57471465e-04, 4.35015810e-04, 4.92297696e-04, 2.48761713e-03,
        3.58619995e-03],
       [1.37003732e-04, 1.27769442e-04, 1.72653285e-04, 2.25573849e-04,
        2.50630247e-04, 2.22064360e-04, 1.16190598e-04, 1.17946431e-04,
        1.21156765e-04, 1.40225207e-04, 1.70081534e-04, 2.11348428e-04,
        2.54353792e-04, 3.17357168e-04, 3.66260053e-04, 2.09502694e-03,
        3.08784615e-03],
       [8.23388909e-05, 7.18237270e-05, 1.06307799e-04, 1.58983006e-04,
        1.81715212e-04, 1.40679547e-04, 6.93994063e-05, 7.08468309e-05,
        7.41597865e-05, 8.73866267e-05, 1.07769312e-04, 1.36257236e-04,
        1.67187265e-04, 2.15976134e-04, 2.55583188e-04, 1.76041509e-03,
        2.66489917e-03],
       [4.55247574e-05, 3.72359441e-05, 6.29482850e-05, 1.11633277e-04,
        1.31400593e-04, 8.60814162e-05, 4.10197256e-05, 4.23030151e-05,
        4.54759170e-05, 5.48469720e-05, 6.90581915e-05, 8.91977414e-05,
        1.12107465e-04, 1.50995493e-04, 1.82775697e-04, 1.52846149e-03,
        2.36840835e-03],
       [3.35590129e-05, 2.59040538e-05, 4.93051232e-05, 9.73775396e-05,
        1.15957379e-04, 6.79473420e-05, 3.02902974e-05, 3.13464875e-05,
        3.42516444e-05, 4.20828933e-05, 5.40542097e-05, 7.15719787e-05,
        9.22472745e-05, 1.29064025e-04, 1.59532093e-04, 1.41921077e-03,
        2.21766460e-03],
       [3.56689596e-05, 2.62331572e-05, 5.22604086e-05, 1.04562385e-04,
        1.24901662e-04, 7.12264648e-05, 2.86043698e-05, 2.93703627e-05,
        3.20886807e-05, 3.98020760e-05, 5.19502278e-05, 7.05232601e-05,
        9.28084332e-05, 1.33087545e-04, 1.67506405e-04, 1.39490192e-03,
        2.16844836e-03],
       [3.96678807e-05, 2.87372318e-05, 5.74590737e-05, 1.13464592e-04,
        1.35651298e-04, 7.78719466e-05, 2.97834293e-05, 3.03990624e-05,
        3.31025046e-05, 4.11413503e-05, 5.40372136e-05, 7.42136550e-05,
        9.84527414e-05, 1.42220934e-04, 1.80336923e-04, 1.41379268e-03,
        2.18446900e-03],
       [5.52369458e-05, 4.09617295e-05, 7.59516907e-05, 1.39298082e-04,
        1.65732799e-04, 1.01940334e-04, 3.92816114e-05, 3.98439069e-05,
        4.26986209e-05, 5.22699406e-05, 6.78032147e-05, 9.21874879e-05,
        1.20998551e-04, 1.71954371e-04, 2.17450499e-04, 1.51366306e-03,
        2.30664773e-03],
       [9.28814177e-05, 7.46140055e-05, 1.19573732e-04, 1.90603474e-04,
        2.21981563e-04, 1.57185074e-04, 6.64723562e-05, 6.72108328e-05,
        7.02268742e-05, 8.34476431e-05, 1.04835974e-04, 1.37324196e-04,
        1.74196026e-04, 2.36146226e-04, 2.91292326e-04, 1.73560339e-03,
        2.59142343e-03],
       [1.48417232e-04, 1.30373571e-04, 1.85596296e-04, 2.57837353e-04,
        2.91779766e-04, 2.38400183e-04, 1.12973008e-04, 1.14152189e-04,
        1.17114367e-04, 1.36005955e-04, 1.66403875e-04, 2.10677821e-04,
        2.58503533e-04, 3.33499278e-04, 3.97494662e-04, 2.06641408e-03,
        3.01993175e-03],
       [2.09774105e-04, 1.96045077e-04, 2.59238794e-04, 3.28515462e-04,
        3.66064762e-04, 3.28506624e-04, 1.70874593e-04, 1.72777761e-04,
        1.75576149e-04, 2.01187593e-04, 2.42193713e-04, 2.99887835e-04,
        3.59625295e-04, 4.46638415e-04, 5.16390780e-04, 2.46043054e-03,
        3.53328672e-03],
       [2.69176870e-04, 2.59754783e-04, 3.29841612e-04, 3.98575857e-04,
        4.42405933e-04, 4.15409527e-04, 2.28852393e-04, 2.31554246e-04,
        2.34181553e-04, 2.66335363e-04, 3.17684376e-04, 3.88347894e-04,
        4.59407041e-04, 5.56645140e-04, 6.30256198e-04, 2.84342853e-03,
        4.03248351e-03],
       [3.17343049e-04, 3.10547868e-04, 3.87070083e-04, 4.57695959e-04,
        5.07166980e-04, 4.85841030e-04, 2.74720647e-04, 2.78004311e-04,
        2.80487931e-04, 3.17822349e-04, 3.77424459e-04, 4.58603454e-04,
        5.38941325e-04, 6.44841534e-04, 7.22193129e-04, 3.14841137e-03,
        4.43205905e-03]])

my_wave_by_phase = np.array([[3.13794596e-04, 2.60747977e-04, 1.98327167e-04, 1.37003732e-04,
        8.23388909e-05, 4.55247574e-05, 3.35590129e-05, 3.56689596e-05,
        3.96678807e-05, 5.52369458e-05, 9.28814177e-05, 1.48417232e-04,
        2.09774105e-04, 2.69176870e-04, 3.17343049e-04],
       [3.09622763e-04, 2.56933610e-04, 1.92769400e-04, 1.27769442e-04,
        7.18237270e-05, 3.72359441e-05, 2.59040538e-05, 2.62331572e-05,
        2.87372318e-05, 4.09617295e-05, 7.46140055e-05, 1.30373571e-04,
        1.96045077e-04, 2.59754783e-04, 3.10547868e-04],
       [3.83853527e-04, 3.21259206e-04, 2.47150322e-04, 1.72653285e-04,
        1.06307799e-04, 6.29482850e-05, 4.93051232e-05, 5.22604086e-05,
        5.74590737e-05, 7.59516907e-05, 1.19573732e-04, 1.85596296e-04,
        2.59238794e-04, 3.29841612e-04, 3.87070083e-04],
       [4.49050191e-04, 3.78645128e-04, 2.99610507e-04, 2.25573849e-04,
        1.58983006e-04, 1.11633277e-04, 9.73775396e-05, 1.04562385e-04,
        1.13464592e-04, 1.39298082e-04, 1.90603474e-04, 2.57837353e-04,
        3.28515462e-04, 3.98575857e-04, 4.57695959e-04],
       [4.95989718e-04, 4.17691821e-04, 3.29775166e-04, 2.50630247e-04,
        1.81715212e-04, 1.31400593e-04, 1.15957379e-04, 1.24901662e-04,
        1.35651298e-04, 1.65732799e-04, 2.21981563e-04, 2.91779766e-04,
        3.66064762e-04, 4.42405933e-04, 5.07166980e-04],
       [4.81940931e-04, 4.04907080e-04, 3.13423587e-04, 2.22064360e-04,
        1.40679547e-04, 8.60814162e-05, 6.79473420e-05, 7.12264648e-05,
        7.78719466e-05, 1.01940334e-04, 1.57185074e-04, 2.38400183e-04,
        3.28506624e-04, 4.15409527e-04, 4.85841030e-04],
       [2.75498916e-04, 2.30195412e-04, 1.73268912e-04, 1.16190598e-04,
        6.93994063e-05, 4.10197256e-05, 3.02902974e-05, 2.86043698e-05,
        2.97834293e-05, 3.92816114e-05, 6.64723562e-05, 1.12973008e-04,
        1.70874593e-04, 2.28852393e-04, 2.74720647e-04],
       [2.78806473e-04, 2.33097532e-04, 1.75577904e-04, 1.17946431e-04,
        7.08468309e-05, 4.23030151e-05, 3.13464875e-05, 2.93703627e-05,
        3.03990624e-05, 3.98439069e-05, 6.72108328e-05, 1.14152189e-04,
        1.72777761e-04, 2.31554246e-04, 2.78004311e-04],
       [2.81366153e-04, 2.35903853e-04, 1.78616428e-04, 1.21156765e-04,
        7.41597865e-05, 4.54759170e-05, 3.42516444e-05, 3.20886807e-05,
        3.31025046e-05, 4.26986209e-05, 7.02268742e-05, 1.17114367e-04,
        1.75576149e-04, 2.34181553e-04, 2.80487931e-04],
       [3.18926404e-04, 2.68297863e-04, 2.04458638e-04, 1.40225207e-04,
        8.73866267e-05, 5.48469720e-05, 4.20828933e-05, 3.98020760e-05,
        4.11413503e-05, 5.22699406e-05, 8.34476431e-05, 1.36005955e-04,
        2.01187593e-04, 2.66335363e-04, 3.17822349e-04],
       [3.78816859e-04, 3.19736081e-04, 2.45273714e-04, 1.70081534e-04,
        1.07769312e-04, 6.90581915e-05, 5.40542097e-05, 5.19502278e-05,
        5.40372136e-05, 6.78032147e-05, 1.04835974e-04, 1.66403875e-04,
        2.42193713e-04, 3.17684376e-04, 3.77424459e-04],
       [4.60090975e-04, 3.89579405e-04, 3.01071165e-04, 2.11348428e-04,
        1.36257236e-04, 8.91977414e-05, 7.15719787e-05, 7.05232601e-05,
        7.42136550e-05, 9.21874879e-05, 1.37324196e-04, 2.10677821e-04,
        2.99887835e-04, 3.88347894e-04, 4.58603454e-04],
       [5.40122293e-04, 4.58886110e-04, 3.57471465e-04, 2.54353792e-04,
        1.67187265e-04, 1.12107465e-04, 9.22472745e-05, 9.28084332e-05,
        9.84527414e-05, 1.20998551e-04, 1.74196026e-04, 2.58503533e-04,
        3.59625295e-04, 4.59407041e-04, 5.38941325e-04],
       [6.43779578e-04, 5.50128604e-04, 4.35015810e-04, 3.17357168e-04,
        2.15976134e-04, 1.50995493e-04, 1.29064025e-04, 1.33087545e-04,
        1.42220934e-04, 1.71954371e-04, 2.36146226e-04, 3.33499278e-04,
        4.46638415e-04, 5.56645140e-04, 6.44841534e-04],
       [7.17540021e-04, 6.15438551e-04, 4.92297696e-04, 3.66260053e-04,
        2.55583188e-04, 1.82775697e-04, 1.59532093e-04, 1.67506405e-04,
        1.80336923e-04, 2.17450499e-04, 2.91292326e-04, 3.97494662e-04,
        5.16390780e-04, 6.30256198e-04, 7.22193129e-04],
       [3.16315470e-03, 2.86463139e-03, 2.48761713e-03, 2.09502694e-03,
        1.76041509e-03, 1.52846149e-03, 1.41921077e-03, 1.39490192e-03,
        1.41379268e-03, 1.51366306e-03, 1.73560339e-03, 2.06641408e-03,
        2.46043054e-03, 2.84342853e-03, 3.14841137e-03],
       [4.45062891e-03, 4.06667647e-03, 3.58619995e-03, 3.08784615e-03,
        2.66489917e-03, 2.36840835e-03, 2.21766460e-03, 2.16844836e-03,
        2.18446900e-03, 2.30664773e-03, 2.59142343e-03, 3.01993175e-03,
        3.53328672e-03, 4.03248351e-03, 4.43205905e-03]])

nphase = 15
lat_grid = np.array([ 22.5,  45. ,  67.5,  90. , 112.5, 135. , 157.5, 180. , 202.5,
       225. , 247.5, 270. , 292.5, 315. , 337.5])
phase_grid = (360*np.ones(nphase) - lat_grid)/360*np.ones(nphase)
nwave = 17
wave_grid = np.array([1.1425, 1.1775, 1.2125, 1.2475, 1.2825, 1.3175, 1.3525, 1.3875,
       1.4225, 1.4575, 1.4925, 1.5275, 1.5625, 1.5975, 1.6325, 3.6   ,
       4.5   ])

"""
for iphase,phase in enumerate(phase_grid):
    plt.title(r'Central Lattitude: {}$\degree$'.format(phase)+'\n'
              +r'Phase: {}$\degree$'.format(360-phase))
    plt.plot(wave_grid, pat_phase_by_wave[iphase,:,0])
    plt.tight_layout()
    plt.grid()
"""

# Plot spectrum at each phase
fig, axs = plt.subplots(nrows=5,ncols=3,sharex=True,sharey=True,
                        figsize=[8.25,11.75],dpi=600)
plt.xlim(1,4.6)
plt.ylim(-5e-1,4.5)
# add a big axis, hide frame
fig.add_subplot(111,frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none',which='both',top=False,bottom=False,left=False,right=False)
plt.xlabel(r'Wavelength($\mu$m)')
plt.ylabel('Flux ratio ($10^{-3}$)')
ix = 0
iy = 0
for iphase,phase in enumerate(phase_grid):

    axs[ix,iy].errorbar(wave_grid, pat_phase_by_wave[iphase,:,0]*1e3,
                        yerr=pat_phase_by_wave[iphase,:,1]*1e3,
                        marker='s',ms=0.1,ecolor='r',mfc='k',color='k',
                        linewidth=0.5,label='fortran')
    axs[ix,iy].plot(wave_grid, my_phase_by_wave[iphase,:]*1e3,
                    marker='s',ms=0.1,mfc='b',color='b',
                    linewidth=0.5,label='python')
    axs[ix,iy].legend(loc='lower right',fontsize='small')
    # axs[ix,iy].grid()
    axs[ix,iy].text(1.5,3.5,'phase = {}'.format(phase),fontsize=12)
    iy += 1
    if iy == 3:
        iy = 0
        ix += 1
# plt.show()
plt.savefig('test_spectra.pdf')


# Plot phase curve at each wavelength
fig, axs = plt.subplots(nrows=17,ncols=1,sharex=True,sharey=False,
                        figsize=[5,13],dpi=600)
plt.xlim(0.,1.)
# add a big axis, hide frame
fig.add_subplot(111,frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none',which='both',top=False,bottom=False,left=False,right=False)
plt.xlabel('phase')
plt.ylabel(r'Wavelength($\mu$m)')

for iwave,wave in enumerate(wave_grid):
    axs[iwave].errorbar(phase_grid, pat_wave_by_phase[iwave,:,0]*1e3,
                        yerr=pat_wave_by_phase[iwave,:,1]*1e3,
                        marker='s',ms=0.1,ecolor='r',mfc='k',color='k',linewidth=0.5)
    axs[iwave].plot(phase_grid, my_wave_by_phase[iwave,:]*1e3,
                        marker='s',ms=0.1,mfc='b',color='b',linewidth=0.5)
    # axs[iwave].get_yaxis().set_visible(False)
    axs[iwave].set_yticklabels([])
    wave = np.around(wave,decimals=2)
    axs[iwave].set_ylabel(wave,rotation=0,fontsize=8)
    # axs[iwave].legend()
plt.tight_layout()

plt.savefig('test_phase_curve.pdf')