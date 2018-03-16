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

