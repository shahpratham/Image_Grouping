# Image_Grouping

# ORB Research paper Analysis

## Some basic content 

Problem at hand : Feature detection & matching

What are the fundamental steps ?
	1. Feature Detection
	2. Feature Description (using feature descriptor vector ..more on that later)
	3. Feature  matching

What are features ?

A feature is a piece of information which is relevant for solving the computational task related to a certain application.

In machine learning and pattern recognition, a feature is an individual measurable property or characteristic of a phenomenon

ORB performs as well as SIFT on the task of feature detection (and is better than SURF) while being almost two orders of magnitude faster. ORB builds on the well-known FAST keypoint detector and the BRIEF descriptor. Both of these techniques are attractive because of their good performance and low cost. 
ORB’s main contributions are as follows:

The addition of a fast and accurate orientation component to FAST

The efficient computation of oriented BRIEF features

Analysis of variance and correlation of oriented BRIEF features

A learning method for decorrelating BRIEF features under rotational invariance, leading to better performance in nearest-neighbor applications.