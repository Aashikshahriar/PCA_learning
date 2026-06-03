import streamlit as st


def show_step(step):

    descriptions = {

        1:
        "Generate correlated data",

        2:
        "Mean center the dataset",

        3:
        "Compute covariance matrix",

        4:
        "Find eigenvalues and eigenvectors",

        5:
        "Rotate to PCA basis",

        6:
        "Project data",

        7:
        "Compute explained variance",

        8:
        "Reconstruct data"
    }

    st.info(
        descriptions[step]
    )