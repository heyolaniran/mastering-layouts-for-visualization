from dash import Dash , html, dcc , clientside_callback , Output, Input, dash_table


styles = ['']

options = [
   {
        "label": "Car-sharing data",
        "value": "https://raw.githubusercontent.com/plotly/datasets/master/carshare_data.json",
   }, 
   {
       "label" : "Iris data" , 
       "value" : "https://raw.githubusercontent.com/plotly/datasets/master/iris_data.json"
   }, 


 ]


app = Dash(__name__, title="Data Table", external_stylesheets=styles)


app.layout = html.Div([

    html.B('Display Raw APIs data in Data Table', style={'textAlign': 'center'}), 

    dcc.Dropdown(options=options ,  value="https://raw.githubusercontent.com/plotly/datasets/master/iris_data.json" , id='api_select') ,


    html.Div([
        html.P('Display DataTable') ,

        dash_table.DataTable(id="dataTable")

    ])
])


clientside_callback(
    """
    async function(value) {
       const data = await fetch(value)
                    .then((response)=>{
                         return response.json()
                 })

        return data 
    }
    """,
    Output("dataTable", 'data'), 
    Input('api_select', 'value')
)


if(__name__ == '__main__') :
    app.run()