import csv
import numpy as np
import math

with open("landmark.csv") as file_name:
    array = np.loadtxt(file_name, delimiter=",").ravel()
    #print(array)
    
x1 = array[::3]
y1 = array[1::3]
z1 = array[2::3]
    
x2 = []
y2 = []
z2 = []
for i in range(0,21):
    a = x1[i] - x1[0]
    x2.append(a)
    b = y1[i] - y1[0]
    y2.append(b)
    c = z1[i] - z1[0]
    z2.append(c)
#print(x2, y2, z2)

#k = math.sqrt((x2[1] - x2[0])**2 + (y2[1] - y2[0])**2)
k = math.sqrt((x2[1] - x2[0])**2 + (y2[1] - y2[0])**2 + (z2[1] - z2[0])**2)
print(k)

x = []
y = []
z = []
for i in range(20):
    d = x2[i] / k
    x.append(d)
    e = y2[i] / k
    y.append(e)
    f = z2[i] / k
    z.append(f)
#print(x, y, z)

"""
#xy = []
xy.extend(x)
xy.extend(y)
np.savetxt('distance.csv', xy, delimiter=',')
"""

xyz = [] 
xyz.extend(x)
xyz.extend(y)
xyz.extend(z)

np.savetxt('distance.csv', xyz, delimiter=',')
