# For di-atomic


import numpy as np
import matplotlib.pyplot as plt
import math
#Creating the matrix
E1 = -5
E2 = -10
Beta = -2
n = 2900 #Rank of matrix
M = np.zeros((n,n))
#print(M)
for i in range (n):
    for j in range (n):
        if i == j:
            if i % 2 == 0:
                M[i][j] = E2
            else:
                M[i][j] = E1
        elif j == i+1 :
            M[i][j] = Beta
        elif j == i-1 :
            M[i][j] = Beta
print(M) #Starting matrix is constructed.
#Now our goal is to diagonalize the matrix.
w,v = np.linalg.eig(M) #Eigen values of matrix M
plt.hist(w,bins = 90)
#print(w)
q = w.sort() #Arranged in ascending order
#print(w)
d = w[n-1] - w[0]
step = d/n
print(step)
xlegend = plt.xlabel('Eigen value')
ylegend = plt.ylabel('Density of eigen states')
#plt.style.use('ggplot')
plt.title(f'For dimension n={n}')
plt.show()