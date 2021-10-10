#! /usr/bin/env python3
import numpy as np
#from sklearn.cluster import KMeans
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
p = np.float32(des)
k=2
Z = np.array(p)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, totalImages, 1.0)
ret,label,center=cv2.kmeans(Z,k,None,criteria,totalImages,cv2.KMEANS_RANDOM_CENTERS)

def make_all_cluster_folder():
  path = os.path.join(main_path,"Cluster-0")
  os.mkdir(path)
  path = os.path.join(main_path,"Cluster-1")
  os.mkdir(path)
#   path = os.path.join(main_path,"Cluster-2")
#   os.mkdir(path)

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
    target_path = os.path.join(get_target_folder(label.ravel()[i]), filename)
    #print(original_path)
    shutil.copyfile(original_path, target_path, follow_symlinks=True)
    i += 1
make_all_cluster_folder()
paste_images_to_folder(main_path)

##########################################
'''
cats = 4/18 (19)  
cars = 5/18 (17)
'''
##########################################