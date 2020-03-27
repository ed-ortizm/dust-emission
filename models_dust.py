import numpy as np
#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from os import walk # --> dirpath, dirnames, filenames
import matplotlib
import matplotlib.pyplot as plt
#1. It needs to load all the models and keep them in memory
    # This means I'll need to have an array with the parameters that identify
    # a model.
# From README.txt
models = [ 'MW3.1_00', 'MW3.1_10', 'MW3.1_20', 'MW3.1_30', 'MW3.1_40', 'MW3.1_50', 'MW3.1_60', 'LMC2_00', 'LMC2_05', 'LMC2_10', 'smc']
q_PAHs  = [ 0.47, 1.12, 1.77, 2.50, 3.19, 3.90, 4.58, 0.75, 1.49, 2.37, 0.10]
model_q_dic = {models[i]:q_PAHs for i in range(len(models))}
umins   = [ 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.70, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 7.00, 8.00, 10.0, 12.0, 15.0, 20.0, 25.0]
umaxs= [1e2,1e3, 1e4, 1e5, 1e6, 1e7]# I added 1e2
# Actually the directory structure is quite different in the website
# ftp://ftp.astro.princeton.edu/draine/dust/irem4/

# Class to read the directory structure and pass the data to arrays withing a dictionary

class Data:
    def __init__(self, path='dust_models/'):
        self.path = path
    def txt_files(self):
        # This list store the outputs from walk
        dirpath,dirnames,files = [],[],[]
        # dirpath contains the paths to all the folders that have txt filenames
        # dirnames is a list with only the name of the folders containing the txt filenames
        # files is a list with the names of all the files
        # The map is one to one among each element of these lists, ie, element 1 refer to the same Uumin
        for (a,b,c) in walk(self.path):
            dirpath.append(a)
            dirnames.append(b)
            files.append(c)
        # Doing some make up
        dirpath = dirpath[1:]
        dirnames = dirnames[0]
        files.remove([])
        return dirpath, dirnames,files
    def arr_dat(self,file):
        # This method generates a Numpy array for one txt file of data
        f = open(file,'r')
        vals = []
        # Flag variable
        i = 0
        for line in f:
            if ('lambda' in line):
                i = 1
            elif i == 1:
                i = 2
            elif i == 2:
                val = line.split()
                vals.append(val)
        f.close()
        if i == 0:
            return np.zeros(3)
        data = np.array(vals)
        #print(file)
        #print(data)
        data = data.astype(float)
        return data
    def dic_files(self):
        # This method returns a dictionary where the key is the directory path
        # and the values are lists with the files in the corresponding directory.
        dirpath, dirnames,files = self.txt_files()
        all_txts = {dirpath[i]:files[i] for i in range(len(dirpath))}
        return all_txts
    def dic_arr(self):
        dic_arr = {}
        # This method returns a dictioanry containing all the data, arranged
        #similarly as in dic_files
        all_txts = self.dic_files()
        for key,values in all_txts.items():
            for val in values:
                arr = self.arr_dat(key + '/' + val)
                dic_arr[val] = arr
        return dic_arr

d = Data()
dic_arr = d.dic_arr()
for x in dic_arr:
    print(x)
    break

# There are 1542 files
#print(len(dic_arr))
# Class to create a model
class Model:
    def __init__(self, umin, umax, model,gamma,data, model_q_dic = model_q_dic):
        self.umin = umin
        self.umax = umax
        self.model = model
        self.q_PAH = model_q_dic[model]
        if 0 < gamma < 1:
            self.gamma = gamma
        else:
            print("gamma must be a number between 0 and 1")
        #self.file = path + 'U' + umin + '/' + 'U' + umin + '_' + umax + '_' + model + '.txt'
        # For doing computations with gamma
        # --> j_nu = (1-gamma)*j_nu[umin,umin] + gamma*j_nu[umin,umax]
        self.key_min_min = 'U' + umin + '_' + umin + '_' + model + '.txt'
        self.key_min_max = 'U' + umin + '_' + umax + '_' + model + '.txt'
        self.data = data # this is the data loaded in memory by the last class
    # Returning the raw data needed to compute the model
    def raw_model(self):
        return self.key_min_min, self.data.dic_arr()[self.key_min_min], self.key_min_max, self.data.dic_arr()[self.key_min_max]
    # Returning wavelength in nm
    def wavelength(self):
        pass
    # Computing the model (first 4 parameters of the constructor)
    def spectrum(self):
        min_min, j_nu_min_min, min_max, j_nu_min_max = self.raw_model()
        # to be careful about empty txt files
        if (len(j_nu_min_min) == 3):
            print("Impossible to compute the spectra")
            print(min_min + " does not have enough data\n")
            return np.zeros(1), np.zeros(1)
        elif (len(j_nu_min_max) == 3):
            print("Impossible to compute the spectra")
            print(min_max + " does not have enough data\n")
            return np.zeros(1), np.zeros(1)
        else:
            print(j_nu_min_min[:,2])

            j_nu = (1.-self.gamma)*j_nu_min_min[:,2] + self.gamma*j_nu_min_max[:,2]
            lambdas = j_nu_min_max[:,0] * 1000. # it is in microns, then with this I convert them to nm
            spectrum = j_nu * (0.001/1.66)*4*np.pi*3e7
            spectrum = spectrum/(lambdas*lambdas) # conversion factors for units in W/nm/(Kg of H)
            return lambdas,spectrum
    def bolometric(self):
        lambdas,spectrum = self.spectrum()
        # Checking if no Data
        if len(lambdas)== 1:
            print("Impossible to compute bolometric luminosity")
            print("There is no spectral data for this model")
            return None
        return np.trapz(spectrum,lambdas)
    def plot_spec(self):
        lambdas,spectrum = self.spectrum()
        if len(lambdas)== 1:
            print("Impossible to plot the spectrum")
            print("There is no spectral data for this model")
            return None
        plt.semilogx(lambdas,spectrum) # this looks like an emission spectrum
        # plt.loglog do not, neither plt.semilogy
        plt.title(self.key_min_max[:-4])
        plt.xlabel('$nm$')
        plt.ylabel('$L_{\lambda}$' +' [W/nm/(kg of H)]')
        plt.savefig(self.key_min_max[:-4]+'.pdf')
        plt.show()
m = Model(umin= '0.20', umax='1e3', model='MW3.1_60',gamma = 0.3,data = d)
#a,b,c,d = m.raw_model()
#print(a,b,c,d)
#l,s = m.spectrum()
#bolometric = m.bolometric()
m.plot_spec()
