#!/usr/bin/python
from models_dust import *

print("We are now loading all the data from the models into a dictionary using the class Data...\n")
d = Data()
print("From the method dic_arr() we obtain a dictionary, where the key is the name of a model.")
print("As for the value, this dictionary has an array with the relevant data for this project.")
print("That is: the emission spectrum between 1 cm and 1 micron. Lets check a cuple of then\n" )
dic_arr = d.dic_arr()

for x,y in dic_arr.items():
    print(x)
    print(y)
    break
print("\n")
print('U0.20_1e3_MW3.1_60.txt')
print(dic_arr['U0.20_1e3_MW3.1_60.txt'])

print("The total number of files with potential models is:")# 1542 files
print(len(dic_arr))

print("We are now going to generate de emissin spectra for the last model showed:\n")
print("U0.20_1e3_MW3.1_60")
m = Model(umin= '0.20', umax='1e3', model='MW3.1_60',gamma = 0.3,data = d)
#a,b,c,d = m.raw_model()
#print(a,b,c,d)
print("Now we can obtain the wavelength range and emission for this model with a gamma of 0.3\n")
l,s = m.spectrum()
print("This is the wavelength range in nm:\n")
print(l)
print("This is the emission in [W/nm/(Kg of H)]\n")
print(s)

print("Now we can compute the bolometric luminosity:\n")
bolometric = m.bolometric()
print(bolometric)

print("And finally a plot of the spectrum")
m.plot_spec()
