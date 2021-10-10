#! /usr/bin/env python3
import numpy as np
from sklearn.cluster import KMeans
import random
import os
import cv2
import math
import sys
import shutil

#np.set_printoptions(threshold=sys.maxsize)

filenames = []
totalImages = 0
def load_images_from_folder(folder): #loading all images from a specified folder n storing it in an array of images
    global totalImages
    global filenames
    images = []
    for filename in os.listdir(folder):
        filenames.append(filename)
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
            totalImages +=1
    return images
main_path = "/home/ppspr/Downloads/images"
allImages = load_images_from_folder(main_path)
kp =[]
des = []
for i in range(totalImages):
  totalFeaturePoints = 1500
  orb = cv2.ORB_create(nfeatures= totalFeaturePoints)
  temp_kp, temp_des = orb.detectAndCompute(allImages[i], None)
  kp.append(temp_kp)
  des.append(temp_des)
  a, b= des[i].shape
  des[i] = des[i].reshape(a*b)
  des[i] = np.append(des[i], 0)

n=totalImages
p = des
k=2
X = p
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
kmeans.labels_

dimensions = (totalFeaturePoints*32) +1
cluster = np.zeros(dimensions*k).reshape(k,dimensions)
for i in range(k):
  r= random.randint(0,(n-1))
  for j in range(dimensions):
    cluster[i][j]= p[r][j]
cluster_labels = kmeans.labels_
print(cluster_labels)
print(kmeans.predict(cluster))

print(kmeans.cluster_centers_)

def make_all_cluster_folder():
  path = os.path.join(main_path,"Cluster-0")
  os.mkdir(path)
  path = os.path.join(main_path,"Cluster-1")
  os.mkdir(path)
  path = os.path.join(main_path,"Cluster-2")
  os.mkdir(path)

def get_target_folder(cluster_label_value):
  if cluster_label_value == 0:
    target_folder = os.path.join(main_path,"Cluster-0")
  elif cluster_label_value == 1:
    target_folder = os.path.join(main_path,"Cluster-1")
  elif cluster_label_value == 2:
    target_folder = os.path.join(main_path,"Cluster-2")
  return target_folder

def paste_images_to_folder(original_folder):
  i = 0
  for filename in filenames:
    original_path = os.path.join(original_folder,filename)
    target_path = os.path.join(get_target_folder(cluster_labels[i]), filename)
    #print(original_path)
    shutil.copyfile(original_path, target_path, follow_symlinks=True)
    i += 1
make_all_cluster_folder()
paste_images_to_folder(main_path)

######################################
'''
cats = 3/18 (19)  Total images of cats were 19 but sklearn got 18 images of cat out of which 3 were of car
cars = 2/18 (17)  Total images of cars were 17 but sklearn got 18 images of car out of which 3 were of cat
'''
######################################
