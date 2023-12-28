from dash import dcc,  html , callback, Dash , Output , Input
from dash.exceptions import PreventUpdate
external_style = ['']

app = Dash(__name__ , title='Prevent Update', external_stylesheets=external_style) 


app.layout  = html.Div([
     html.P('Clickez sur le bouton pour afficher') ,
    
    html.Button('Cliquez ici',id='button'),
    
    html.P(id='show')
]
)

@callback(
    Output(component_id='show', component_property='children'), 
    Input('button', component_property='n_clicks')
)

def show_content(clicks) :
    
    if clicks is None : 
        raise PreventUpdate
    else : 
        return 'Le texte s\'affiche au click du button'



if(__name__ == '__main__'): 
    app.run(debug=True)