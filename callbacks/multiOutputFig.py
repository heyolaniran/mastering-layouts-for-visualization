from dash import Dash , dcc , html, callback , Input, Output
import plotly_express as px 
import pandas 


app = Dash(__name__)


dataframe = pandas.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

app.layout = html.Div([

    #First input div 
    html.Div([

        dcc.Dropdown(
            dataframe['Indicator Name'].unique(), 
            'Agriculture, value added (% of GDP)', 
            id='x_indicator'
        ),

        dcc.RadioItems(
            ['linear', 'Log'], 
            'linear', 
            inline=True, 
            id='xaxis_type'
        )
       
    ], style={'width' : '48%', 'display':  'inline-block'}), 

    #Second input div 

    html.Div([
        dcc.Dropdown(
            dataframe['Indicator Name'].unique(), 
            'Life expectancy at birth, total (years)', 
            id="y_indicator", 
        ), 

        dcc.RadioItems(
            ['linear', 'Log'], 
            'linear', 
            inline=True, 
            id='yaxis_type'
        )
    ] , style={'display' : 'inline-block' , 'float' : 'right', 'width' : '48%'}) , 

    #Graph 


    dcc.Graph(id="graph"), 

    dcc.Slider(
        min=dataframe['Year'].min(), 
        max=dataframe['Year'].max(), 
        id="graph-slider",
        value=dataframe['Year'].max(),  
        marks={str(year) : str(year) for year in dataframe['Year'].unique()}
    )

])

# Define Callback 

@callback(
    Output('graph', 'figure'),
    Input(component_id='x_indicator', component_property='value'), 
    Input(component_id='y_indicator', component_property='value'),
    Input(component_id='xaxis_type', component_property='value'), 
    Input(component_id='yaxis_type', component_property='value'), 
    Input(component_id='graph-slider', component_property='value'), 
    

)

def update_graph(x_indicator, y_indicator , xaxis_type , yaxis_type , year) :
    df = dataframe[dataframe['Year'] == year] 

    fig = px.scatter(df, x=df[df['Indicator Name'] == x_indicator]['Value'], 
                    y=df[df['Indicator Name'] == y_indicator]['Value'],
                    hover_name=df[df['Indicator Name'] == y_indicator]['Country Name'])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0} , hovermode="closest")
    fig.update_xaxes(title=x_indicator, type=xaxis_type)
    fig.update_yaxes(title=y_indicator,  type=yaxis_type)

    return fig 


if __name__ == '__main__' :
    app.run(debug=True)