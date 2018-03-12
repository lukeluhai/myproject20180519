import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 1000)
y = 1+x+x**2+x**3+5*x**4+x**5+x**6+x**7+x**(0.5)
# y = np.sin(x)

# z = np.cos(x**2)
plt.figure(figsize=(8, 4))
plt.plot(x, y,color='red',linewidth=2)
# plt.plot(x, z, 'b--')
plt.xlabel('times')
plt.ylabel('volt')
plt.title('plt first example')
#plt.ylim(-1.2,1.2)
plt.legend()
plt.show()

