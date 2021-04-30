#For mono-atomic



import numpy as np
import matplotlib.pyplot as plt
import math
#Creating the matrix
E0 = -10
Beta = -2
n = 4000#Rank of matrix
M = np.zeros((n,n))
#print(M)
for i in range (n):
    for j in range (n):
        if i == j:
            M[i][j] = E0
        elif j == i+1 :
            M[i][j] = Beta
        elif j == i-1 :
            M[i][j] = Beta
for i in range(n):
    for j in range(n):
        if i == n-1 and j==0:
            M[i][j] = Beta
        elif i == 0 and j == n-1:
            M[i][j] = Beta              
print(M) #Starting matrix is constructed.
#Now our goal is to diagonalize the matrix.
w,v = np.linalg.eig(M) #Eigen values of matrix M
print(w)
q = w.sort() #Arranged in ascending order
#print(w)



wid=math.sqrt(n)
div=int(wid)


plt.hist(w,bins= div)
#plt.hist(w,bins = bi)
d = w[n-1] - w[0]
step = d/n
print(step)
xlegend = plt.xlabel('Eigen value')
ylegend = plt.ylabel('Density of eigen states')
#plt.style.use('ggplot')
plt.title(f'For dimension n={n}')
plt.show()