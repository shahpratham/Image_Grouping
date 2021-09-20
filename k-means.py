import numpy as np
import random
import math
import sys
d = int(input("Enter no. of dimensions "))
n = int(input("Enter no. of feature points "))
p = np.zeros((d+1)*n).reshape(n,(d+1))
for i in range(n):
  for j in range(d):
    p[i][j]=int(input("Enter value"))
    print(p)
k = int(input("Enter no. of clusters"))
cluster = np.zeros(d*k).reshape(k,d)
random_no = np.full(k,-1)
for i in range(k):
  r= random.randint(0,(n-1))
  while r in random_no:
    r= random.randint(0,(n-1))
  random_no[i] = r
  for j in range(d):
    cluster[i][j]= p[r][j]
  print(str(cluster[i][0]) +" "+ str(cluster[i][1]))
def distance():
  dis=0
  for i in range(n):
    min_dis= sys.maxsize
    for j in range(k):
      for q in range(d-1):
        dis+= (p[i][q] - cluster[j][q])**2
      dis = math.sqrt(dis)
      if(dis < min_dis): #finding minimum distance
        min_dis= dis
        p[i][d-1]=j #nearest cluster
t=0
for c in range(n):
  distance()
  sum = np.zeros((d+1)*k).reshape(k,(d+1))
  for j in range(k): #finding new k cluster points
    count =0
    for i in range(n):
      if(p[i][d-1] == j):
        for q in range(d):
          sum[j][q]+=p[i][q]
        count+=1
    sum[j][d-1]=count
  for i in range(k):
    if(sum[i][d-1]!=0):
      for q in range(d):
        cluster[i][q] = sum[i][q]/sum[i][d-1] #storing new cluster points  
  t+=1
for i in range(k):
  for q in range(0,d-1,2):
          print("Cluster is "+str(cluster[i][q]) +" "+ str(cluster[i][q+1]))