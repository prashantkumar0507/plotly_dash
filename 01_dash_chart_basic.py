from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# create data frame using plotly express data package
graph_df = px.data.medals_long()


#basic graph component
myGraph = dcc.Graph(figure={})   #no figure added
mySelection = dcc.Dropdown(options=["CHART1", "CHART2"],
                           value="CHART1",
                           clearable=False)


app.layout = dbc.Container([myGraph,mySelection])

@app.callback(
    Output(myGraph, component_property="figure"),
    Input(mySelection, component_property="value")
)
def change_graph(user_selection):
    if user_selection=="CHART1":
        fig = px.bar(data_frame=graph_df, x="nation", y="count", color="medal")
    elif user_selection=="CHART2":
        fig = px.scatter(data_frame=graph_df, x="nation", y="count", color="medal")
    
    return fig


#run the app
if __name__=="__main__":
    app.run_server(port=8051, debug=True)
