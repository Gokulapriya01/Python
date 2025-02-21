import numpy as np

marr=np.array([21,30,41,50,61,70,81,90,101])
print(np.max(marr))
print(np.sum(marr))
print(np.min(marr))
print(np.average(marr))

marr2=np.reshape(marr,(3,3))
print(marr2)
print(np.max(marr2, axis=1))
print(np.sum(marr2,axis=1))
print(np.sum(marr2,axis=0))
marr3=marr2.flatten()
print(marr3)