from  dash import Dash, html, callback , Output, Input , dcc , clientside_callback
import json 
import pandas 


style = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] 

app = Dash(__name__, title='Country Indicators', external_stylesheets=style)

dataframe = pandas.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

indicators = {
    'pop' : 'Population', 
    'lifeExp' : 'Life Expectancy', 
    'gdpPercap' : 'GDP per Capita'
}

available_countries = dataframe['country'].unique()



app.layout = html.Div(children=[

    html.Div([
        dcc.Graph(
            id='graph'
        )
    ]), 

    dcc.Store(id="graph_data_store",
              data=[{
                  'x': dataframe[dataframe['country'] == 'Benin']['year'], 
                  'y' : dataframe[dataframe['country'] == 'Benin']['pop']
              }]
              ), 

    html.P('Indicateur') , 

    dcc.Dropdown(indicators, 'pop', id="indicator"), 

    html.P('Country'),

    dcc.Dropdown(available_countries, 'Benin', id="country"),

    html.P('Graph Scale'), 

    dcc.RadioItems(
        ['linear', 'log'], 
        'linear', 
        id='graph_scale'
    ), 

    html.Hr() , 

    html.Div([
        html.Details([
            html.Summary('Content of figure storage'), 

            dcc.Markdown(
               id='clientside_df_json'
            )
        ]) , 

    ])




])

@callback(
    Output(component_id='graph_data_store', component_property='data'), 
    Input(component_id='indicator', component_property='value'), 
    Input(component_id='country', component_property='value')
)

# Update rendered data storage in dcc.Store 

def update_graph_store(indicator , country) : 

    dff = dataframe[dataframe['country'] == country] 


    return [{
        'x' : dff['year'], 
        'y' : dff[indicator], 
        'mode' : 'markers'
    }]

# JS function to run some callback without calling backend server and drawing the Graph

clientside_callback(
    """
    function(data, scale) {
        return {
            'data' : data , 
            'layout' : {
                'yaxis' : {'type' : scale}
            }
        }
    }
    """ , 
    Output(component_id='graph', component_property='figure'), 
    Input(component_id='graph_data_store', component_property='data'), 
    Input(component_id='graph_scale', component_property='value')
)


# Generate Json format of current country indicator scaling 

@callback(
    Output(component_id='clientside_df_json', component_property='children'), 
    Input(component_id='graph_data_store', component_property='data')
)

def generate_json(data): 
    return '```\n'+json.dumps(data)+'\n```'



if __name__ == '__main__' : 
    app.run(debug=False)