import math
import ruspini
import numpy as np

# init K
k = 4

# init centroid by random
# centroids[i] = [x, y]
centroids = {
    i+1 : [np.random.randint(0,80),np.random.randint(0,80)]
    for i in range(k)
}

# ---------- START FUNGSI ------------ #

def hitungJarak(point, centroid):
    return math.sqrt(
        math.pow(point['x'] - centroid[0], 2) + math.pow(point['y'] - centroid[1], 2)
    )

def cariTerdekat(_arr):
    return np.argmin(_arr)+1

# centroids[i] = [x, y]
# centroids = [
#     1 : [.. , ..],
#     2 : [.. , ..],
#     3 : [.. , ..],
#     4 : [.. , ..],
# ]
def generateCentroid(_arr,_k):          
    out = []
    for i in range(1,_k+1):
        dx = 0
        dy = 0
        count = 0
        for j in range(0,len(_arr)):
            if _arr[j]['cluster'] == i :
                count += 1
                dx += _arr[j]['x']
                dy += _arr[j]['y']
        try:
            out.append((i, [dx/count, dy/count]))
        except Exception as e:
            out.append((i, [0, 0]))
    # print(dict(out))    
    return dict(out)

def cekCentroid(oldCentroid, newCentroid):
    #untuk terus looping status cek harus True
    _s = True
    for i in oldCentroid.keys():
        print("CEK CENTROID : %i"%i)
        print("- Old : %a"%(oldCentroid[i]))
        print("- New : %a"%(newCentroid[i]))
        # print("old : %a --- new : %a"%(oldCentroid[i],newCentroid[i]))
        if oldCentroid[i][0] == newCentroid[i][0] and  oldCentroid[i][1] == newCentroid[i][1]:
            _s = False
        else :
            return True
    return _s

def cluster(_data, _centroid):
    out = []
    newdata = []
    # for i in _centroid.keys():
    #     d = []
    #     for j in range(0, len(_data)):
    #         d.append(hitungJarak(_data[j],_centroid[i]))
    #         print("cluster %i -- data %i : %f"%(i,j,hitungJarak(_data[j],_centroid[i])))
    #     newdata.append(d)
    # print(newdata[0])

    for i in range(0, len(_data)):
        d = []
        for j in _centroid.keys():
            d.append(hitungJarak(_data[i],_centroid[j]))
            # print("cluster %i -- data %i : %f"%(j,i,hitungJarak(_data[i],_centroid[j])))
        newdata.append(d)
    # print(newdata)

    for i in range(0, len(newdata)):
        out.append({
            'x'         : _data[i]['x'],
            'y'         : _data[i]['y'],
            'cluster'   : cariTerdekat(newdata[i])
        })
        # print(cariTerdekat(newdata[i]))
    # print(out)
    return out

# ------------ END FUNGSI ------------ #


# --------------- LOOP --------------- #
d = []
citerasi = 0
iterasi = True
while iterasi :
    citerasi += 1
    print("\n-------------------------------")
    print("ITERASI KE -- %i"%(citerasi))
    print("-------------------------------")
    d = cluster(ruspini.data,centroids)
    newCentroid = generateCentroid(d,k)
    iterasi = cekCentroid(centroids,newCentroid)
    centroids = newCentroid

print("\n-------------------------------")
print("Data Final Klustering")
print("-------------------------------")
print(d)