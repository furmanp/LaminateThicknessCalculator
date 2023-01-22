from dash import Dash, dcc, Input, Output, State, callback_context
import pandas as pd
from main import *
from layout import content_layout

app = Dash(__name__, prevent_initial_callbacks=True)
server = app.server
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = content_layout


@app.callback(
    Output('memory', 'data'),  # Output to update the memory state (dataframe with User Input
    Output('ply_table', 'data'),  # Output to update the dash_Table.DataTable
    Output('total_thk', 'value'),
    Output('weight_sqm', 'value'),
    Output('resin_intake', 'value'),
    Input('add_ply', 'n_clicks'),
    Input('undo_btn', 'n_clicks'),
    State('material_dropdown', 'value'),
    State('weight_input', 'value'),
    State('fvf', 'value'),
    State('ply_multiple_input', 'value'),
    State('resin_type', 'value'),
    State('memory', 'data'),

)
def update_df(submit, undo, material, weight, fvf, multiplier, resin_type, store_df):
    fvf = 0.01 * fvf
    if store_df is not None:
        df = pd.read_json(store_df, orient='records')
    else:
        df = pd.DataFrame(columns=['Ply no.', 'Material', 'Weight', 'Thickness'])

    if callback_context.triggered_id == 'add_ply':
        for i in range(multiplier):
            new_entry = pd.DataFrame({'Ply no.': len(df) + 1,
                                      'Material': [material],
                                      'Weight': [weight],
                                      'Thickness': ply_thk(get_density(material), weight, fvf)})
            df = pd.concat([df, new_entry])
    elif callback_context.triggered_id == 'undo_btn':
        df.drop(df.tail(1).index, inplace=True)

    tot_thk = laminate_thk(df, 'Thickness')
    sfc_weight = aerial_weight(get_density(material), get_density(resin_type), fvf, tot_thk)
    resin_cons = resin_intake(get_density(material), get_density(resin_type), fvf, tot_thk)
    return [df.to_json(orient='records'),
            df.to_dict(orient='records'),
            tot_thk,
            sfc_weight,
            resin_cons]


@app.callback(
    Output('download_table', 'data'),
    Input('export_btn', 'n_clicks'),
    State('memory', 'data'),
)
def export_data(n_clicks, store_df):
    df = pd.read_json(store_df, orient='records')
    return dcc.send_data_frame(df.to_csv, "ply_table.csv")


if __name__ == '__main__':
    app.run_server(debug=True)
