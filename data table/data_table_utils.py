from dash import dash_table
import pandas as pd


def getDataTable(df,tid):
    table = dash_table.DataTable(
        id=tid,
        columns=([{"name": i, "id": i} for i in df.columns]),
        data=df.to_dict('records'),
        editable=True,
        page_size=15,           # number of rows per page
        sort_action='native',
        filter_action='native'
    )

    return table

