from dash import html , Dash , ctx , callback , Output , Input 
import json 


app = Dash(name=__name__, title='Triggered Actions') 


app.layout = html.Div(children=[
    
    html.Div([
         html.Button('Button 1',id='btn-1') , 
         html.Button('Button 2', id='btn-2') , 
         html.Button('Button 3',id='btn-3')
    ]), 
    
    html.Div(id='container') 
 
])

@callback(
    Output(component_id='container', component_property='children'), 
    Input(component_id='btn-1' , component_property='n_clicks'), 
    Input(component_id='btn-2' , component_property='n_clicks'), 
    Input(component_id='btn-3' , component_property='n_clicks'), 
)

def trigrrered_actions(btn1 , btn2, btn3) :
    
    button_id = ctx.triggered_id if not None else 'No click yet ' 
    
    result = json.dumps({
        'states' : ctx.states , 
        'triggered_id' : ctx.triggered, 
        'properties' : ctx.triggered_prop_ids , 
        'inputs' : ctx.inputs
    })
    return html.Div([
        html.Table([
              html.Tr([
                 html.Th('Button 1') , 
                html.Th('Button 2'), 
                html.Th('Button 3'), 
                html.Th('Last button clicked')
            ] 
            ) , 
            html.Tr([
                html.Td(btn1 or 0) , 
                html.Td(btn2 or 0), 
                html.Td(btn3 or 0) , 
                html.Td(button_id or '')
            ]
                
            )
        ]) , 
        
        html.Div([
            html.Pre(result)
        ])
        
    ])
    
    
if __name__ == '__main__' : 
  app.run(debug=True)