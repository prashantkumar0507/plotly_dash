from dash import Dash, Input, Output, dcc,callback, dash_table,html,State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pandas as pd
import pandas as pd
from data_table_utils import getDataTable


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

table_df = pd.read_csv('./data/country_data.csv')
tab_id = 'dtable-rows'
data_table = getDataTable(table_df,tab_id)
add_row_btn = dbc.Button('Add Rows', id='add-btn',class_name='me-1', outline=True ,color='primary', n_clicks=0 )


app.layout = html.Div([
    dbc.Row(dbc.Col(html.H3('DATA TABLE ADD ROWS'), width={'size':3, 'offset':4})),
    html.Br(),
    dbc.Row(dbc.Col(add_row_btn, width={'size':2, 'offset':1})),
    html.Br(),
    dbc.Row(dbc.Col(data_table, width={'size':10, 'offset':1}))
])

# callback to add rows
@app.callback(
    Output('dtable-rows','data'),
    Input('add-btn','n_clicks'),
    State('dtable-rows', 'data'),
    State('dtable-rows', 'columns'),
    prevent_intial_call=True
)
def add_rows(nclicks,rows,cols):
    print('adding row')
    if nclicks>0:
        rows.append({c['id']: '' for c in cols})
        return rows
    
    raise PreventUpdate 
    

app.run_server(port=7001, debug=True)