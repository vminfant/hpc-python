#!/usr/bin/env python3

import numpy as np

arr = np.arange(0,np.pi/2,0.1)
dfi = (np.sin(arr)[2:] - np.sin(arr)[:-2])/(2.0*0.1)
f_ref = np.cos(arr[1:-1])
