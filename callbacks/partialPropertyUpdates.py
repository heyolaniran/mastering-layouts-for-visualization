from dash import Dash, html, callback , Patch , Output , Input, dcc
import plotly_express as px; 
import pandas ; 



app= Dash(__name__, title='Country Indicator 2.0')


# Resource from gapminder data 
df = pandas.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')


figure = px.scatter(df, x="gdp per capita", y="life expectancy", hover_name="country",
                 log_x=True, size_max=60)


figure.update_traces(marker=dict(color="blue"))




app.layout = html.Div([
    html.H3("Updating Country Point Colors"), 
    dcc.Dropdown(id="dropdown" , options=df.country.unique(), multi=True) , 
    dcc.Graph(id="graph", figure=figure)
])


@callback(
    Output(component_id="graph", component_property='figure'), 
    Input(component_id="dropdown", component_property='value'),
    prevent_initial_call=True
)

def update_markers(countries) : 

    country_count = list(df[df.country.isin(countries)].index)

    patched_fig = Patch() 

    updated_markers = [
        "green" if i in country_count else "blue" for i in range(len(df)+1)
    ]

    patched_fig['data'][0]['marker']['color'] = updated_markers

    return patched_fig


if(__name__ == '__main__') : 
    app.run(debug=True)