import numpy as np
from numpy import newaxis
import matplotlib.pyplot as plt

# 创建3维矩阵
arr1 = np.arange(30).reshape(2, 3, 5)
# [[[ 0  1  2  3  4]
#   [ 5  6  7  8  9]
#   [10 11 12 13 14]]
#
#  [[15 16 17 18 19]
#   [20 21 22 23 24]
#   [25 26 27 28 29]]]
print(arr1)
print(arr1.ndim)  # 维度
print(arr1.shape)  # 数组维度
print(arr1.size)  # 元素总数
print(arr1.dtype)  # 描述数组中元素类型的对象
print(arr1.itemsize)  # 数组中每个元素的字节大小

# 数组创建
# 从列表中创建
arr2 = np.array([range(10)])
print(arr2)
# 从元祖中创建
arr2 = np.array((range(10)))
print(arr2)
arr2 = np.array([(0, 1, 2, 3, 4), (5, 6, 7, 8, 9)])
print(arr2)

# 创建时制定数据类型
arr3 = np.array([(0, 1, 2, 3, 4), (5, 6, 7, 8, 9)], dtype=complex)
print(arr3)

# 创建值为0,1的数组
arr4 = np.zeros((2, 3, 5))
arr5 = np.ones((2, 3, 5), dtype=np.float)
print(arr4)
print(arr5)

# 类似range的函数使用
# def arange(start=None, stop=None, step=None, dtype=None): # known case of numpy.core.multiarray.arange
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None):
arr6 = np.arange(10, 80, 3)
arr7 = np.linspace(1, 3, num=50)
print(arr6)
print(arr7)
# 打印数组
# reshape(self, shape, *shapes, order='C'): # known case of numpy.core.multiarray.ndarray.reshape
print(arr7.reshape(5, 5, 2))
# 数组操作
arr8 = np.array(range(10))
arr9 = np.array(range(10))
print(arr8 + arr9)
print(arr8 * arr9)
print(arr8.reshape(2, 5) * arr9.reshape(2, 5))
print(arr8 > 5)
print(arr8 ** 2)
print(np.tan(arr8))
# 矩阵乘积
print(np.dot(arr8.reshape(2, 5), arr9.reshape(5, 2)))
arr8 += 4
print(arr8)
print(np.exp(arr8 + 1j))
print(np.exp(arr8 + 1j).dtype)
# 计算元素的和 ，最大值，最小值
arr10 = np.random.random((3, 5))
print(arr10.sum())
print(arr10.max())
print(arr10.min())
print(np.random.random((2, 5)))  # Return random floats in the half-open interval [0.0, 1.0).
print(np.random.randn(2, 5))  # Return a sample (or samples) from the “standard normal” distribution.

# 利用axis进行数组操作  axis=0   axis=1  axis=2 axis=3
# 慢慢体会把，看不懂
arr11 = np.arange(210).reshape(3, 2, 5, 7)
print(arr11)
print('result')
print('axis=0')
print(arr11.sum(axis=0))
print('axis=1')
print(arr11.sum(axis=1))
print('axis=2')
print(arr11.sum(axis=2))
print('axis=3')
print(arr11.sum(axis=3))
# 通用函数 all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov,
# cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero,
# outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where

# 索引、切片和迭代
arr12 = np.array(range(30)).reshape(3, 2, 5)
print(arr12)
print(arr12[0])
print(arr12[0:2])
print(arr12[0:2][0][0][0:3])

arr13 = np.array(range(16)) * 5
print(arr13)
print(arr13[::2])
print(arr13[::-1])  # 倒序


def f(x, y):
    return 10 * x + y


arr13 = np.fromfunction(f, (6, 7), dtype=float)
print(arr13)
print(arr13[4, 5])
print(arr13[0:4, 1])
print(arr13[0:3])
print(arr13[:, 2:4])
print(arr13[-1])
print(arr13.shape)
print(arr13[1, ...])
print(arr13[..., 2])

print('=========================================分隔线==========================================')
# 对多维数组的迭代是相对于第一个轴完成的
for row in arr13:
    print(row)
for element in arr13.flat:
    print(element)

# 形状操作
arr14 = 10 * np.random.random((3, 4))
print(arr14)
print(arr14.shape)
print(arr14.ravel())
print(arr14.reshape(4, 3))
print(arr14.T)
# 数组堆叠
print('# 数组堆叠===================================================================================')
arr15 = np.int32(10 * np.random.random((3, 5)))
arr16 = np.int32(10 * np.random.random((3, 5)))
print(np.vstack((arr15, arr16)))
print(np.hstack((arr15, arr16)))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# column_stack将1-D数组作为列堆叠到2-D数组中。取一个1-D数组的序列，
# 并将它们作为列堆叠以形成单个2-D数字组。2-D数组按原样堆叠，就像hstack。1-D数组首先变为2-D列。
print(np.column_stack((a, b)))
print(np.row_stack((a, b)))
print(np.vstack((a, b)))
print(np.hstack((a, b)))
print(a[:, newaxis])
print(np.column_stack((a[:, newaxis], b[:, newaxis])))
print(np.hstack((a[:, newaxis], b[:, newaxis])))

