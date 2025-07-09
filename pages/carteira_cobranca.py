from dash import html, dcc, dash_table, register_page
import dash_bootstrap_components as dbc


register_page(__name__, path="/carteira-cobranca", name="Cobrança")

# Layout da aba Base
base_layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Filtros"),
                dbc.CardBody([
                    html.Div([
                        dbc.Label("PA"),
                        dbc.Input(id="input-pa", type="text", placeholder="PA"),
                    ]),
                    html.Div([
                        dbc.Label("Ano/mês"),
                        dbc.Input(id="input-ano-mes", type="text", placeholder="Ano/mês"),
                    ]),
                    html.Div([
                        dbc.Label("Modalidade"),
                        dbc.Input(id="input-modalidade", type="text", placeholder="Modalidade"),
                    ]),
                ])
            ]),
            html.Br(),
            dbc.Card([
                dbc.CardHeader("Metas"),
                dbc.CardBody([
                    html.Div(id="tabela-metas"),
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.Div([
                                    html.H4("137.453", className="card-title"),
                                    html.P("Qtd Emitidos no Mês", className="card-text"),
                                    html.H5("117.720", className="card-title"),
                                    html.P("Qtd Liquidado no Mês", className="card-text"),
                                ], className="me-3"),
                                dcc.Graph(id="grafico-rosca-qtd", style={
                                    "width": "100px",
                                    "height": "100px",
                                    "margin-left": "auto",
                                    "margin-right": "auto",
                                    "display": "block"
                                })
                            ], className="d-flex align-items-center"),
                        ])
                    ])
                ], width=6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.Div([
                                    html.H4("R$161.131.535", className="card-title"),
                                    html.P("Valor Emitido no Mês", className="card-text"),
                                    html.H5("R$135.343.686", className="card-title"),
                                    html.P("Valor Liquidado no Mês", className="card-text"),
                                ], className="me-3"),
                                dcc.Graph(id="grafico-rosca-valor", style={
                                    "width": "100px",
                                    "height": "100px",
                                    "margin-left": "auto",
                                    "margin-right": "auto",
                                    "display": "block"
                                })
                            ], className="d-flex align-items-center"),
                        ])
                    ])
                ], width=6),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Projeto 123"),
                            html.Div([
                                html.P("Realizadas"),
                                html.P("200"),
                            ], className="d-flex justify-content-between"),
                            html.Div([
                                html.P("Falta"),
                                html.P("1017"),
                            ], className="d-flex justify-content-between"),
                            html.Div([
                                html.P("Total"),
                                html.P("1217"),
                            ], className="d-flex justify-content-between"),
                            dbc.Progress(value=20, className="mb-3"),
                        ])
                    ])
                ], width=6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H5("Gestão de Metas"),
                            html.Div([
                                html.P("Realizadas"),
                                html.P("0"),
                            ], className="d-flex justify-content-between"),
                            html.Div([
                                html.P("Falta"),
                                html.P("1217"),
                            ], className="d-flex justify-content-between"),
                            html.Div([
                                html.P("Total"),
                                html.P("1217"),
                            ], className="d-flex justify-content-between"),
                            dbc.Progress(value=0, className="mb-3"),
                        ])
                    ])
                ], width=6),
            ]),
        ], width=9),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Tabela de Dados"),
                    html.Div(id="tabela-cobranca"),
                ])
            ])
        ], width=12),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Boletos Emitidos"),
                    dcc.Graph(id="grafico-boletos-emitidos"),
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Mortalidade da Carteira"),
                    dcc.Graph(id="grafico-mortalidade-carteira"),
                ])
            ])
        ], width=6),
    ]),
])

