from dash import html, dcc, dash_table, register_page
import dash_bootstrap_components as dbc
from utils.graphs import listar_municipios_disponiveis, modalidade_dict


register_page(__name__, path="/carteira-cobranca", name="Cobrança")



# Tabs com aba base preenchida
layout = html.Div([
    html.H1("Cobrança"),
    dbc.Tabs(
        [
            dbc.Tab(
                html.Div("ABA 1 -"),
                label="Base",
                tab_id="aba-1",
                label_style={"color": "#00A091"},
                active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            dbc.Tab(html.P("Aba 2 aberta!"), label="Liquidação", tab_id="aba-2",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            dbc.Tab(html.P("Aba 3 aberta!"), label="Resultado", tab_id="aba-3",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            dbc.Tab(html.P("Aba 4 aberta!"), label="Ranking", tab_id="aba-4",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            dbc.Tab(html.P("Aba 6 aberta!"), label="Propensos", tab_id="aba-6",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),
        ],
        id="tabs",
        active_tab="aba-1",
    )
])
