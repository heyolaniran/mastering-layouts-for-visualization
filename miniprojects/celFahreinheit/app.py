from dash import Dash , html , dcc , callback , Output , Input, ctx 


styles = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, title='Temperature Converter', external_stylesheets=styles)


app.layout = html.Div([
    
    dcc.Input(
        id='celcius', 
        type='number',
        min=0, 
    ) , 
    
    dcc.Input(
        id='fahrenheit', 
        min=0,
        type='number',
     
    )
])

@callback(
    Output('celcius', 'value'), 
    Output('fahrenheit', 'value'), 
    Input('celcius', 'value'), 
    Input('fahrenheit', 'value'), 
    prevent_initial_call=True
)

def swap(celcius, fahrenheit) : 
    triggered_id = ctx.triggered[0]['prop_id'].split(".")[0]
    value = 0 
    converted = 0
    if triggered_id == 'celcius' : 
        value = celcius 
        converted = (int(celcius) * 9/5 ) + 32
    else :
        value = 5/9 * (int(fahrenheit) - 32) 
        converted = fahrenheit
    return value , converted


if __name__ == '__main__' : 
    app.run(debug=True)