from data import *
#====================GUI=======================================

app = Dash(
    __name__,
    #Import Bootstrap
    # external_stylesheets=[dbc.themes.BOOTSTRAP],
    external_stylesheets=[dbc.themes.DARKLY]
    )

app.layout=html.Div(
    className='container flex h-100 bg-dark',
    children=[
        html.H1('BCG Consulting Case',className=' text-light', style={'text-align':'center'}),
        html.Br(),
        dbc.Row(
            [
               dbc.Col(
                dcc.Dropdown(className='col-auto m-auto bg-dark text-light p-4 dropdown',id='Bars-Dropdown',
                    options=[
                        # dict(zip(['label'],interest1,['value'],interest1))
                        {'label':'Product','value':'Product'},
                        {'label':'Sales_Performance','value':'Sales_Performance'},
                    ],
                    multi=False,
                    value=interest1[0], #Valor Inicial
                    style={'width':'60%'}
                    ),
               ),
               
               dbc.Col(
                dbc.Toast(
                        [
                            html.P(children=[], className="mb-0", id='output_container')
                        ],
                        header="El valor elegido por el usuario es:",
                    ),

                ),
            
            ],
            align='Center',
            
        ),
        dbc.Row(
            [
                dcc.Graph(id='DataFrame_Table',figure={}),
            ]
        )
    ],
)
@app.callback(
    [
        Output(component_id='output_container',component_property='children'),
        Output(component_id='DataFrame_Table',component_property='figure'),
    ],
    [
        Input(component_id='Bars-Dropdown', component_property='value'),
        # Input("folds",'value'),
    ]
    )
#-----------------------------------------------------

def update_Graph(bars_dropdown):
    #graficos en Plotly of matplotlib
    print(bars_dropdown)
    container = f'{bars_dropdown}'

    interest1_values=list()
    for column in df.columns:
        for label in interest1:
            if column==label:
                interest1_values.append(df[column].values)

    # print(np.array(df.index.values,).reshape(len(df.index.values),1))
    interest1.insert(0,'index')
    # interest1_values.insert(0,df.index.values)
    # print(interest1,interest1_values)

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(values=list(interest1),fill_color='grey',align='left'),
                cells=dict(values=list(interest1_values),align='left'),

            )
        ]
    )
    fig.update_layout(
        title_text='DF Visualization',
        title_xanchor ='center',
        title_font =dict(size=24),
        title_x=0.5,
        geo=dict(scope='usa'),

    )
    return [container,fig]


if __name__ == '__main__':
    app.run_server(debug=True)