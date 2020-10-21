import numpy as np
print("-@-"*20)
ddarr=np.array([[1,2,3],[4,5,6]])
print("ddarr.dim=",ddarr.ndim)
print("ddarr.shape=",ddarr.shape)
print("ddarr.size=",ddarr.size)
print("ddarr.dtype=",ddarr.dtype)

print(ddarr)

print(ddarr[0,1])
print(ddarr[0])
print(ddarr[:,0])
print(ddarr[1,:])