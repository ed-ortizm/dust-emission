import numpy as np
#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from os import walk # --> dirpath, dirnames, filenames
#1. It needs to load all the models and keep them in memory
    # This means I'll need to have an array with the parameters that identify
    # a model.
# From README.txt
models = [ 'MW3.1_00', 'MW3.1_10', 'MW3.1_20', 'MW3.1_30', 'MW3.1_40', 'MW3.1_50', 'MW3.1_60', 'LMC2_00', 'LMC2_05', 'LMC2_10', 'smc']
q_PAHs  = [ 0.47, 1.12, 1.77, 2.50, 3.19, 3.90, 4.58, 0.75, 1.49, 2.37, 0.10]
umins   = [ 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.70, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 7.00, 8.00, 10.0, 12.0, 15.0, 20.0, 25.0]
umaxs= [1e2,1e3, 1e4, 1e5, 1e6, 1e7]# I added 1e2
# Actually the directory structure is quite different in the website
# ftp://ftp.astro.princeton.edu/draine/dust/irem4/

# Class to read the directory structure with the data

class Data:
    def __inin__(self, path='dust_models'):
        self.path = path
    def txt_files(self):
        # This list store the outputs from walk
        dirpath,dirnames,files = [],[],[]
        # dirpath contains the paths to all the folders that have txt filenames
        # dirnames is a list with only the name of the folders containing the txt filenames
        # files is a list with the names of all the files
        for (a,b,c) in walk('dust_models/'):
            dirpath.append(a)
            dirnames.append(b)
            files.append(c)
        # Doing some make up
        dirpath = dirpath[1:]
        dirnames = dirnames[0]
        files.remove([])



# Class to create a model
class Model:
    def __init__(self, umin, umax, model):
        self.umin = umin
        self.umax = umax
        self.model = model
        self.q_PAH = q_PAH
        self.gamma = gamma
    # Returning the models
#    def model(self):
#        return self.model
