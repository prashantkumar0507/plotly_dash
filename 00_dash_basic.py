from dash import Dash,dcc, Output,Input
import dash_bootstrap_components as dbc



#initialize the app using Dash constructor and applies BOOTSTRAP theme
app = Dash(__name__, external_stylesheets= [dbc.themes.BOOTSTRAP])

#create markdown component and input component
mkd_txt = dcc.Markdown(children="")
input_text = dcc.Input(value="Hola Friend !")


#create a layout for page
app.layout= dbc.Container([mkd_txt,input_text])



#callback to the components , for interactivity
@app.callback(
    Output(mkd_txt, component_property="children"),
    Input(input_text, component_property="value")
)
def change_markdown(user_input):
    return user_input


#run the app
if __name__=="__main__":
    app.run_server(port=8051)