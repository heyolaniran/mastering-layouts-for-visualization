from dash import Dash , html, callback , Output , Input 
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
            
            #Radio Items for scatter plot display 
            
            Radio.Items(
                ['linear', 'log'], 
                'linear', 
                id='crossfilter-xaxis-type', 
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            )

        ], style={'width' : '49%', 'display': 'inline-block'}), 
        
        # Div element for second plot 
        
        html.Div(children=[
            
            dcc.Dropdown(
                dataframe['Indicator Name'].unique() , 
                'Life expectancy at birth, total (years)', 
                id='crossfilter-yaxis-column'
            ) , 
            
            Radio.Items(
                ['linear','radio'], 
                'linear', 
                id='crossfilter-yaxis-type', 
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            )
            
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
        
    ], style={'padding' : '10px 5px' })
])
