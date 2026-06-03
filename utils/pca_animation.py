import numpy as np
import plotly.graph_objects as go


def animate_pca_rotation(
    X,
    eigenvectors
):

    frames = []

    target_angle = np.arctan2(
        eigenvectors[1,0],
        eigenvectors[0,0]
    )

    for angle in np.linspace(
        0,
        target_angle,
        40
    ):

        R = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle),  np.cos(angle)]
        ])

        rotated = X @ R.T

        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=rotated[:,0],
                        y=rotated[:,1],
                        mode="markers"
                    )
                ]
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=X[:,0],
                y=X[:,1],
                mode="markers"
            )
        ],
        frames=frames
    )

    fig.update_layout(
        template="plotly_dark",
        title="Animated PCA Rotation",
        updatemenus=[
            {
                "buttons":[
                    {
                        "label":"Play",
                        "method":"animate",
                        "args":[None]
                    }
                ]
            }
        ]
    )

    return fig