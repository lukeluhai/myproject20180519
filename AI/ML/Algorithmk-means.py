import numpy as np
from sklearn.cluster import KMeans

# k-means算法实例


def loadData(filePath):
    fr = open(filePath, 'r+')
    lines = fr.readlines()
    retData = []
    retCityname = []
    for line in lines:
        items = line.strip().split(',')
        retCityname.append(items[0])
        for i in range(1, len(items)):
            retData.append(float(items[i]))
    return retData, retCityname


data, cityName = np.loadData('city.txt')
km = KMeans(n_clusters=3)
label = km.fit_predict(data)
expenses = np.sum(km.cluster_centers_, axis=1)
CityCluster = [[], [], []]
for i in range(len(cityName)):
    CityCluster[label[i]].append(cityName[i])
for i in range(len(CityCluster)):
    print(expenses[i])
    print(CityCluster[i])

