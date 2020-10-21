import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,256,endpoint=True)
print('x=',x)

s=np.sin(x)
c=np.cos(x)

plt.plot(x,s)
plt.plot(x,c)
plt.show()