from dash import Dash, html, dcc
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

def transform_data(df):
    """
    Groups and sorts data by date
    Returns:
        out_df: dataframe
    """

    out_df = df.copy()

    # Groups data by date and sums the sale on each grouped date
    out_df = out_df.groupby('date')['sales'].sum().reset_index()

    # Sorts the data based on date
    out_df = out_df.sort_values(by=['date'], ascending=True)
    return out_df

def create_app(df, app):
    """
    Create dash app
    """
    fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales")
    app.layout = html.Div(children=[
        html.H1(children='Soul Foods'),

        html.Div(children='''
            Soul Foods Sales Data
        '''),

        dcc.Graph(
            id='pink_morsel_total_sales',
            figure=fig
        )
    ])


def main():
    app = Dash(__name__)
    df = read_csv()
    df = transform_data(df)
    create_app(df, app)
    app.run(debug=True)


if __name__ == '__main__':
    main()