import matplotlib.pyplot as plt
import numpy as np

n=5+np.random.randn(1000)
print(n)

m=list(range(len(n)))
print(m)

plt.bar(m,n)
plt.title("Raw Data")
plt.show()

plt.hist(n,bins=200)
plt.title("histogram")
plt.show()