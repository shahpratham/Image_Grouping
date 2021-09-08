# Image_Grouping

## What are Features?

A feature is a piece of information about the content of an image; typically about whether a certain region of the image has certain properties. Features may be specific structures in the image such as points, edges or objects.

## Types of Features

- **Edges**: Edges are points where there is a boundary between two image regions. Edges are usually defined as sets of points in the image which have a strong gradient magnitude.

- **Corners / interest points**- It refer to point-like features in an image, which have a local two dimensional structure. It was then noticed that the so-called corners were also being detected on parts of the image which were not corners in the traditional sense (for instance a small bright spot on a dark background may be detected). These points are frequently known as interest points

- **Blobs / regions of interest points**: Blobs provide a complementary description of image structures in terms of regions, as opposed to corners that are more point-like. Blob detectors can detect areas in an image which are too smooth to be detected by a corner detector.

- **Ridges**: Ridges are formed with the points where the intensity gray level reaches a local extremum in a given direction. A ridge can be thought of as a one-dimensional curve that represents an axis of symmetry, and in addition has an attribute of local ridge width associated with each ridge point. Ridge descriptors are frequently used for road extraction in aerial images and for extracting blood vessels in medical images
