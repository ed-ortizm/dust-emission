#!/usr/bin/python
from models_dust.py import *

print("We are now loading all the data from the models into a dictionary using the class Data...")
d = Data()
print("From the method dic_arr() we obtain a dictionary, where the key is the name of a model.")
print("As for the value, this dictionary has an array with the relevant data for this project.")
print("That is: the emission spectrum between 1 cm and 1 micron. Lets check a cuple of then" )
dic_arr = d.dic_arr()

for x,y in dic_arr.items():
    print(x)
    print(y)
    break

print('U0.20_1e3_MW3.1_60.txt')
print(dic_arr['U0.20_1e3_MW3.1_60.txt'])

print("The total number of files with potential models is:")# 1542 files
print(len(dic_arr))

#m = Model(umin= '0.20', umax='1e3', model='MW3.1_60',gamma = 0.3,data = d)
#a,b,c,d = m.raw_model()
#print(a,b,c,d)
#l,s = m.spectrum()
#bolometric = m.bolometric()
#m.plot_spec()
