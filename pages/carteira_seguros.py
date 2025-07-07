from dash import html, dcc, dash_table, register_page
import dash_bootstrap_components as dbc
from utils.graphs import listar_municipios_disponiveis, modalidade_dict


register_page(__name__, path="/carteira-seguro", name="Seguros")

# 🚩 Obter a lista de municípios do banco
municipios_opcoes = listar_municipios_disponiveis()

layout = html.Div([
    html.H1("Seguros"),

    dbc.Tabs(
        [
            dbc.Tab(
                label="Dashboard"
            ),

            dbc.Tab(
                html.P("Aba 2 aberta!"),
                label="ABA 2"
            ),
        ],
        id="tabs",
        active_tab="Dashboard",
    ),
])
