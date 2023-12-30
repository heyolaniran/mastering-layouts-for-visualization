from dash import Dash , callback, Output, Input, ctx , html
from datetime import datetime
import time
app =  Dash(__name__, title='Indirect User Action')


app.layout = html.Div([
    
    html.Div([
        html.Button('Button 1 fast Execution', id='btn_1'), 
        html.Button('Button 2 Slow Execution', id='btn_2')

    ]) , 
    
    html.Div([
        
        html.Div( 'Not executed yet', id='output_1'), 
        html.Div( 'Not executed yet', id='output_2'), 
        html.Div( 'Not executed yet', id='output_3')
    ])
])

#fast interaction execution

@callback(
    Output(component_id='output_1', component_property='children'), 
    Input(component_id='btn_1', component_property='n_clicks')
)

def fast_exec(button) : 
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")
    button_id = ctx.triggered
    return '{} execute callback at {}'.format(button_id, current_time) 


@callback(
    Output(component_id='output_2', component_property='children'), 
    Input(component_id='btn_2', component_property='n_clicks')
)

def slow_exec(button) : 
    time.sleep(5)
    now = datetime.now()
    
    current_time = now.strftime("%H:%M:%S")
    
    button_id = ctx.triggered 
    return '{} execute callback at {}'.format(button_id, current_time)


@callback(
    Output(component_id='output_3', component_property='children'), 
    Input(component_id='output_2', component_property='children'), 
    Input(component_id='output_1', component_property='children')
)

def resume_exec(output2 , output1) : 
    time.sleep(10)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    return 'callback is executed at {}'.format(current_time)


if __name__ == '__main__' : 
    app.run(debug=True)