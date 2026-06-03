import numpy as np
import plotly.graph_objects as go


def scree_plot(explained):

    cumulative = np.cumsum(explained)

    fig = go.Figure()

    fig.add_bar(
        x=[
            f"PC{i+1}"
            for i in range(len(explained))
        ],
        y=explained,
        name="Individual"
    )

    fig.add_scatter(
        x=[
            f"PC{i+1}"
            for i in range(len(explained))
        ],
        y=cumulative,
        mode="lines+markers",
        name="Cumulative"
    )

    fig.update_layout(
        title="Scree Plot",
        template="plotly_dark"
    )

    return fig