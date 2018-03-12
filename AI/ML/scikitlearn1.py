from sklearn import datasets


# boston 房价数据集

from sklearn.datasets import load_boston
boston = load_boston()
print(boston.data)
data, target = load_boston(return_X_y=True)
print(data)
print(target)


# 鸢尾花数据集-加载实例

from sklearn.datasets import load_iris
iris = load_iris()
print(iris)
print(iris.data.shape)
print(iris.target_names)

# 手写数据集
from sklearn.datasets import load_digits
digits = load_digits()
print(digits.data.shape)
print(digits.target.shape)
print(digits.images.shape)
import matplotlib.pyplot as plt
plt.matshow(digits.images[0])
plt.show()

import numpy as np
from sklearn.cluster import KMeans

# k-means算法实例

def loadData(filePath):
    fr=open(filePath,'r+')
    lines=fr.readlines()
    retData=[]
    retCityname=[]
    for line in lines:
        items=line.strip().split(',')
        retCityname.append(items[0])
        for i in range(1,len(items)):
            retData.append(float(items[i]))
    return retData,retCityname



data,cityName=np.loadData('city.txt')
km=KMeans(n_clusters=3)
label=km.fit_predict(data)
expenses=np.sum(km.cluster_centers_,axis=1)
CityCluster=[[],[],[]]
for i in range(len(cityName)):
    CityCluster[label[i]].append(cityName[i])
for i in range(len(CityCluster)):
    print(expenses[i])
    print(CityCluster[i])