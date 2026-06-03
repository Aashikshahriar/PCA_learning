import numpy as np
import plotly.graph_objects as go


def covariance_ellipse(X, eigenvalues, eigenvectors):

    theta = np.linspace(0, 2*np.pi, 200)

    circle = np.array([
        np.cos(theta),
        np.sin(theta)
    ])

    ellipse = (
        eigenvectors
        @ np.diag(np.sqrt(eigenvalues))
        @ circle
    )

    fig = go.Figure()

    fig.add_scatter(
        x=X[:,0],
        y=X[:,1],
        mode="markers",
        name="Data"
    )

    fig.add_scatter(
        x=ellipse[0],
        y=ellipse[1],
        mode="lines",
        line=dict(width=4),
        name="Covariance Ellipse"
    )

    fig.update_layout(
        title="Covariance Ellipse",
        template="plotly_dark"
    )

    return fig