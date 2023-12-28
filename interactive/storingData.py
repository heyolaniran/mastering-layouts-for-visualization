from dash import Dash , callback, html , Output, Input , dcc 
import json 
import pandas
app = Dash(__name__, title='Store data') 

app.layout = html.Div([
    
    html.Div(
        dcc.Graph(id='graph'), 
        html.Table(id='table'), 
        dcc.Dropdown(id='dropdown')
    ), 
    
    html.Div([
        dcc.Store(id='intermediate-data')
    ]), 
    
    
])

@callback(
    Output(component_id='intermediate-data', component_property='data'), 
    Input('dropdown', 'value')
)

def store_intermediate_value(value) : 
    
    # Dispatch global update into sharing data update to decrease high process ressource 
    clean_data = slow_process_step(value)
    
    
    # retrn cleaned data in correct format 
    return json.dumps(clean_data)

"""""
Update graph based on intermediate stored value 

"""""
@callback(
    Output(component_id='graph', component_property='figure'), 
    Input(component_id='intermediate-data', component_property='data')
)

def update_graph(cleanedData) :
    
    # Read cleaned data file source 
    dataframe = pandas.read_json(cleanedData, orient='split'), 
     
    #Process to create figure 
    figure = create_figure(dataframe) 
    
    return figure 

"""""
Update graph based on intermediate stored value 

"""""
@callback(
    Output(component_id='table', component_property='children'), 
    Input(component_id='intermediate-data', component_property='data')
)

def update_graph(cleanedData) :
    
    # Read cleaned data file source 
    dataframe = pandas.read_json(cleanedData, orient='split'), 
     
    #Process to create table 
    table = create_table(dataframe) 
    
    return table 