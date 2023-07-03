from dash import Dash, Input, Output, dcc,callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

table_df = pd.read_csv('./data/country_data.csv')

table_df.head()

data_table = dash_table.DataTable(table_df.to_dict('records'), id='simple_tbl',columns= [{"name": i, "id": i} for i in table_df.columns])

app.layout= dbc.Container([data_table])

if __name__=="__main__":
    app.run_server(port=8053, debug=True)