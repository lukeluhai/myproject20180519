# 非负矩阵分解方法
import matplotlib.pyplot as plt
from sklearn import decomposition
# 加载PCA算法包
from sklearn.datasets import fetch_olivetti_faces
# 加载Olivetti 人脸数据集导入函数
from numpy.random import RandomState
# 加载randomstate用于创建随机种子
n_row, n_col = 2, 3
# 设置展示时的排列情况
n_components = n_row * n_col
# 设置提取的特征的数目
image_shape = (64, 64)
# 设置人脸数据图片的大小
datasets = fetch_olivetti_faces(shuffle=True, random_state=RandomState(0))
faces = datasets.data


def plot_gallery(title, images, n_col=n_col, n_row=n_row):
    # 创建图片，并制定图片大小（英寸）
    plt.figure(figsize=(2. * n_col, 2.26 * n_row))
    # 设置标题及字号大小
    plt.suptitle(title, size=16)

    for i, comp in enumerate(images):
        # 选择画制的子图
        plt.subplot(n_row, n_col, i + 1)
        vmax = max(comp.max(), -comp.min())
        # 对数值归一化，并以灰度图形显示。
        plt.imshow(
            comp.reshape(image_shape),
            cmap=plt.cm.gray,
            interpolation='nearest',
            vmin=-vmax,
            vmax=vmax)
        # 去除子图的坐标轴标签
        plt.xticks(())
        plt.yticks(())
        # 对子图位置及间隔进行调整
        plt.subplots_adjust(0.01, 0.05, 0.99, 0.93, 0.04, 0.)


# NMF和PCA实例 并存放在一个列表中
estimators = [
    ('Eigenfaces=PCA using randomized SVD',
     decomposition.PCA(
         n_components=6,
         whiten=True)),
    ('Non-negative components-NMF',
     decomposition.NMF(
         n_components=6,
         init='nndsvda',
         tol=5e-3))]
for name, estimator in estimators:
    # 调用PCA或NMF提取特征
    estimator.fit(faces)
    # 获取提取的特征
    components_ = estimator.components_
    # 按照固定格式进行排列
    plot_gallery(name, components_[:n_components])
plt.show()
