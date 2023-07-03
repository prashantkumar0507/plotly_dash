from dash import Dash, Input,Output, dcc,callback,html
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

dd_component = dcc.Dropdown(id='drop_id', options=['activate','disable'])

btn_simple = dbc.Button('Click',id='simple_btn', disabled=True, n_clicks=0, name='Click!' )

app.layout = dbc.Container([dd_component,html.Br() ,btn_simple])


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