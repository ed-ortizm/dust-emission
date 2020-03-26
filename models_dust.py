import numpy as np

#1. It needs to load all the models and keep them in memory
    # This means I'll need to have an array with the parameters that identify
    # a model.
# From README.txt
models = [ 'MW3.1_00', 'MW3.1_10', 'MW3.1_20', 'MW3.1_30', 'MW3.1_40', 'MW3.1_50', 'MW3.1_60', 'LMC2_00', 'LMC2_05', 'LMC2_10', 'smc']
q_PAH  = [ 0.47, 1.12, 1.77, 2.50, 3.19, 3.90, 4.58, 0.75, 1.49, 2.37, 0.10]
umin   = [ 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.70, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 7.00, 8.00, 10.0, 12.0, 15.0, 20.0, 25.0]
umax= [1e2,1e3, 1e4, 1e5, 1e6, 1e7]# I added 1e2
