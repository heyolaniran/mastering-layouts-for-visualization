from dash import Dash , html, dcc, callback , Output, Input 
import plotly.graph_objects as go 

app =  Dash(__name__)


#Multi graphs logic 

figure = go.Figure(
    [
        go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7, 8], y=[0, 1, 3, 2, 4, 3, 4, 6, 5]),
        go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7, 8],y=[0, 4, 5, 1, 2, 2, 3, 4, 2])
    ], 

    go.Layout(
        dict(
            annotations =[
                dict(
                    x=2, 
                    y=5, 
                    text="High point", 
                    showarrow=True , 
                    arrowhead=1
                ), 
                dict(
                    x=7,
                    y=6, 
                    text="High Point", 
                    showarrow=False, 
                    yshift=0
                )
            ]
        ), 
        showlegend=True
    )
)

app.layout = html.Div([

    html.Button('Show/Clear Annotation', id='annotation_button'), 
    dcc.Graph(id='graph', figure=figure)
])


if(__name__ == '__main__'): 
    app.run(debug=True)