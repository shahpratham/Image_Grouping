import numpy as np
import random
import math
import sys


# Creating an array for d dimensions & n feature points
d = int(input("Enter no. of dimensions "))
n = int(input("Enter no. of feature points "))
p = np.zeros((d+3)*n).reshape(n,(d+3))


# Taking Manual input for n feature points
for i in range(n):
  for j in range(d):
    p[i][j]=int(input("Enter value"))
  p[i][d+1] = sys.maxsize
  #p[i][d+2] = -1
print(p)

# Creating array for no. of desired clusters
k = int(input("Enter no. of clusters"))
cluster = np.zeros(d*k).reshape(k,d)

# Random number generator
random_no = np.full(k,-1)

for i in range(k):
  r= random.randint(0,(n-1))
  while r in random_no:   # For preventing repetition of cluster centers
    r= random.randint(0,(n-1))
  random_no[i] = r
  for j in range(d):
    cluster[i][j]= p[r][j]
  for q in range(d):
    print(str(cluster[i][q]), end=" ")
  print("")

def distance():
  dis =0
  for i in range(n):
    min_dis= p[i][d+1]
    val = int(p[i][d])
    if p[i][d+2]== 0 :
      for j in range(k):
        dis = 0
        for q in range(d):
          dis+= (p[i][q] - cluster[j][q])**2
        dis = math.sqrt(dis)
        p[i][d+2]+=1
        if(dis < min_dis): #finding minimum distance
          min_dis= dis
          p[i][d]=j #nearest cluster
          p[i][d+1]= min_dis
      #p[i][d+2] += 2

    elif p[i][d+2] > 0 :
      dis =0
      for q in range(d):
        dis += (p[i][q] - cluster[val][q]) ** 2
      dis = math.sqrt(dis)
      p[i][d + 2] += 1
      if dis > min_dis:
        for j in range(k):
          dis = 0
          # if j == p[i][d] :
          #   continue
          for q in range(d):
            dis += (p[i][q] - cluster[j][q]) ** 2
          dis = math.sqrt(dis)
          p[i][d + 2] += 1
          if (dis < min_dis):  # finding minimum distance
            min_dis = dis
            p[i][d] = j  # nearest cluster
            p[i][d + 1] = min_dis


t=0
prev_cluster = np.full((d*k),sys.float_info.max).reshape(k,d)
for c in range(n):
  flag=0
  for j in range(k):
    for q in range(d):
      difference = (cluster[j][q] - prev_cluster[j][q])/cluster[j][q]
      print("at "+str(t)+" iteration, difference is "+str(difference))
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
    print(prev_cluster)
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
    print(cluster)
  t+=1
print(cluster, t)

for x in range (n) :
  print(p[x][d+2])

print(p)