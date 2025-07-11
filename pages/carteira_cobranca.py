from dash import html, dcc, dash_table, register_page
import dash_bootstrap_components as dbc


register_page(__name__, path="/carteira-cobranca", name="Cobrança")

base_layout = html.Div([

    # Linha dos cards centralizados e maiores
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Card([
                    html.Div(style={
                        "position": "absolute",
                        "left": 0,
                        "top": 0,
                        "bottom": 0,
                        "width": "16px",
                        "backgroundColor": "#C9D200",
                        "borderTopLeftRadius": "12px",
                        "borderBottomLeftRadius": "12px"
                    }),
                    dbc.CardBody([
                        html.Div([
                            dcc.Graph(id="grafico-rosca-qtd", style={
                                "width": "220px",
                                "height": "220px",
                                "margin": "0 auto",
                                "display": "block"
                            }, config={"displayModeBar": False}),
                            html.Div([
                                html.Div([
                                    html.H4("137.453", className="card-title mb-0", style={"fontWeight": "bold", "textAlign": "center"}),
                                    html.P("Qtd Emitidos no Mês", className="card-text", style={"fontSize": "16px", "textAlign": "center", "marginBottom": "0"})
                                ], style={"flex": 1}),
                                html.Div([
                                    html.H4("117.720", className="card-title mb-0", style={"fontWeight": "bold", "textAlign": "center"}),
                                    html.P("Qtd Liquidado no Mês", className="card-text", style={"fontSize": "16px", "textAlign": "center", "marginBottom": "0"})
                                ], style={"flex": 1})
                            ], style={"display": "flex", "justifyContent": "space-around", "marginTop": "10px"})
                        ], style={"display": "flex", "flexDirection": "column", "alignItems": "center", "position": "relative"}),
                    ])
                ], style={
                    "boxShadow": "0 4px 16px 0 rgba(0,0,0,0.15)",
                    "borderRadius": "12px",
                    "position": "relative",
                    "overflow": "hidden",
                    "width": "100%",
                    "maxWidth": "600px",
                    "height": "340px",
                    "margin": "0 auto"
                })
            ], style={"display": "flex", "justifyContent": "center"})
        ], width=6),
        dbc.Col([
            html.Div([
                dbc.Card([
                    html.Div(style={
                        "position": "absolute",
                        "left": 0,
                        "top": 0,
                        "bottom": 0,
                        "width": "16px",
                        "backgroundColor": "#C9D200",
                        "borderTopLeftRadius": "12px",
                        "borderBottomLeftRadius": "12px"
                    }),
                    dbc.CardBody([
                        html.Div([
                            dcc.Graph(id="grafico-rosca-valor", style={
                                "width": "220px",
                                "height": "220px",
                                "margin": "0 auto",
                                "display": "block"
                            }, config={"displayModeBar": False}),
                            html.Div([
                                html.Div([
                                    html.H4("R$161.131.535", className="card-title mb-0", style={"fontWeight": "bold", "textAlign": "center"}),
                                    html.P("Valor Emitido no Mês", className="card-text", style={"fontSize": "16px", "textAlign": "center", "marginBottom": "0"})
                                ], style={"flex": 1}),
                                html.Div([
                                    html.H4("R$135.343.686", className="card-title mb-0", style={"fontWeight": "bold", "textAlign": "center"}),
                                    html.P("Valor Liquidado no Mês", className="card-text", style={"fontSize": "16px", "textAlign": "center", "marginBottom": "0"})
                                ], style={"flex": 1})
                            ], style={"display": "flex", "justifyContent": "space-around", "marginTop": "10px"})
                        ], style={"display": "flex", "flexDirection": "column", "alignItems": "center", "position": "relative"}),
                    ])
                ], style={
                    "boxShadow": "0 4px 16px 0 rgba(0,0,0,0.15)",
                    "borderRadius": "12px",
                    "position": "relative",
                    "overflow": "hidden",
                    "width": "100%",
                    "maxWidth": "600px",
                    "height": "340px",
                    "margin": "0 auto"
                })
            ], style={"display": "flex", "justifyContent": "center"})
        ], width=6),
    ], style={"marginBottom": "32px"}),
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
                                }, config={"displayModeBar": False})
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
                                }, config={"displayModeBar": False})
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
    # Linha com título à esquerda e filtros colados ao topo/canto direito
    dbc.Row([
        dbc.Col([
            html.H1("Cobrança", style={"marginBottom": 0, "marginTop": 0})
        ], width=6, style={"display": "flex", "alignItems": "flex-start", "paddingTop": "0", "paddingBottom": "0"}),
        dbc.Col([
            html.Div([
                dbc.Row([
                    dbc.Col([
                        dbc.Label("PA", style={"fontWeight": "bold", "marginBottom": "2px"}),
                        dbc.Input(id="input-pa", type="text", placeholder="PA", style={"maxWidth": "120px", "height": "32px", "padding": "2px 8px"})
                    ], width="auto", style={"paddingRight": "8px", "paddingLeft": "0"}),
                    dbc.Col([
                        dbc.Label("Ano/mês", style={"fontWeight": "bold", "marginBottom": "2px"}),
                        dbc.Input(id="input-ano-mes", type="text", placeholder="Ano/mês", style={"maxWidth": "120px", "height": "32px", "padding": "2px 8px"})
                    ], width="auto", style={"paddingRight": "8px", "paddingLeft": "0"}),
                    dbc.Col([
                        dbc.Label("Modalidade", style={"fontWeight": "bold", "marginBottom": "2px"}),
                        dbc.Input(id="input-modalidade", type="text", placeholder="Modalidade", style={"maxWidth": "120px", "height": "32px", "padding": "2px 8px"})
                    ], width="auto", style={"paddingRight": "0", "paddingLeft": "0"}),
                ], justify="end", align="start", style={"gap": "8px", "flexWrap": "nowrap", "marginTop": "0", "marginBottom": "0"})
            ], style={"display": "flex", "justifyContent": "flex-end", "alignItems": "flex-start", "paddingTop": "0", "paddingBottom": "0"})
        ], width=6, style={"display": "flex", "alignItems": "flex-start", "justifyContent": "flex-end", "paddingTop": "0", "paddingBottom": "0"})
    ], style={"marginBottom": "8px", "marginTop": "0", "paddingTop": "0", "paddingBottom": "0"}),
    html.Hr(style={"marginTop": "0", "marginBottom": "24px"}),
    # As abas ficam logo abaixo dos filtros
    html.Div([
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
        ),
        # Espaço entre as abas e a primeira linha
        html.Div(style={"marginBottom": "32px"}),
    ]),
    # O conteúdo principal já está dentro das abas
])
