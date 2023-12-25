from dash import Dash
import plotly_express as px 
import pandas


external_styleSheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] 

app = Dash(__name__ , external_stylesheets=external_styleSheets) 

styles = {
    'pre' : {
        'border' : 'thin lightgrey bold', 
        'overflowX' : 'scroll'
    }
}

df = pandas.DataFrame({
     "x": [1,2,1,2],
    "y": [1,2,3,4],
    "customdata": [1,2,3,4],
    "fruit": ["apple", "apple", "orange", "orange"]
})

fig = px.scatter(df, x='x' , y='y', color='fruit')

fig.update_layout(clickmode='event+select')

fig.update_traces(marker_size=15)

