# IMAGE_GROUPING

Segregates images using feature extraction and Clustering algorithm

## Table of Contents

- [About the Project](#about-the-project)
    - [Tech Stack](#tech-stack)
    - [File Structure](#file-structure)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [Results and Demo](#results)
- [Future Work](#to-dos)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [Acknowledgements and Resources](#acknowledgements-and-resources)
- [License](#license)

## About The Project

https://user-images.githubusercontent.com/82367556/137674015-5a2f7481-c7fd-40ba-8719-b2d03f582475.mp4

## Tech Stack

- OpenCV
- Scikit Learn

### Prerequisites

- Should have python environment. You can refer [here](https://www.tutorialspoint.com/python/python_environment.htm) for the setup.
- Python librairies
    - OpenCV `pip install opencv-python`
    - Scikit `pip install scikit-learn`
    - numpy `pip install numpy`

For installation of pip you can refer [here](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)

- Must have Test Data, or you can get it from [here](https://drive.google.com/file/d/1wu7fiQ0NtBH5s2wu4JrZEnFjwblHCOlX/view?usp=sharing).

### Installation

1.  Clone the repo
    
    ```git
    git clone https://github.com/shahpratham/Image_Grouping.git
    ```
    

### Usage

```bash
cd /path/to/Image_Grouping
```

> For using Sklearn K-means use this, similar can be done openCV code

```python
python kmeansUsingSkLearn.py
```

> For viewing Cluster Directory

```
cd /path/to/TestDAta
```

## Results

|     |     |
| --- | --- |
| Task | Time Taken (in seconds) |
| Pre-processing | 8.906 |
| Feature Extraction | 49.37 |
| Clustering | 1.216 |
| Creating Directories and pasting images | 0.8 |

> Did this for 100 images and tested on Lenovo Legion 5(Ryzen 5 4600H) and got accuracy close to 80%. 

## To Dos

- [ ] Improving accuracy
- [ ] Finding optimum of K
- [ ] Make a web app where one can upload images and can cluster it online.
