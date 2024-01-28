from dash import Dash , dcc,  ctx , html , callback, Input , Output 
import plotly_express as px 
import plotly.graph_objects as go


app = Dash(__name__); 


app.layout = html.Div([

    html.Button('Dessiner le graphe', id='draw_graph'), 
    html.Button('Nettoyer le graphe', id='reset_graph'), 

    dcc.Graph(id="graph")
])

@callback(
    Output(component_id='graph', component_property='figure'),
    inputs = [Input(component_id='draw_graph', component_property="n_clicks"), 
              Input(component_id="reset_graph", component_property="n_clicks")], 
    prevent_initial_call = True
)


def update_graph(button1 , button2) : 

    action = ctx.triggered_id 

    if(action =="reset_graph") : 
        return reset()
    else : 
        return draw()


def draw(): 
    df = px.data.iris() ; 

    return px.scatter(df , x=df.columns[0], y=df.columns[1])


def reset() : 
    return go.Figure() ; 

if(__name__ == "__main__"): 
    app.run(debug=True)