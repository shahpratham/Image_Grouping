import numpy as np
import random
import math
import sys
n = int(input("Enter no. of feature points ")) #code is made for 2d
p = np.zeros(3*n).reshape(n,3) #storing n points x,y dimension and their respective cluster
for i in range(n):
  for j in range(2):
    p[i][j]=int(input("Enter value"))
k = int(input("Enter no. of clusters"))
cluster = np.zeros(2*k).reshape(k,2)
for i in range(k):
  r= random.randint(0,n)
  cluster[i][0]= p[r][0]
  cluster[i][1]= p[r][1]
  c=0
for c in range(n):
  for i in range(n): #for finding which point belongs to which cluster
    min_dis= sys.maxsize
    for j in range(k):
      d= math.sqrt( (p[i][0] - cluster[j][0])**2 + (p[i][1] - cluster[j][1])**2 )
      if(d<min_dis): #finding minimum distance
        min_dis= d
        p[i][2]=j #nearest cluster
  sum = np.zeros(3*k).reshape(k,3)
  for j in range(k): #finding new k cluster points
    count =0
    for i in range(n):
      if(p[i][2] == j):
        sum[j][0]+=p[i][0]
        sum[j][1]+=p[i][1]
        count+=1
    sum[j][2]=count
  for i in range(k):
    cluster[i][0] = sum[j][0]/sum[j][2] #storing new cluster points
    cluster[i][1] = sum[j][1]/sum[j][2]