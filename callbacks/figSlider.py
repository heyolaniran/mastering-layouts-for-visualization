from dash import html, dcc, Dash , Input, Output, callback
import plotly_express as px 
import pandas 


app = Dash(__name__) 

fig = pandas.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app.layout = html.Div([

    html.Div([
        html.H3('Rechercher des informations par Pays'), 
        dcc.Input(id='my_country', value='Benin', type='text')
    ], style={'textAlign' : 'center', 'flex' : 3}),

    dcc.Graph(id='fig-with-slider'), 
    dcc.Slider(
        min=fig['year'].min(), 
        max=fig['year'].max(), 
        step=None, 
        value=fig['year'].min(), 
        marks={str(year) : str(year) for year in fig['year'].unique()}, 
        id='year-slider'
    ),

    html.Br(), 

    

])

@callback(
    Output('fig-with-slider', 'figure'), 
    Input(component_id='my_country', component_property='value'), 
    Input(component_id='year-slider', component_property='value')
)


def update_fig(my_country, selected_year) :
    if my_country == '' : 
        country_fig = fig 
        filtred_fig = country_fig[country_fig.year == selected_year]
        figure = px.scatter(filtred_fig, x='gdpPercap',
                    y='lifeExp', 
                    color='continent',
                    size='pop', hover_name='country', size_max=100)
    else :
        #fixes handling country error 
        try :
            country_fig = fig[fig.country == my_country]
            
        except :
            country_fig= fig[fig.continent == 'Africa'] 
        figure = px.line(country_fig,x='year',y='lifeExp')
    figure.update_layout(transition_duration=200)
    return figure


if __name__ == '__main__' :
    app.run(debug=True)