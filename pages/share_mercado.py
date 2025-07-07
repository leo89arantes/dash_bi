from dash import html, dcc, dash_table, register_page
import dash_bootstrap_components as dbc
from utils.graphs import listar_municipios_disponiveis, modalidade_dict


register_page(__name__, path="/share-mercado", name="Share Mercado")

# 🚩 Obter a lista de municípios do banco
municipios_opcoes = listar_municipios_disponiveis()

layout = html.Div([
    html.H1("Share Mercado"),

    dbc.Tabs(
        [
            dbc.Tab(
                html.Div([
                    dbc.Row([
                        # 🔍 Barra lateral de filtros
                        dbc.Col([
                            html.H5("Filtros"),
                            html.Label("Município"),
                            dcc.Dropdown(
                                id="filtro-municipio",
                                options=[{"label": m, "value": m} for m in municipios_opcoes],
                                placeholder="Selecione o município",
                                value="GUAXUPE",
                                clearable=False, 
                                searchable=True 
                            ),

                            html.Label("Modalidade"),
                            dcc.Dropdown(
                                id="filtro-modalidade",
                                options=[{"label": key, "value": key} for key in modalidade_dict.keys()],
                                placeholder="Selecione a modalidade",
                                value="Empréstimos e TD",
                                clearable=False,
                                searchable=True
                            ),
                            html.Hr(),

                            # 🔹 Cards de KPIs (placeholders)
                            dbc.Col(id="cards-filtros", width=2),
                            dbc.Card(dbc.CardBody([html.H4("51 mil"), html.P("População")]), color="primary", inverse=True),
                            dbc.Card(dbc.CardBody([html.H4("2,8 M"), html.P("PIB")]), color="success", inverse=True),
                            dbc.Card(dbc.CardBody([html.H4("6 mil"), html.P("Empresas")]), color="danger", inverse=True),
                            dbc.Card(dbc.CardBody([html.H4("52 mil"), html.P("Outro")]), color="warning", inverse=True),
                        ], width=2),

                        # 🔥 Gráficos e tabela
                        dbc.Col([
                            dbc.Row([
                                dbc.Col(dcc.Graph(id="grafico-pie"), width=4),
                                dbc.Col(dcc.Graph(id="grafico-linha"), width=8)
                            ]),
                            html.Br(),
                            dash_table.DataTable(
                                id="tabela-resultados",
                                style_table={'overflowX': 'auto'},
                                style_cell={'textAlign': 'center', 'fontFamily': 'Arial'},
                                style_header={
                                    'backgroundColor': '#40E0D0',
                                    'fontWeight': 'bold',
                                    'color': 'white'
                                },
                                style_data_conditional=[
                                    {
                                        'if': {'row_index': 'odd'},
                                        'backgroundColor': 'rgb(248, 248, 248)'
                                    }
                                ],
                            )
                        ], width=10)
                    ])
                ]),
                label="Dashboard",
                tab_id="Dashboard"
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
