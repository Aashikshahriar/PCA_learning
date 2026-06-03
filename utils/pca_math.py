import numpy as np


def center_data(X):

    mean = np.mean(X, axis=0)

    return X - mean, mean


def covariance_matrix(X):

    return np.cov(X.T)


def eigen_decomposition(cov):

    eigenvalues, eigenvectors = np.linalg.eig(cov)

    idx = np.argsort(eigenvalues)[::-1]

    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    return eigenvalues, eigenvectors


def project_data(X, eigenvectors):

    return X @ eigenvectors


def explained_variance(eigenvalues):

    return (
        eigenvalues /
        np.sum(eigenvalues)
    ) * 100


def reconstruct_data(
    projected,
    eigenvectors,
    n_components
):

    W = eigenvectors[:, :n_components]

    return projected[:, :n_components] @ W.T


def reconstruction_error(
    original,
    reconstructed
):

    return np.mean(
        (original - reconstructed) ** 2
    )