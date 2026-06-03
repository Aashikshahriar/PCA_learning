import numpy as np


def generate_correlated_data(
    n_samples,
    correlation,
    noise=0.2,
    seed=42
):
    np.random.seed(seed)

    x = np.random.normal(size=n_samples)

    y = (
        correlation * x
        + np.sqrt(1 - correlation**2)
        * np.random.normal(size=n_samples)
    )

    y += noise * np.random.normal(size=n_samples)

    return np.column_stack((x, y))