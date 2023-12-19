from dash import html, Dash, dcc
import plotly_express as px 
import pandas 


df = pandas.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

figure = px.scatter(df,x="gdp per capita", y="life expectancy", 
                    size="population", color="continent",
                     hover_name="country", log_x=True, size_max=90)

app = Dash(__name__) 

app.layout = html.Div([
    html.H4(children='Expérance de vie par capitale', style={'textAlign': 'center'}), 
    dcc.Graph(id='life-exp-vs-gdp', figure=figure)
])


if __name__ == '__main__':
    app.run(debug=True)