from dash import html, dcc, Dash
import plotly.express as px
import pandas
#App 

app = Dash(__name__) ; 


#set colors 

colors = {
    'background' : '#111111',
    'text' : '#7FDBFF'
}

#dataFrame 

df= pandas.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x='Fruit', y='Amount', color='City',barmode='group' )

#apply stylizing on figure 

fig.update_layout(
    plot_bgcolor = 'white',
    paper_bgcolor = 'white',
    font_color = 'black'
)


#App layout

app.layout = html.Div(style={'backgroundColor' : colors['background']},
                        children = [
                            html.H1(children='Hello People', style={'textAlign' : 'center' , 'color': colors['text']}) , 

                            html.Div(children='Evolution App v2', style={
                                'textAlign' : 'center',
                                'color' : colors['text']
                            }),

                            dcc.Graph(
                                id='secondo', 
                               figure = fig
                            )
                        ]
                    )


if __name__ == '__main__' :
    app.run(debug=True)