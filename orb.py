#! /usr/bin/env python3
import random
import math
import sys
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
#np.set_printoptions(threshold=sys.maxsize) #for printing complete array without truncation

totalImages = 0
def load_images_from_folder(folder): #loading all images from a specified folder n storing it in an array of images
    global totalImages
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
            totalImages +=1
    return images
allImages = load_images_from_folder("/home/ppspr/Downloads/images")
kp =[]
des = []
for i in range(totalImages):
  totalFeaturePoints = 500
  orb = cv2.ORB_create(nfeatures= totalFeaturePoints)
  temp_kp, temp_des = orb.detectAndCompute(allImages[i], None)
  kp.append(temp_kp)
  des.append(temp_des)
  a, b= des[i].shape
  des[i] = des[i].reshape(a*b)
  des[i] = np.append(des[i], 0)

d = totalFeaturePoints*32 
n=totalImages
print(d)
p = np.zeros((d+1)*n).reshape(n,d+1)
p = des
print(p)

#np.savetxt('/home/ppspr/code/python/test.txt', p) #did this for getting value of p and running it on scikit code

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
        if (abs(difference) < 0.001 ):
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
  #print(t)
index = np.where(distanceForBestCase == np.amin(distanceForBestCase))  
print(bestCaseClustersCentroid[index],t)
for i in range(totalImages): #Printing which image belobgs to which cluster
  print(p[i][d])