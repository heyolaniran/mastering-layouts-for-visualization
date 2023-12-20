from dash import html, dcc, Dash , Input, Output, callback
import plotly_express as px 
import pandas 


app = Dash(__name__) 

fig = pandas.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app.layout = html.Div([

    dcc.Graph(id='fig-with-slider'), 
    dcc.Slider(
        min=fig['year'].min(), 
        max=fig['year'].max(), 
        step=None, 
        value=fig['year'].min(), 
        marks={str(year) : str(year) for year in fig['year'].unique()}, 
        id='year-slider'
    )

])

@callback(
    Output('fig-with-slider', 'figure'), 
    Input(component_id='year-slider', component_property='value')
)


def update_fig(selected_year) :
    filtred_fig = fig[fig.year == selected_year]
    figure = px.scatter(filtred_fig, x='gdpPercap',
                y='lifeExp', 
                color='continent',
                size='pop', hover_name='country', size_max=100)
    figure.update_layout(transition_duration=200)
    return figure


if __name__ == '__main__' :
    app.run(debug=True)