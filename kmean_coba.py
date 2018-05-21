import ruspini
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

k = 4

#mencari max dari tiap-tiap attribut
def cariMax(arr, key):
    r = []
    for i in range(0, len(arr)):
        r.append(arr[i][key])
    return max(r)
    
#mencari min dari tiap-tiap attribut
def cariMin(arr, key):
    r = []
    for i in range(0, len(
        arr)):
        r.append(arr[i][key])
    return min(r)

#menghitung jarak euclidean
def hitungJarak(_p, _c) :
    return math.sqrt(math.pow(_p['x']-_c[]))


# centroids[i] = [x, y]
np.random.seed(300)
centroids = {
    i+1 : 
    [
        np.random.randint(
        cariMin(ruspini.data,'x'),
        cariMax(ruspini.data,'x'))
    ,   np.random.randint(
        cariMin(ruspini.data,'y'),
        cariMax(ruspini.data, 'y'))
    ]
    for i in range(k)
}

print('Centroids')
for i in centroids.keys():
    print(centroids[i])
