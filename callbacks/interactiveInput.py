from dash import html, Dash, dcc , Input, callback, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6('Interactive input value'), 
    html.Div([
        "Input :", 
        dcc.Input(id="my-input", value='initial value', type='text')
    ]),


    html.Div(id='output')
])

@callback(
        Output(component_id='output', component_property='children'),
        Input(component_id='my-input', component_property='value')
)



def update_input_value(input) :
    return f'Output : {input}'

if __name__ == '__main__' :
    app.run(debug=True)