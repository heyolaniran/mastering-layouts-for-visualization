from dash import Dash , html, dcc, callback , Output, Input , Patch
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
                    yshift=10
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


@callback(
    Output('graph', 'figure'), 
    Input('annotation_button', 'n_clicks')
)

def update_graph(action) :

    patched_fig = Patch()

    if action and action % 2 != 0 : 
        patched_fig['layout']["annotations"].clear()
    else :
        patched_fig['layout']['annotations'].extend(
            [
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
                    yshift=10
                )
            ]
        )

    return patched_fig 


if(__name__ == '__main__'): 
    app.run(debug=True)