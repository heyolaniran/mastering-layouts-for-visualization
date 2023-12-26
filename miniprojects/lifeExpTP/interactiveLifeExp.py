from dash import Dash , html, callback , Output , Input , dcc
import plotly_express as px 
import pandas 

# Externals resources to use 

external_style = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

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


@callback(
    Output(component_id='crossfilter-indicator-scatter', component_property='figure'), 
    Input(component_id='crossfilter-xaxis-column', component_property='value'),
    Input(component_id='crossfilter-yaxis-column', component_property='value'),
    Input(component_id='crossfilter-xaxis-type', component_property='value'),
    Input(component_id='crossfilter-yaxis-type', component_property='value'),
    Input(component_id='crossfilter-year--slider', component_property='value')
)

def upgrade_graph(xaxis_column , yaxis_column, xaxis_type, yaxis_type, selected_year) :
    #Get data for specific selected year from source file 
    df = dataframe[dataframe['Year'] == selected_year]

    #Build scatter plot from df 

    figure = px.scatter(df , x=df[df['Indicator Name']==xaxis_column]['Value'], 
                        y=df[df['Indicator Name'] == yaxis_column]['Value'],
                        hover_name=df[df['Indicator Name']== yaxis_column]['Country Name'])
    

    #Update traces for scatter plote

    figure.update_traces(customdata=df[df['Indicator Name'] == yaxis_column]['Country Name'])

    # Transition for scatter plot update 
    figure.update_layout(hovermode='closest', margin={'l': 40 , 'b': 40 ,  't': 10 , 'r': 0})

    #Update axes display name

    figure.update_xaxes(title=xaxis_column, type=xaxis_type)

    figure.update_yaxes(title=yaxis_column, type=yaxis_type)

    return figure


if(__name__ == '__main__') : 
    app.run(debug=True)