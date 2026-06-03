# PCA Learning

**Plug, Play, and Learn Principal Component Analysis (PCA) Interactively**

🌐 **Live Demo:**
https://pcalearning-madebyashik.streamlit.app/


## Overview

PCA Learning is an interactive dashboard built using **Python**, **Streamlit**, **NumPy**, and **Plotly** that helps users understand Principal Component Analysis (PCA) both visually and mathematically.

Instead of treating PCA as a black-box algorithm, this dashboard walks users through every stage of the dimensionality reduction process:

* Data Generation
* Mean Centering
* Covariance Matrix
* Eigenvalues
* Eigenvectors
* Principal Components
* PCA Projection
* Explained Variance
* Scree Plot
* Reconstruction Error
* 3D PCA Visualization


# What is PCA?

Principal Component Analysis (PCA) is a dimensionality reduction technique that transforms data into a new coordinate system.

The transformation is performed such that:

* The first principal component captures the maximum variance.
* The second principal component captures the maximum remaining variance.
* Each principal component is orthogonal to the others.

This allows high-dimensional datasets to be represented using fewer dimensions while retaining most of the information.

---

# Mathematical Foundation

## Step 1: Center the Data

Given a dataset

$$
X =
\begin{bmatrix}
x_1 \
x_2 \
\vdots \
x_n
\end{bmatrix}
$$

Then, subtract the mean vector

$$
\mu = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

from every observation:

$$
X_{\text{centered}} = X - \mu
$$

Centering ensures that the data has zero mean.

## Step 2: Compute the Covariance Matrix

The covariance matrix captures the relationships between variables:

$$
\Sigma
======

\frac{1}{n-1}
X^T X
$$

where

* (X) is the centered data matrix
* (\Sigma) is the covariance matrix

A large covariance indicates that two variables vary together.


## Step 3: Eigenvalue Decomposition

PCA computes the eigenvalues and eigenvectors of the covariance matrix.

$$
\Sigma v = \lambda v
$$

where

* (v) is an eigenvector
* (\lambda) is the corresponding eigenvalue

The eigenvectors determine the directions of the new coordinate system.

The eigenvalues determine the amount of variance captured along those directions.


## Step 4: Construct Principal Components

The eigenvalues are sorted in descending order:

$$
\lambda_1 \ge \lambda_2 \ge \lambda_3 \ge \cdots
$$

The corresponding eigenvectors become:

$$
PC_1, PC_2, PC_3, \ldots
$$

The first principal component captures the maximum variance.

## Step 5: Project the Data

The centered data is projected onto the new basis:

$$
Z = XV
$$

where

* (X) is the centered data
* (V) is the matrix of eigenvectors
* (Z) is the transformed PCA representation


# Explained Variance

The explained variance ratio of a principal component is

$$
\text{Explained Variance Ratio}
===============================

\frac{\lambda_i}
{\sum_{j=1}^{k}\lambda_j}
$$

This metric indicates how much information is retained by each component.

The dashboard visualizes this through:

* Explained Variance Charts
* Scree Plots
* Cumulative Variance Curves
* 
# Features

## Interactive Controls

Adjust:

* Number of Samples
* Correlation
* Noise
* Random Seed
* Components Retained

## Visualizations

* Original Dataset
* Centered Dataset
* Covariance Matrix
* Covariance Heatmap
* Covariance Ellipse
* Eigenvectors
* PCA Projection
* Scree Plot
* Animated PCA Rotation
* 3D PCA Demo
* Reconstruction Analysis


# Tech Stack

* Python
* Streamlit
* NumPy
* Plotly
* Scikit-Learn


# Installation

Clone the repository:

```bash
git clone https://github.com/Aashikshahriar/PCA_learning.git
```

Navigate to the project:

```bash
cd PCA_learning
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# Live Application

https://pcalearning-madebyashik.streamlit.app/

---

# Educational Goal

Most PCA tutorials focus on equations without intuition.

This project aims to bridge the gap between

$$
\text{Mathematical Understanding}
\quad \Longleftrightarrow \quad
\text{Visual Understanding}
$$

by allowing users to experiment with data and observe PCA in real time.

---

# Author

**Khondakar Ashik Shahriar**
**Dept of EEE, BUET**

