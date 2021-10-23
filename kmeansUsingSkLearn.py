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
main_path = input("Enter path to your image directory: ") #Specifing the path of images
allImages = load_images_from_folder(main_path)

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

n=totalImages
p = des
X = np.array(p)
begin_time = datetime.now()

distortions = []
inertias = []
mapping1 = {}
mapping2 = {}
K = range(1, 20) #Kept a limit of 20 clusters, so it will predict no. cluster from 1 to 20

'''
  Distortion: It is calculated as the average of the squared distances from the cluster centers of the respective clusters. Typically, the Euclidean distance metric is used.
  Inertia: It is the sum of squared distances of samples to their closest cluster center.

We iterate the values of k from 1 to 20 and calculate the values of distortions for each value of k and calculate the distortion and inertia for each value of k in the given range.
'''

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
k = []

for key, val in mapping1.items():
    k.append(val) #stroing all values of distortions

x = range(1, len(k)+1)
kn = KneeLocator(x, k, curve='convex', direction='decreasing') #finding elbow point using Distortion
k = kn.knee
if k == None:
  k = int(input("You need to enter no. of cluster, our code couldnt predict :( ")) #It couldn't predict cluster when datasets contains similar images
print("No. of clusters: ", str(k))
kmeans = KMeans(n_clusters=k, random_state=0, ).fit(X)
kmeans.labels_

cluster = np.zeros(dimensions*k).reshape(k,dimensions)
for i in range(k):
  r= random.randint(0,(n-1))
  for j in range(dimensions):
    cluster[i][j]= p[r][j]
cluster_labels = kmeans.labels_ #Sroeing all labels in this

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