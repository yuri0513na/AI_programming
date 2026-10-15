import numpy as np

v=np.array([[1,2],[3,4]])
w=np.array([[5,6],[7,8]])
print(v)
print(w)
print(v.dot(w)) #行列の掛け算

x=np.array([1,2,3])
y=np.array([4,5,6])
print(x*y) #アダマール積（要素同士の掛け算）