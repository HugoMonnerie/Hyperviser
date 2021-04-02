import requests
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px


def fetchAllData():
    data = requests.get('http://localhost:5000/')
    print(data.json())
    return data.json()


def fetchCpu():
    data = requests.get('http://localhost:5000/cpu')
    print(data.json())
    return data.json()


def fetchRam():
    data = requests.get('http://localhost:5000/ram**')
    print(data.json())
    return data.json()


# Initialise the app
app = dash.Dash(__name__)

# Define the app
app.layout = html.Div()


app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                   # Define the left element
                                   html.Div(
                                       className='four columns div-user-controls'),
                                   # Define the right element
                                   html.Div(
                                       className='eight columns div-for-charts bg-grey')
                               ])
                      ])

children = [
    html.H2('Dash - STOCK PRICES'),
    html.P('''Visualising time series with Plotly - Dash'''),
    html.P('''Pick one or more stocks from the dropdown below.''')
]
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
