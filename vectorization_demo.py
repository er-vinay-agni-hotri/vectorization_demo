#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a = np.array([1,2,3,4,5])
print(a)


# In[6]:


import time
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c= np.dot(a,b)
toc = time.time()
print(c)
print("Vectorized version product : ", str(1000*(toc-tic)), " ms")

c = 0

tic = time.time()
for i in range(1000000):
    c+=a[i]*b[i]
    
toc=time.time()
print(c)
print("For loop: ", str(1000*(toc-tic)), " ms")

## Addition using Numpy
tic = time.time()
d= a+b
toc = time.time()
print(d)
print("Vectorized version: ", str(1000*(toc-tic)), " ms")





