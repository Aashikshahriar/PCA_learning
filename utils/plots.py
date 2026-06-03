import plotly.express as px
import plotly.graph_objects as go


def scatter_plot(
    X,
    title
):

    fig = px.scatter(
        x=X[:, 0],
        y=X[:, 1],
        title=title
    )

    return fig


def covariance_heatmap(cov):

    fig = go.Figure(
        data=go.Heatmap(
            z=cov
        )
    )

    fig.update_layout(
        title="Covariance Heatmap"
    )

    return fig


def variance_bar_chart(explained):

    fig = go.Figure()

    fig.add_bar(
        x=[
            f"PC{i+1}"
            for i in range(len(explained))
        ],
        y=explained
    )

    fig.update_layout(
        title="Explained Variance (%)"
    )

    return fig


def projection_plot(projected):

    fig = px.scatter(
        x=projected[:, 0],
        y=projected[:, 1],
        title="PCA Projection"
    )

    return fig