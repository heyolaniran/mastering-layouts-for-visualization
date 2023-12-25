from dash import Dash , html, callback , Output , Input , dcc
import plotly_express as px 
import pandas 

# Externals resources to use 

external_style = ['']

file_souce = 'https://plotly.github.io/datasets/country_indicators.csv' 

#Declare app 

app = Dash(name=__name__ , external_stylesheets=external_style , title='Life Expectancy Study')

dataframe = pandas.read_csv(file_souce)

# App layout definition 
app.layout = html.Div([
    
    html.Div([
        
        html.Div([
            
            # Scatter plot dropdown
            dcc.Dropdown(
                dataframe['Indicator Name'].unique(), 
                'Fertility rate, total (births per woman)', 
                id='crossfilter-xaxis-column' 
            ) , 
            
            #Radio Items for scatter plot for first  display 
            
            dcc.RadioItems(
                ['linear', 'log'], 
                'linear', 
                id='crossfilter-xaxis-type', 
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            )

        ], style={'width' : '49%', 'display': 'inline-block'}), 
        
       
        
        html.Div(children=[
            
             #  dropdown for second   plot 
            dcc.Dropdown(
                dataframe['Indicator Name'].unique() , 
                'Life expectancy at birth, total (years)', 
                id='crossfilter-yaxis-column'
            ) , 
            
             #  Radio Items for second   plot 
            dcc.RadioItems(
                ['linear','radio'], 
                'linear', 
                id='crossfilter-yaxis-type', 
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            )
            
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
        
    ], style={'padding' : '10px 5px' }), 
    
    # Represent first plot 
    
    html.Div([
         dcc.Graph(
             id='crossfilter-indicator-scatter', 
             hoverData={'points' : [{'customdata' : 'Benin'}]}
         )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    
    html.Div([
        dcc.Graph(id='x-time-series'), 
        dcc.Graph(id='y-time-series')
    ], style={'display' : 'inline-block', 'width' : '49%'}), 
    
    html.Div([
        dcc.Slider(
            min=dataframe['Year'].min(), 
            max=dataframe['Year'].max(), 
            value=dataframe['Year'].max(), 
            step=None, 
            id='crossfilter-year--slider', 
            marks={str(year) : str(year) for year in dataframe['Year'].unique()}
        )
    ],  style={'width': '49%', 'padding': '0px 20px 20px 20px'})
])


if(__name__ == '__main__') : 
    app.run(debug=True)