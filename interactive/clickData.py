from dash import callback , Output , Input, html , dcc
from graph import app , styles , fig
import json

app.layout = html.Div([
    
    dcc.Graph(
        id="basic-interaction" , 
        figure=fig
    ) , 
    
    html.Div([
        
        dcc.Markdown("""
                     
                     **Click on Data to display details 
                     
                     Click Data basic interaction with plotly 
                     """) , 
        
        html.Div(className='row' , style={'textAlign' : 'center'}, children=[
            
             html.Pre(id='click_data', style=styles['pre'])
        ])
    ])
])

@callback(
    Output('click_data', 'children'), 
    Input('basic-interaction', 'clickData')
)

def update_click_data(clickData) : 
    return json.dumps(clickData)


if __name__  == '__main__' :
    app.run(debug=True)