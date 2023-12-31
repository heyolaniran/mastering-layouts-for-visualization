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
    ], style={'flex': 10 , 'padding': 20}), 

    #CheckBox 

    html.Div(children=[
        html.Label('CheckBoxes'), 
        dcc.Checklist(['Cotonou', 'Abomey-Calavi', 'Parakou'], ['Parakou', 'Abomey-Calavi'], id="check_box")
    ], style={'padding': 5}), 


    #Range Slider 
    html.Div(children=[
        html.Label('Range'), 
        dcc.Slider(
            min=0, 
            max=9, 
            marks={i: f'Label {i}'if i== 1 else str(i) for i in range(0,9) }, 
            value=4
        )
    ], style={'flex':5 , 'padding':5})

])


if __name__ == '__main__': 
    app.run(debug=True)