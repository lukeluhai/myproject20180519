# DBSCAN算法实例
from sklearn.cluster import DBSCAN
import sklearn.cluster as skc
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
mac2id = dict()
onlinetimes = []
f = open('TestData.txt')
for line in f:
    # 读取每条数据中的mac地址，开始上网时间，上网时长
    mac = line.split(',')[2]
    onlinetime = int(line.split(',')[6])
    starttime = int(line.split(',')[4].split(' ')[1].split(':')[0])
    if mac not in mac2id:
        mac2id[mac] = len(onlinetimes)
        onlinetimes.append((starttime, onlinetime))
    else:
        onlinetimes[mac2id[mac]] = [(starttime, onlinetime)]
real_X = np.array(onlinetimes).reshape((-1, 2))
# 调用DBSCAN方法进行训练，LAbels为每个数据的簇标签
X = real_X[:, 0:1]
db = skc.DBSCAN(eps=0.01, min_samples=20).fit(X)
labels = db.labels_
# 打印数据被记上的标签，计算标签为-1，即噪声数据的比例
print('labels:')
print(labels)
ratio = len(labels[labels[:] == -1]) / len(labels)
print(ratio)
# 计算簇的个数并进行打印，评价聚类效果
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print(n_clusters_)
print(metrics.silhouette_score(X, labels))
# 打印各簇的标号，及各簇内数据
for i in range(n_clusters_):
    print('Cluster', i)
    print(list(X[labels == i].flatten()))
