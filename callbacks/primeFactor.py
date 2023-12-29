from dash import Dash ,  html , dcc , callback ,  Output , Input , no_update
from dash.exceptions import PreventUpdate 


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(name=__name__ , external_stylesheets=styles, title='Prime Factors') 

app.layout = html.Div([
    
    html.P('Insert a number and get his prime factors'),
    
    dcc.Input(id='number') , 
    
    html.Div(id='result')
])

@callback(
    Output('result', component_property='children'), 
    Input(component_id='number', component_property='value')
)

def show_prime_factors(number) : 
    if number is None : 
        raise PreventUpdate(msg="Insert not null value plz")
 
    factors = prime_factors(number)
    return '{} equals to {}'.format(number , '*'.join(str(factor) for factor in factors))


def prime_factors(num) : 
        n = int(num)
        i = 2 
        factors = [] 
        
        while n >= i*i : 
            if n % i == 0: 
                n = int(n/i)
                factors.append(i)
            else : 
                i+= 1 if i == 2 else 2
            
            
        factors.append(n)
        
        return factors
    
if __name__ == '__main__' : 
    app.run(debug=True)