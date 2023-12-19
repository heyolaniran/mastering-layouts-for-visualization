from dash import html, dcc, Dash


app=Dash(__name__)

app.layout=html.Div([
    #Dropdown Components 
    html.Div(children=[
        html.Label('Dropdown'), 
        dcc.Dropdown(['Cotonou', 'Abomey-Calavi', 'Parakou'], 'Parakou', id='dropdown'), 

        html.Br(), 

        html.Label("Multiple DropDown", style={'textAlign': 'center', 'marginBottom': '2px'}), 
        dcc.Dropdown(['Cotonou', 'Abomey-Calavi', 'Parakou'],[], id='multi-dropdown',multi=True)
    ]),


    #Radio Items 
    html.Div(children=[
        html.Label('Radio Items'), 
        dcc.RadioItems(['Cotonou', 'Abomey-Calavi', 'Parakou'], 'Cotonou' , id="radio_item")
    ], style={'flex': 10 , 'padding': 20})

])


if __name__ == '__main__': 
    app.run(debug=True)