import json 
from dash import html , callback , Input , Output , dcc
from graph import fig, app, styles


app.layout = html.Div([
     
     dcc.Graph(
         id='basic-interactions', 
         figure = fig
     ) , 
     
     html.Div( className='row', children = [
         html.Div([
             dcc.Markdown("""
                          
                          **Hover Data** 
                          Survolez la donnée pour récupérer les informations relatives
                          
                          """), 
             
             html.Pre(id='hover_data', style=styles['pre']) 
         ])
     ])
     
])


@callback(
    Output(component_id='hover_data', component_property='children'), 
    Input('basic-interactions', 'hoverData')
)

def update_hover_data(hoverData) :
    return json.dumps(hoverData)



if __name__ == '__main__' : 
    app.run(debug=True)