# Layout da aba Liquidação
liquidacao_layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Filtros"),
                dbc.CardBody([
                    html.Div([
                        dbc.Label("PA"),
                        dbc.Input(id="input-pa-liq", type="text", placeholder="PA"),
                    ]),
                    html.Div([
                        dbc.Label("Ano/mês"),
                        dbc.Input(id="input-ano-mes-liq", type="text", placeholder="Ano/mês"),
                    ]),
                    html.Div([
                        dbc.Label("Modalidade"),
                        dbc.Input(id="input-modalidade-liq", type="text", placeholder="Modalidade"),
                    ]),
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.Div([
                                    html.H4("32.235", className="card-title"),
                                    html.P("Liquidados na cooperativa emissora", className="card-text"),
                                    html.H5("10.265", className="card-title"),
                                    html.P("Liquidados Rede Externa", className="card-text"),
                                    html.H5("4.235", className="card-title"),
                                    html.P("Liquidados Sicoob", className="card-text"),
                                ], className="me-3"),
                                dcc.Graph(id="grafico-rosca-qtd-liq", style={
                                    "width": "100px",
                                    "height": "100px",
                                    "margin-left": "auto",
                                    "margin-right": "auto",
                                    "display": "block"
                                })
                            ], className="d-flex align-items-center"),
                        ])
                    ])
                ], width=6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.Div([
                                    html.H4("R$161.131.535", className="card-title"),
                                    html.P("Valor Emitido no Mês", className="card-text"),
                                    html.H5("R$135.343.686", className="card-title"),
                                    html.P("Valor Liquidado no Mês", className="card-text"),
                                    html.H5("R$161.131.535", className="card-title"),
                                    html.P("Valor Emitido no Mês", className="card-text"),
                                ], className="me-3"),
                                dcc.Graph(id="grafico-rosca-valor-liq", style={
                                    "width": "100px",
                                    "height": "100px",
                                    "margin-left": "auto",
                                    "margin-right": "auto",
                                    "display": "block"
                                })
                            ], className="d-flex align-items-center"),
                        ])
                    ])
                ], width=6),
            ]),
        ], width=9),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Qtd de Títulos emitidos por Local de Liquidação"),
                    dcc.Graph(id="grafico-qtd-liquidacao"),
                ])
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Valor de Títulos emitidos por Local de Liquidação"),
                    dcc.Graph(id="grafico-valor-liquidacao"),
                ])
            ])
        ], width=6),
    ]),
])



# Tabs com aba base preenchida
layout = html.Div([
    html.H1("Cobrança"),
    dbc.Tabs(
        [
            dbc.Tab(
                html.Div(base_layout),
                label="Base",
                tab_id="aba-1",
                label_style={"color": "#00A091"},
                active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            dbc.Tab(html.P(liquidacao_layout), label="Liquidação", tab_id="aba-2",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            # Aba Resultado com gráficos e tabela
            dbc.Tab(
                html.Div([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.H5("Receita dos últimos 12 meses"),
                                    dcc.Graph(id="grafico-receita-12m")
                                ])
                            ])
                        ], width=6),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.H5("Despesa dos últimos 12 meses"),
                                    dcc.Graph(id="grafico-despesa-12m")
                                ])
                            ])
                        ], width=6),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.H5("Resultado dos últimos 12 meses"),
                                    dcc.Graph(id="grafico-resultado-12m")
                                ])
                            ])
                        ], width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.H5("Evolução Receita e Despesa (MoM/YoY)"),
                                    html.Div(id="tabela-evolucao-receita-despesa")
                                ])
                            ])
                        ], width=12),
                    ]),
                ]),
                label="Resultado",
                tab_id="aba-3",
                label_style={"color": "#00A091"},
                active_label_style={"color": "#00A091", "fontWeight": "bold"}
            ),

            # Aba Ranking com dois rankings em tabelas
            dbc.Tab(
                html.Div([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.H5("Cooperados com Contrato Ativo"),
                                    html.Div(id="tabela-ranking-contrato-ativo")
                                ])
                            ])
                        ], width=6),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.H5("Contatos Ativos por Qtd. de Boletos"),
                                    html.Div(id="tabela-ranking-boletos")
                                ])
                            ])
                        ], width=6),
                    ]),
                ]),
                label="Ranking",
                tab_id="aba-4",
                label_style={"color": "#00A091"},
                active_label_style={"color": "#00A091", "fontWeight": "bold"}
            ),

            dbc.Tab(html.P("Aba 6 aberta!"), label="Propensos", tab_id="aba-6",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),
        ],
        id="tabs",
        active_tab="aba-1",
    )
])
