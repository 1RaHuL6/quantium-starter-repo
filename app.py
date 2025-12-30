# import dash
# from dash import html,dcc
# import pandas as pd
# import plotly.express as px 

# df = pd.read_csv('data/processed/output.csv')
# df['date'] = pd.to_datetime(df['date'], dayfirst=False)  

# df = df.sort_values('date')
# daily_sales = df.groupby('date')['sales'].sum().reset_index()

# fig = px.line(
#     daily_sales,x='date', y = 'sales', title='Daily sales of Pink Morsels',
#     labels = {'date': 'Date', 'sales': 'Sales ($)'}
# )

# fig.add_vline(
#     x = datetime.date(2021, 1, 15),
#     line_dash = 'dash',
#     line_color = 'red',
#     annotation_text = 'Price Increase (Jan 15, 2021)',
#     annotation_position = 'top right'
# )

# app = dash.Dash(__name__)

# app.layout= html.Div([
#     html.H1("Pink Morsel Sales Dashboard", 
#             style= {'textAlign': 'center', 'margin': '20px'}),
#     dcc.Graph(figure=fig)
    
# ])

# if __name__ == '__main__':
#     app.run(debug=True)
    
    
    
# app.py
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('data/processed/output.csv')
df['date'] = pd.to_datetime(df['date'])  # Ensure datetime
df = df.sort_values('date')
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Create base figure
fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Daily Sales of Pink Morsel',
    labels={'date': 'Date', 'sales': 'Sales ($)'}
)

# ✅ SAFE METHOD: Add vertical line using 'shapes'
fig.update_layout(
    shapes=[
        dict(
            type='line',
            x0='2021-01-15',  # Can be string if x-axis is date strings
            x1='2021-01-15',
            y0=0,
            y1=1,
            yref='paper',  # Use full y-axis (0 to 1 in paper coordinates)
            line=dict(color='red', dash='dash'),
        )
    ],
    annotations=[
        dict(
            x='2021-01-15',
            y=1,
            yref='paper',
            xanchor='left',
            yanchor='bottom',
            text='Price Increase (Jan 15, 2021)',
            showarrow=False,
            font=dict(color='red')
        )
    ]
)

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard", style={'textAlign': 'center', 'margin': '20px'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)