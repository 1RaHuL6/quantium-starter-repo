 
# app.py
import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('data/processed/output.csv')
df['date'] = pd.to_datetime(df['date']) 
df = df.sort_values('date')
df_north = df[df['region'] == 'north']
# Create base figure
# fig = px.line(
#     df,
#     x='date',
#     y='sales',
#     color='region',
#     title='Daily Sales of Pink Morsel',
#     labels={'date': 'Date', 'sales': 'Sales ($)'}
# )

# fig.update_layout(
#     shapes=[
#         dict(
#             type='line',
#             x0='2021-01-15',  
#             x1='2021-01-15',
#             y0=0,
#             y1=1,
#             yref='paper', 
#             line=dict(color='red', dash='dash'),
#         )
#     ],
#     annotations=[
#         dict(
#             x='2021-01-15',
#             y=1,
#             yref='paper',
#             xanchor='left',
#             yanchor='bottom',
#             text='Price Increase (Jan 15, 2021)',
#             showarrow=False,
#             font=dict(color='red')
#         )
#     ]
# )

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard", style={'textAlign': 'center', 'margin': '20px'}),
    
    html.Div([
        html.Label("Select Region:"),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            inline=True,
            style={'margin': '10px'}
        )
    ], style={'textAlign': 'center'}),
    
     dcc.Graph(id = 'sales-chart')     
])

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    daily_df = filtered_df.groupby(['date', 'region'])['sales'].sum().reset_index()
    
    fig = px.line(
        daily_df,
        x='date',
        y='sales',
        color='region',
        title='Pink Morsel Sales by Region',
        labels={'date': 'Date', 'sales': 'Sales ($)', 'region': 'Region'}
    )
    
    fig.add_vline(x='2021-01-15', line_dash='dash', line_color='red')
    
    return fig


if __name__ == '__main__':
    app.run(debug=True)