import dash
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from scripts.int_api import get_data

df = get_data()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Analyser la consommation éléctrique française en temps réel !')
])

if __name__ == '__main__':
    app.run(debug=True)
