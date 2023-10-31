import numpy as np
from scipy.cluster.vq import kmeans, vq
import random
import os
import cv2
import shutil
from datetime import datetime
from kneed import KneeLocator

filenames = []
totalImages = 0
images = []

def load_images_from_folder(folder):
    global totalImages
    global filenames
    for filename in os.listdir(folder):
        filenames.append(filename)
        img = cv2.imread(os.path.join(folder, filename), flags=cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
            totalImages += 1
    return images

main_path = input("Enter path to your image directory: ")
allImages = load_images_from_folder(main_path)

kp = []
des = []
c = 0

for i in range(totalImages):
    totalFeaturePoints = 800
    dimensions = (totalFeaturePoints * 32) + 1
    orb = cv2.ORB_create(nfeatures=totalFeaturePoints, edgeThreshold=0, fastThreshold=0)
    temp_kp, temp_des = orb.detectAndCompute(allImages[i], None)
    a, b = temp_des.shape
    if a == totalFeaturePoints:
        kp.append(temp_kp)
        des.append(temp_des)
        des[c] = des[c].reshape(a * b)
        des[c] = np.append(des[c], 0)
        c += 1
    else:
        filename = filenames[i]
        os.remove(os.path.join(main_path, filename))
        totalImages -= 1
        filenames.remove(filename)

n = totalImages
p = des
X = np.array(p)
begin_time = datetime.now()

distortions = []
inertias = []
mapping1 = {}
mapping2 = {}
K = range(1, 20)

for k in K:
    centroids, _ = kmeans(X, k)
    # Assign each data point to a cluster
    cluster_indices, _ = vq(X, centroids)
    distortions.append(sum(np.min(np.square(X - centroids[cluster_indices]), axis=1) / X.shape[0]))

x = range(1, len(K) + 1)
kn = KneeLocator(x, distortions, curve='convex', direction='decreasing')
k = kn.elbow

if k is None:
    k = int(input("You need to enter the number of clusters because the code couldn't predict it: "))

print("No. of clusters: ", str(k))
centroids, _ = kmeans(X, k)
cluster_indices, _ = vq(X, centroids)

cluster_labels = cluster_indices  # Store cluster labels

def make_all_cluster_folder():
    for i in range(k):
        clusterFolderName = "Cluster" + str(i)
        path = os.path.join(main_path, clusterFolderName)
        os.mkdir(path)

def get_target_folder(cluster_label_value):
    clusterFolderName = "Cluster" + str(cluster_label_value)
    target_folder = os.path.join(main_path, clusterFolderName)
    return target_folder

def paste_images_to_folder(original_folder):
    i = 0
    for filename in filenames:
        original_path = os.path.join(original_folder, filename)
        target_path = os.path.join(get_target_folder(cluster_labels[i]), filename)
        shutil.copyfile(original_path, target_path, follow_symlinks=True)
        i += 1

make_all_cluster_folder()
paste_images_to_folder(main_path)
