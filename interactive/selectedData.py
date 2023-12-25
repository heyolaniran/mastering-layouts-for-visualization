from graph import app ,  styles , fig 

from dash import dcc , html , callback , Input , Output 
import json 


app.layout = html.Div([
    
    #Represents the graph 
    
    dcc.Graph(
        id='basic_interactions', 
        figure=fig
    ) , 
    
    html.Div([
        
        
        dcc.Markdown("""
                     
                     
                     **Select Data Interaction** \n
                     **Select Region with rectangle tool in the graph menu to display specific information**
                     
                     """), 
        
        html.Div(className='row' , style={'textAlign': 'center' , 'width' : '55%'}, children=[
            
            html.Pre(id='selected_data', style=styles['pre'])
        ])
        
    ])
])

#Define call backs interactions 

@callback(
    Output(component_id='selected_data', component_property='children'), 
    Input(component_id='basic_interactions', component_property='selectedData')
)

def update_selected_data(selectedData) : 
    return json.dumps(selectedData)


if(__name__ == '__main__') :
    app.run(debug=True)