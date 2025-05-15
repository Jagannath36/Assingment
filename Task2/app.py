import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the dataset
df = pd.read_csv('C:\\Users\\hp\\Downloads\\archive (8)\\sales.csv')
df = df.dropna(subset=['Year'])  # Remove rows with NaN years
df['Year'] = df['Year'].astype(int)

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div(style={'backgroundColor': 'white', 'padding': '20px'}, children=[
    html.H1("Sales Dashboard", style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='genre-filter',
        options=[{'label': genre, 'value': genre} for genre in df['Genre'].unique()],
        value=df['Genre'].unique()[0],
        style={'width': '50%', 'margin': '20px auto'}
    ),

    dcc.Graph(id='bar_chart'),
    dcc.Graph(id='pie_chart'),
    dcc.Graph(id='global_sales_prediction'),
    dcc.Graph(id='eu_sales_prediction')
])

# Callbacks for visuals
@app.callback(
    [Output('bar_chart', 'figure'),
     Output('pie_chart', 'figure'),
     Output('global_sales_prediction', 'figure'),
     Output('eu_sales_prediction', 'figure')],
    [Input('genre-filter', 'value')]
)
def update_charts(selected_genre):
    filtered_df = df[df['Genre'] == selected_genre]

    # Chart 1: Bar Chart of Publisher vs NA_Sales
    bar_data = filtered_df.groupby('Publisher')['NA_Sales'].sum().sort_values(ascending=False).head(10)
    bar_fig = go.Figure(data=[
        go.Bar(x=bar_data.index, y=bar_data.values, marker_color='darkblue')
    ])
    bar_fig.update_layout(
        title='Top 10 Publishers by NA Sales',
        xaxis_title='Publisher',
        yaxis_title='NA Sales (millions)',
        plot_bgcolor='white'
    )

      # 2. Pie chart: % of total records by genre (based on count)
    genre_counts = df['Genre'].value_counts()
    pie_fig = go.Figure(data=[go.Pie(
        labels=genre_counts.index,
        values=genre_counts.values,
        hole=0.3
    )])
    pie_fig.update_layout(
        title="Genre Distribution (% of Total Records)"
    )


    # Chart 3: Predict Global_Sales for next 2 years (Regression)
    yearly_sales = df.groupby('Year')['Global_Sales'].sum().reset_index()
    X = yearly_sales[['Year']]
    y = yearly_sales['Global_Sales']
    model = LinearRegression()
    model.fit(X, y)
    future_years = np.array([[2023], [2024]])


    predictions = model.predict(future_years)

    reg_fig = go.Figure()
    reg_fig.add_trace(go.Scatter(x=yearly_sales['Year'], y=y, mode='markers', name='Actual', marker=dict(color='gray')))
    reg_fig.add_trace(go.Scatter(x=yearly_sales['Year'], y=model.predict(X), mode='lines', name='Trend', line=dict(color='green')))
    reg_fig.add_trace(go.Bar(x=[2023, 2024], y=predictions, name='Predictions', marker_color='orange'))

    reg_fig.update_layout(
        title='Global Sales Prediction for Next 2 Years',
        xaxis_title='Year',
        yaxis_title='Global Sales',
        plot_bgcolor='white'
    )



    # Chart 4: Predict EU_Sales for next 1 year
    yearly_eu_sales = df.groupby('Year')['EU_Sales'].sum().reset_index()
    Xe = yearly_eu_sales[['Year']]
    ye = yearly_eu_sales['EU_Sales']
    model_eu = LinearRegression()
    model_eu.fit(Xe, ye)
    eu_pred = model_eu.predict(np.array([[2023]]))

    eu_fig = go.Figure()
    eu_fig.add_trace(go.Scatter(x=yearly_eu_sales['Year'], y=ye, mode='markers', name='Actual', marker=dict(color='purple')))
    eu_fig.add_trace(go.Scatter(x=yearly_eu_sales['Year'], y=model_eu.predict(Xe), mode='lines', name='Trend', line=dict(color='blue')))
    eu_fig.add_trace(go.Bar(x=[2023], y=eu_pred, name='Prediction', marker_color='red'))

    eu_fig.update_layout(
        title='EU Sales Prediction for Next Year',
        xaxis_title='Year',
        yaxis_title='EU Sales',
        plot_bgcolor='white'
    )

    return bar_fig, pie_fig, reg_fig, eu_fig

# Run server
if __name__ == '__main__':
    app.run(debug=True)
