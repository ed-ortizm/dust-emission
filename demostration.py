#!/usr/bin/python
from models_dust import *

print("We are now loading all the data from the models into a dictionary using the class Data...\n")
d = Data()
print("From the method dic_arr() we obtain a dictionary, where the key is the name of a model.")
print("As for the value, this dictionary has an array with the relevant data for that model.")
print("That is: the emission spectrum between 1 cm and 1 micron. Lets check a cuple of then\n" )
dic_arr = d.dic_arr()

for x,y in dic_arr.items():
    print(x)
    print(y)
    break
print("\n")
print('U0.20_1e3_MW3.1_60.txt')
print(dic_arr['U0.20_1e3_MW3.1_60.txt'])
print('\n')
print("The total number of files with potential models is:")# 1542 files
print(len(dic_arr))
################################################################################
band = 'PACS_red.dat'
filter = Filter_handler(band)
print('\n')
print("We are now going to generate de emissin spectra for the last model showed:\n")
print("U0.20_1e3_MW3.1_60")
m = Model(umin= '0.20', umax='1e3', model='MW3.1_60',gamma = 0.3,data = d, filter=filter)
#a,b,c,d = m.raw_model()
#print(a,b,c,d)
print('\n')
print("Now we can obtain the wavelength range and emission for this model with a gamma of 0.3\n")
l,s = m.spectrum()
print('\n')
print("This is the wavelength range in nm:\n")
print(l)
print('\n')
print("This is the emission in [W/nm/(Kg of H)]\n")
print(s)

print('\n')
print("Now a plot of the spectrum (check for a PDF file in this directory)")
m.plot_spec()

print('\n')
print("Now we can compute the bolometric luminosity in [W/(Kg of H)]:")
bolometric = m.bolometric()
print(bolometric)

print('\n')
print("Finally we compute the luminosity density.")
print("in the band: " + band)
w,f = m.L_density()
print('\n')
print("Luminosity density per unit wavelength in [W/nm/(Kg of H)]")
print(w)
print('\n')
print("Luminosity density per unit frequency in [W/Hz/(Kg of H)]")
print(f)
print("\n")
print("That's it!!")
