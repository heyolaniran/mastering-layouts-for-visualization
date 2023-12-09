from dash import html ,  Dash , dcc

import plotly.express as px
import pandas 

app= Dash(__name__)

# Data to exploit 
df = pandas.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})


#Data visualization method 

fig = px.bar(df , x='Fruit', y='Amount', color='City',barmode='group'); 

# Rendering on web 

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'), 
    html.Div(children='My first layout for Data Visualization'), 
    
    dcc.Graph(id='first-graph', figure=fig)
])


#Run app  

if __name__ == '__main__' :
    app.run(debug=True)