from dash import Dash, html, callback , Output , Patch, Input , dcc, ALL


app = Dash(__name__, title="Pattern Matching", suppress_callback_exceptions=True)

options = ["NYC", "MTL", "LA", "TOKYO"]

app.layout = html.Div([

    html.Button( "Add Filter" , id="add_filter", n_clicks=0), 

    html.Div(children=[] , id="filter_zone"), 

    html.Div(children=[], id="outputContent")
])


@callback(
    Output('filter_zone', 'children'), 
    Input('add_filter', 'n_clicks')
)

def filter_field (nClicks) : 
    patched_children = Patch()
    new_filter = dcc.Dropdown(id={'type' : 'city_filter' , 'index': nClicks}, options=options)

    patched_children.append(new_filter); 
    return patched_children ; 


@callback(
        Output('outputContent', 'children'), 
        Input({'type' : 'city_filter' , 'index': ALL}, 'value')
)

def outputValue(values) :
     return html.Div(
        [html.Div(f"Dropdown {i + 1} = {value}") for (i, value) in enumerate(values)]
    )


if(__name__ == "__main__") : 
     app.run(debug=True)