#! /usr/bin/env python3
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
import scipy
from scipy.spatial.distance import cdist
from kneed import KneeLocator
import random
import os
import cv2
import math
import sys
import shutil
from datetime import datetime
begin_time = datetime.now()
filenames = []
totalImages = 0
images = []

def load_images_from_folder(folder): #loading all images from a specified folder n storing it in an array of images
    global totalImages
    global filenames
    for filename in os.listdir(folder):
        filenames.append(filename)
        img = cv2.imread(os.path.join(folder,filename), flags = cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
            totalImages +=1
    return images
main_path = "/home/ppspr/Downloads/images" #Specifing the path of images
allImages = load_images_from_folder(main_path)

print("Preprocessing")
print(datetime.now() - begin_time)
begin_time = datetime.now()

kp =[] #Storing keypoints of all images
des = [] ##Storing descriptors of all images
c = 0
for i in range(totalImages):
  totalFeaturePoints = 800
  dimensions = (totalFeaturePoints*32) +1 #Descriptors return a 32 bit 
  orb = cv2.ORB_create(nfeatures= totalFeaturePoints, edgeThreshold=0,fastThreshold=0)
  temp_kp, temp_des = orb.detectAndCompute(allImages[i], None) #Gets keypoints and descriptors
  a, b= temp_des.shape
  if (a == totalFeaturePoints): 
    kp.append(temp_kp)
    des.append(temp_des)
    des[c] = des[c].reshape(a*b)
    des[c] = np.append(des[c], 0)
    c +=1
  else : #Kmeans needs uniform data, so we need to remove images if they give feature points
    filename = filenames[i]
    os.remove(os.path.join(main_path,filename))
    totalImages -= 1
    filenames.remove(filename)
print("Feature extraction")
print(datetime.now() - begin_time)

n=totalImages
p = des
#k = int(input("Enter no. of clusters: "))
X = np.array(p)
begin_time = datetime.now()

distortions = []
inertias = []
mapping1 = {}
mapping2 = {}
K = range(1, 10)

for k in K:
    # Building and fitting the model
    kmeanModel = KMeans(n_clusters=k, random_state=0, ).fit(X)
    # kmeans.labels_
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_,
                                        'euclidean'), axis=1)) / X.shape[0])
    inertias.append(kmeanModel.inertia_)
 
    mapping1[k] = sum(np.min(cdist(X, kmeanModel.cluster_centers_,
                                   'euclidean'), axis=1)) / X.shape[0]
    mapping2[k] = kmeanModel.inertia_
slope = []
for key, val in mapping1.items():
    slope.append(val) #storing distortions
x = range(1, len(slope)+1)
kn = KneeLocator(x, slope, curve='convex', direction='decreasing')
k = kn.knee #optimum value of k
kmeans = KMeans(n_clusters=k, random_state=0, algorithm= "elkan", ).fit(X)
kmeans.labels_

print("Kmeans")
print(datetime.now() - begin_time)
begin_time = datetime.now()

cluster = np.zeros(dimensions*k).reshape(k,dimensions)
for i in range(k):
  r= random.randint(0,(n-1))
  for j in range(dimensions):
    cluster[i][j]= p[r][j]
cluster_labels = kmeans.labels_
print(cluster_labels)

def make_all_cluster_folder():
  for i in range(k):
    clusterFolderName = "Cluster" + str(i)
    path= os.path.join(main_path, clusterFolderName)
    os.mkdir(path)

def get_target_folder(cluster_label_value):
  clusterFolderName = "Cluster" + str(cluster_label_value)
  target_folder = os.path.join(main_path,clusterFolderName)
  return target_folder

def paste_images_to_folder(original_folder):
  i = 0
  for filename in filenames:
    original_path = os.path.join(original_folder,filename)
    target_path = os.path.join(get_target_folder(cluster_labels[i]), filename)
    shutil.copyfile(original_path, target_path, follow_symlinks=True)
    i += 1

make_all_cluster_folder()
paste_images_to_folder(main_path)

print("Cluster making")
print(datetime.now() - begin_time)
begin_time = datetime.now()