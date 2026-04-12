from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd


def read_csv(filename="../output/cleaned_daily_sales.csv"):
    """
    Converts csv file into dataframe

    Returns:
        dataframe: dataframe
    """
    df = pd.read_csv(filename)
    return df


def create_app(df, app):
    """
    Create dash app
    """
    # Fetch unique regions
    regions = sorted(df['region'].unique())
    # Create the region option labels
    region_options = [{'label': str(region).capitalize(), 'value': region} for region in regions]
    region_options = [{'label': "All", 'value': "All"}] + region_options

    app.layout = html.Div(className="app-container", children=[
        html.Div(className="card", children=[
            html.H1('Soul Foods', className="page-title"),

            html.Div(
                'Soul Foods Sales Data',
                className="page-subtitle"
            ),

            html.Label('Filter by Region:', className="filter-label"),

            dcc.RadioItems(
                id="region_selector",
                options=region_options,
                value="All",
                inline=True,
                className="radio-group"
            ),

            html.Div(
                dcc.Graph(id='pink_morsel_total_sales'),
                className="graph-container"
            )
        ])
    ])

    @app.callback(
        Output("pink_morsel_total_sales", "figure"),
        Input("region_selector", "value")
    )
    def update_graph(selected_region):
        color_map = {
            "north": "#5ad91a",
            "south": "#d62728",
            "east": "#2ca02c",
            "west": "#ff7f0e"
        }
        if selected_region == "All":
            filtered_df = df
            title = 'Pink Morsel Sales - All Regions'
        else:
            filtered_df = df[df['region'] == selected_region]
            title = 'Pink Morsel Sales - ' + selected_region.capitalize()

        fig = px.line(filtered_df, x="date", y="sales", title=title)
        fig.update_traces(line_color=color_map.get(selected_region, "#1f77b4"))

        fig.update_layout(
            template="plotly_white",
            margin=dict(l=20, r=20, t=50, b=20)
        )
        return fig

def build_app():
    app = Dash(__name__, assets_folder='../assets')
    df = read_csv()
    create_app(df, app)
    return app

if __name__ == '__main__':
    app = build_app()
    app.run(debug=True)
