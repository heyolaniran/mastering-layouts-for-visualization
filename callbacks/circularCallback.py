from dash import Dash , callback , ctx , Output, Input , html , dcc

styles =[''] 

app = Dash(__name__, external_stylesheets=styles) 


app.layout = html.Div([
    
    dcc.Slider(
        id='slider', 
        min=0 , 
        max=20 , 
        marks = { i : str(i) for i in range(21)}, 
        value=5
    ), 
    html.Div([
        dcc.Input(id='input',  type='number', min=0, max=20, value=5)
    ])
    
])


@callback(
    Output('slider', 'value'), 
    Output('input', 'value'), 
    Input('slider', 'value'), 
    Input('input', 'value')
)

def circluar_callback(slider , input) : 
    triggered_id = ctx.triggered[0]['prop_id'].split(".")[0]
    
    value = slider if triggered_id == 'slider' else input 
    return value , value

if __name__ == '__main__' : 
    app.run(debug=True)