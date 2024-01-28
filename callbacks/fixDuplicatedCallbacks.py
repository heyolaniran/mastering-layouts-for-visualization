from dash import Dash , dcc,  callback_context , html , callback, Input , Output
import plotly_express as px 
import pandas


app = Dash(__name__); 


app.layout = html.Div([

    html.Button('Dessiner le graphe', id='draw_graph'), 
    html.Button('Nettoyer le graphe', id='reset_graph'), 

    dcc.Graph(id="graph")
])