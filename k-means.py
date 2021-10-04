#! /usr/bin/env python3
import numpy as np
import random
import math
import sys
import os
directory = "Clusters"
parent_dir = os.getcwd()
print(parent_dir)
path = os.path.join(parent_dir, directory)
os.mkdir(path) #Making cluster directory for storing all clusters
d = int(input("Enter no. of dimensions "))
n = int(input("Enter no. of feature points "))
p = np.zeros((d+1)*n).reshape(n,(d+1))
p
for i in range(n):
  for j in range(d):
    p[i][j]=int(input("Enter value"))
print(p)
k = int(input("Enter no. of clusters"))
distanceForBestCase = np.zeros(10)
bestCaseClustersCentroid = np.zeros(d*k*10).reshape(10,k,d)
for counter in range(10):
  cluster = np.zeros(d*k).reshape(k,d)
  random_no = np.full(k,-1)
  for i in range(k):
    r= random.randint(0,(n-1))
    while r in random_no:
      r= random.randint(0,(n-1))
    random_no[i] = r
    for j in range(d):
      cluster[i][j]= p[r][j]
    for q in range(d):
      print(str(cluster[i][q]), end=" ")
    print("")
  def distance():
    dis=0
    for i in range(n):
      min_dis= sys.maxsize
      for j in range(k):
        for q in range(d):
          dis+= (p[i][q] - cluster[j][q])**2
        dis = math.sqrt(dis)
        if(dis < min_dis): #finding minimum distance
          min_dis= dis
          distanceForBestCase[counter] += min_dis
          p[i][d]=j #nearest cluster
  t=0
  prev_cluster = np.full((d*k),sys.float_info.max).reshape(k,d)
  for c in range(n):
    flag=0
    for j in range(k):
      for q in range(d):
        difference = (cluster[j][q] - prev_cluster[j][q])/cluster[j][q]
        #print("at "+str(t)+" iteration, difference is "+str(difference))
        if (abs(difference) < 0.01 ):
          continue
        else:
          flag=1
          break
    if flag == 0:
      break
    else:
      distance()
      sum = np.zeros((d+1)*k).reshape(k,(d+1))
      for i in range(k):
        for q in range(d):
          prev_cluster[i][q] = cluster[i][q]
      #print(prev_cluster)
      for j in range(k): #finding new k cluster points
        count =0
        for i in range(n):
          if(p[i][d] == j):
            for q in range(d):
              sum[j][q]+=p[i][q]
            count+=1
        sum[j][d]=count
      for i in range(k):
        if(sum[i][d]!=0):
          for q in range(d):
            cluster[i][q] = sum[i][q]/sum[i][d] #storing new cluster points
      bestCaseClustersCentroid[counter] = cluster     
    t+=1
index = np.where(distanceForBestCase == np.amin(distanceForBestCase))  
print(bestCaseClustersCentroid[index],t)