print('#将一个数组分成几个较小的数组===============================================================')
# 将一个数组分成几个较小的数组
a = np.arange(30)
a = a.reshape(5, 6)
print(a)
print(np.hsplit(a, 3))
print(np.vsplit(a, 5))
print(np.hsplit(a, (1, 2, 5)))  # 安装列0,1,2-4,5来分
# 简单赋值不会创建数组对象或其数据的拷贝
a = np.arange(30)
b = a
print(b is a)
print(a)
b += 1
print(a)

# 不同的数组对象可以共享相同的数据。view方法创建一个新数组对象，该对象看到相同的数据。
# 浅复制
c = a.view()
print(c is a)
print(c.base is a)
print(c == a)
print(c.flags.owndata)
c[2:10] = 0
print(a)
# 深复制
d = a.copy()
print(d is a)
print(d.base is a)
d[0:10] = 999
print(a)
print(d)

#
# 函数和方法概述
# 这里是一些有用的NumPy函数和方法名称按类别排序的列表。有关完整列表，请参见Routines。
#
# 数组创建
# arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like
# 转换
# ndarray.astype，atleast_1d，atleast_2d，atleast_3d，mat
# 操纵
# array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack
# 问题
# all，any，nonzero，where
# 顺序
# argmax, argmin, argsort, max, min, ptp, searchsorted, sort
# 操作
# choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum
# 基本统计
# cov，mean，std，var
# 基本线性代数
# cross，dot，outer，linalg.svd，vdot

# 花式索引和索引技巧
print("# 花式索引和索引技巧====================================================================")
a = np.arange(30) ** 2
i = np.array([1, 2, 2, 2, 10, 2, 11, 25])
j = np.array([[2, 2, 2, 2], [5, 5, 5, 9]])
print(a)
print(a[i])
print(a[j])

palette = np.array([[0, 0, 0],
                    [255, 0, 0],
                    [0, 255, 0],
                    [0, 0, 255],
                    [255, 255, 255]])
image = np.array([[0, 1, 2, 0],
                  [0, 3, 4, 0]])
print(palette[image])
# 还可以为多个维度提供索引。每个维度的索引数组必须具有相同的形状。
a = np.arange(12).reshape(3, 4)
print(a)
i = np.array([[0, 1], [1, 2]])
j = np.array([[2, 1], [3, 3]])
print(a[i, j])
print(a[[i, j]])

s = np.array([i, j])
print(s)
# print(a[s]) IndexError: index 3 is out of bounds for axis 0 with size 3
print(tuple(s))
print(a[tuple(s)])

# 另一个常见的使用数组索引的方法是搜索时间相关系列的最大值：
time = np.linspace(20, 145, 5)  # time scale
data = np.sin(np.arange(20)).reshape(5, 4)  # 4 time-dependent series
print(time)
print(data)
ind = data.argmax(axis=0)  # index of the maxima for each series
print(ind)
print(data[ind, range(data.shape[1])])
print(data.shape[1])
print(time[ind])


def mandelbrot(h, w, maxit=20):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y, x = np.ogrid[-1.4:1.4:h * 1j, -2:0.8:w * 1j]
    c = x + y * 1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z ** 2 + c
        diverge = z * np.conj(z) > 2 ** 2  # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i  # note when
        z[diverge] = 2  # avoid diverging too much
    return divtime


plt.imshow(mandelbrot(400, 400))
# plt.show()

# 使用布尔索引的第二种方法更类似于整数索引；对于数组的每个维度，我们给出一个1D布尔数组，选择我们想要的切片：

a = np.arange(12).reshape(3, 4)
b1 = np.array([False, False, True])  # first dim selection
b2 = np.array([False, True, False,True])  # second dim selection
print(a)
print(a[b1, :])  # selecting rows
print(a[b1])  # same thing
print(a[:, b2])  # selecting columns
print([b1,b2])
print()
print(a[[b1, b2]])
print(a[[b1, b2]].shape)  # a weird thing to do 怎么回事

a = np.arange(25).reshape(5,5)
b1 =np.array([True,True,True,True,True])
b2 =np.array([True,True,True,True,False])
c = np.array(b1,b2)
print(a)
print(a[c])

# ix_()函数
# ix_函数可以用于组合不同的向量，以便获得每个n-uplet的结果。例如，如果要计算从向量a、b和c中的取得的所有三元组的所有a + b * c：

