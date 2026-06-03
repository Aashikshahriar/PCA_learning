import streamlit as st
import numpy as np
import plotly.graph_objects as go

from utils.generator import generate_correlated_data

from utils.pca_math import (
center_data,
covariance_matrix,
eigen_decomposition,
project_data,
explained_variance,
reconstruct_data,
reconstruction_error
)

from utils.plots import (
scatter_plot,
covariance_heatmap,
projection_plot
)

from utils.covariance_ellipse import covariance_ellipse
from utils.pca_animation import animate_pca_rotation
from utils.scree_plot import scree_plot
from utils.pca_3d import generate_3d_data, plot_3d
from utils.step_mode import show_step

# ==================================================

# PAGE CONFIG

# ==================================================

st.set_page_config(
page_title="PCA Learning Dashboard",
layout="wide"
)

# ==================================================

# MINIMAL DARK THEME

# ==================================================

st.markdown("""
<style>

/* Main App Background */
.stApp {
    background-color: white;
    color: black;
}

/* Main content */
.main {
    background-color: white;
}

/* Headers */
h1, h2, h3 {
    color: black !important;
}

/* Text */
p, div, span, label {
    color: black !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f5f5f5;
}

section[data-testid="stSidebar"] * {
    color: black !important;
}

/* Metrics */
[data-testid="metric-container"] {
    background: white;
    border: 1px solid #dcdcdc;
    border-radius: 12px;
    padding: 12px;
}

[data-testid="metric-container"] label {
    color: #666666 !important;
}

[data-testid="metric-container"] div {
    color: black !important;
    font-weight: 700 !important;
}

/* Dataframes */
[data-testid="stDataFrame"] {
    background-color: white;
}

/* Alerts */
.stAlert {
    background-color: #f8f9fa;
    color: black;
}

</style>
""", unsafe_allow_html=True)

# ==================================================

# HELPERS

# ==================================================

def apply_theme(fig):

    fig.update_layout(
        template="plotly_white",

        paper_bgcolor="white",
        plot_bgcolor="white",

        font=dict(
            color="black",
            size=14
        ),

        xaxis=dict(
            gridcolor="#dcdcdc",
            zerolinecolor="#dcdcdc"
        ),

        yaxis=dict(
            gridcolor="#dcdcdc",
            zerolinecolor="#dcdcdc"
        )
    )

    return fig

# ==================================================

# TITLE

# ==================================================

st.title("Principal Component Analysis Explorer")

st.caption(
"Interactive visualization of covariance, eigenvectors, variance, projection and reconstruction."
)

# ==================================================

# SIDEBAR

# ==================================================

st.sidebar.header("Controls")

samples = st.sidebar.slider(
"Samples",
50,
1000,
300
)

correlation = st.sidebar.slider(
"Correlation",
0.0,
0.99,
0.80
)

noise = st.sidebar.slider(
"Noise",
0.0,
2.0,
0.20
)

seed = st.sidebar.number_input(
"Random Seed",
value=42
)

components = st.sidebar.slider(
"Components Kept",
1,
2,
1
)

step = st.sidebar.slider(
"PCA Step",
1,
8,
1
)

# ==================================================

# STEP DESCRIPTION

# ==================================================

show_step(step)

# ==================================================

# GENERATE DATA

# ==================================================

X = generate_correlated_data(
samples,
correlation,
noise,
seed
)

X_centered, mean = center_data(X)

cov = covariance_matrix(X_centered)

eigenvalues, eigenvectors = (
eigen_decomposition(cov)
)

projected = project_data(
X_centered,
eigenvectors
)

explained = explained_variance(
eigenvalues
)

reconstructed = reconstruct_data(
projected,
eigenvectors,
components
)

error = reconstruction_error(
X_centered,
reconstructed
)

# ==================================================

# SUMMARY

# ==================================================

st.subheader("Dataset Summary")

m1, m2, m3, m4 = st.columns(4)

m1.metric(
"Samples",
samples
)

m2.metric(
"Correlation",
f"{correlation:.2f}"
)

m3.metric(
"Noise",
f"{noise:.2f}"
)

m4.metric(
"Reconstruction Error",
f"{error:.5f}"
)

# ==================================================

# ORIGINAL DATA

# ==================================================

st.subheader("Original Data")

raw_fig = scatter_plot(
X,
"Original Dataset"
)

raw_fig = apply_theme(raw_fig)

st.plotly_chart(
raw_fig,
use_container_width=True
)

# ==================================================

# COVARIANCE ELLIPSE

# ==================================================

st.subheader("Covariance Ellipse")

ellipse_fig = covariance_ellipse(
X_centered,
eigenvalues,
eigenvectors
)

ellipse_fig = apply_theme(
ellipse_fig
)

st.plotly_chart(
ellipse_fig,
use_container_width=True
)

# ==================================================

# COVARIANCE MATRIX

# ==================================================

st.subheader("Covariance Matrix")

c1, c2 = st.columns([1, 2])

with c1:
    st.dataframe(cov)

with c2:

    heatmap = covariance_heatmap(
    cov
)

heatmap = apply_theme(
    heatmap
)

st.plotly_chart(
    heatmap,
    use_container_width=True
)

# ==================================================

# EIGENVALUES

# ==================================================

st.subheader("Eigenvalues")

e1, e2 = st.columns(2)

e1.metric(
"λ₁",
f"{eigenvalues[0]:.4f}"
)

e2.metric(
"λ₂",
f"{eigenvalues[1]:.4f}"
)

# ==================================================

# EIGENVECTORS

# ==================================================

st.subheader("Eigenvectors")

st.dataframe(
eigenvectors
)

# ==================================================

# PCA ROTATION ANIMATION

# ==================================================

st.subheader("Animated PCA Rotation")

rotation_fig = animate_pca_rotation(
X_centered,
eigenvectors
)

rotation_fig = apply_theme(
rotation_fig
)

st.plotly_chart(
rotation_fig,
use_container_width=True
)

# ==================================================

# PCA PROJECTION

# ==================================================

st.subheader("PCA Projection")

proj_fig = projection_plot(
projected
)

proj_fig = apply_theme(
proj_fig
)

st.plotly_chart(
proj_fig,
use_container_width=True
)

# ==================================================

# SCREE PLOT

# ==================================================

st.subheader("Scree Plot")

scree_fig = scree_plot(
explained
)

scree_fig = apply_theme(
scree_fig
)

st.plotly_chart(
scree_fig,
use_container_width=True
)

# ==================================================

# 3D PCA DEMO

# ==================================================

st.subheader("3D PCA Example")

X3 = generate_3d_data()

fig3d = plot_3d(
X3
)

fig3d = apply_theme(
fig3d
)

st.plotly_chart(
fig3d,
use_container_width=True
)

# ==================================================

# RECONSTRUCTION

# ==================================================

st.subheader("Reconstruction")

recon_fig = scatter_plot(
reconstructed,
"Reconstructed Dataset"
)

recon_fig = apply_theme(
recon_fig
)

st.plotly_chart(
recon_fig,
use_container_width=True
)

st.info(
f"Keeping {components} component(s) produces reconstruction error = {error:.6f}"
)
