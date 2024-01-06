from dash import Dash, html, callback , Output , Input , Patch, dcc



app = Dash(__name__, title="Pattern Matching")

options = ["NYC", "MTL", "LA", "TOKYO"]

app.layout = html.Div([

    html.Button(id="add_filter", title='Ajouter un filtre', n_clicks=0), 

    html.Div(children=[] , id="filter_zone"), 

    html.Div(children=[], id="outputContent")
])


callback(
    Output('filter_zone', 'children'), 
    Input('add_filter', 'n_clicks')
)

def filter_field (nClicks) : 
    patched_children = Patch()

    new_filter = dcc.Dropdown(id={'type' : 'city_filter' , 'index': nClicks}, options=options)

    patched_children(new_filter); 
    return patched_children ; 