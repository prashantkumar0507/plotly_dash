from dash import Dash, Input,Output, dcc,callback,html
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

dd_component = dcc.Dropdown(id='drop_id', options=['activate','disable'])

# simple buttons
btn_simple = dbc.Button('Click',id='simple_btn', disabled=True, n_clicks=0, name='Click!' )

# adding styles to buttons
btn_style_one = dbc.Button('Primary',id='primary_btn', outline=True, color='primary', n_clicks=0 )
btn_style_two = dbc.Button('Success',id='success_btn', outline=True, color='success', n_clicks=0 )

btn_style_three = dbc.Button('Danger',id='danger_btn', outline=True, color='danger', n_clicks=0 )



# simple layout
# app.layout = dbc.Container([dd_component,html.Br() ,btn_simple])

# /styling layout
app.layout = html.Div([
    dbc.Row(dbc.Col(dd_component, width={'size':2, 'offset':1})),
    html.Br(),
    dbc.Row(dbc.Col(btn_simple,width={'size':2, 'offset':1})),
    html.Br(),
    dbc.Row([dbc.Col(btn_style_one, width={'size':1, 'offset':1}),
             dbc.Col(btn_style_two, width={'size':1}),
             dbc.Col(btn_style_three, width={'size':1})]),           # Adding multiple buttons in single row  ##1
    html.Br(),        
    dbc.Row(dbc.Col(html.Div([btn_style_one,btn_style_two,btn_style_three]),
                     width={'size':4, 'offset':1}))                 #2 Adding multiple buttons in single row
])



#call back button event. Activate / Deactivate button based on dropdown selection
@callback(
    Output('simple_btn','disabled'),
    Input('drop_id','value'),
)
def activate_button(selection):
    if selection == 'activate':
        return False
    
    return True

if __name__=="__main__":
    app.run_server(port=8053, debug=True)