import numpy as np
import plotly.express as px


def generate_3d_data(
    n=500,
    seed=42
):

    np.random.seed(seed)

    x = np.random.normal(size=n)

    y = 0.8*x + np.random.normal(size=n)*0.3

    z = (
        0.5*x
        + 0.5*y
        + np.random.normal(size=n)*0.2
    )

    return np.column_stack(
        [x,y,z]
    )


def plot_3d(X):

    fig = px.scatter_3d(
        x=X[:,0],
        y=X[:,1],
        z=X[:,2]
    )

    fig.update_layout(
        template="plotly_dark",
        title="3D Dataset"
    )

    return fig