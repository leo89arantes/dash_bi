from dash import html, dcc
import dash_bootstrap_components as dbc
from data.transform import gerar_series_temporais, gerar_liberacao_mensal, gerar_tabela_atualizacao_1, gerar_atualizacao_mensal, gerar_lancamentos_aprovacoes_liberacoes,\
                            gerar_tabela_atualizacao,  gerar_tabela,  gerar_tabela_atualizacao, gerar_tabela_majoracao, gerar_tabela_erros_rpa, gerar_cards_aprovacoes

layout = html.Div([
    html.H1("Monitoramento RPA"),
    dbc.Tabs(
        [
            dbc.Tab(label="Monitoramento", tab_id="aba1",
                    children=html.Div([dcc.Interval(id='interval', interval=60*1000, n_intervals=0),

                                        html.Div([
                                        # Seção 1: Atualização de Renda
                                        html.Div([
                                            # Cabeçalho verde destacado
                                            html.Div("RPA Atualização de Renda", style={
                                                "backgroundColor": "#0B5345",
                                                "color": "white",
                                                "padding": "8px",
                                                "fontSize": "16px",
                                                "fontWeight": "bold",
                                                "borderTopLeftRadius": "8px",
                                                "borderTopRightRadius": "8px",
                                                "textAlign": "center"
                                            }),

                                            # Corpo da seção (com borda)
                                            html.Div([
                                                # Metade Esquerda: Tabela + Cards
                                                html.Div([
                                                    # Tabela (parte superior esquerda)
                                                    gerar_tabela_atualizacao(),

                                                    # Cards (parte inferior esquerda)
                                                    html.Div([
                                                        html.Div([
                                                            html.Div("230", style={
                                                                "fontSize": "18px", "margin": "0", "color": "white", "fontWeight": "bold"
                                                            }),
                                                            html.P("Atualizações", style={"fontSize": "12px", "margin": "0", "color": "white"})
                                                        ], style={
                                                            "backgroundColor": "#0B5345",
                                                            "padding": "10px",
                                                            "borderRadius": "8px",
                                                            "textAlign": "center",
                                                            "marginBottom": "10px"
                                                        }),

                                                        html.Div([
                                                            html.Div("09:30", style={
                                                                "fontSize": "18px", "margin": "0", "color": "white", "fontWeight": "bold"
                                                            }),
                                                            html.P("Hora início", style={"fontSize": "12px", "margin": "0", "color": "white"})
                                                        ], style={
                                                            "backgroundColor": "#0B5345",
                                                            "padding": "10px",
                                                            "borderRadius": "8px",
                                                            "textAlign": "center"
                                                        })
                                                    ], style={"marginTop": "10px"})
                                                ], style={"flex": "1", "paddingRight": "20px"}),

                                                # Metade Direita: Gráficos
                                                html.Div([
                                                    html.Div([
                                                        dcc.Graph(id="grafico-renda", style={"height": "250px", "width": "100%"})
                                                    ], style={"marginBottom": "20px"}),

                                                    html.Div([
                                                        dcc.Graph(id="grafico-atualizacao-mensal", style={"height": "250px", "width": "100%"})
                                                    ])
                                                ], style={"flex": "1"})
                                            ], style={
                                                "display": "flex",
                                                "width": "100%",
                                                "border": "2px solid #0B5345",
                                                "borderBottomLeftRadius": "8px",
                                                "borderBottomRightRadius": "8px",
                                                "padding": "10px",
                                                "boxSizing": "border-box"
                                            })
                                        ], style={
                                            "flex": "1",
                                            "width": "50%",
                                            "padding": "20px",
                                            "boxSizing": "border-box"
                                        }),

                                        # Seção 2: Majoração de Cheque Especial
                                        html.Div([
                                                # Cabeçalho verde destacado
                                                html.Div("RPA Majoração Cheque Especial", style={
                                                    "backgroundColor": "#0B5345",
                                                    "color": "white",
                                                    "padding": "8px",
                                                    "fontSize": "16px",
                                                    "fontWeight": "bold",
                                                    "borderTopLeftRadius": "8px",
                                                    "borderTopRightRadius": "8px",
                                                    "textAlign": "center"
                                                }),

                                                # Corpo da seção (com borda)
                                                html.Div([
                                                    # Tabelas de Majoração e Erros
                                                    html.Div([
                                                        html.Div([
                                                            gerar_tabela_majoracao()
                                                        ], style={"flex": "1", "paddingRight": "10px"}),

                                                        html.Div([
                                                            gerar_tabela_erros_rpa()
                                                        ], style={"flex": "1", "paddingLeft": "10px"})
                                                    ], style={"display": "flex", "width": "100%", "flexWrap": "wrap"}),

                                                    # Cards de Aprovações e Tempo Médio
                                                    html.Div([
                                                        html.Div([
                                                            gerar_tabela()
                                                        ], style={"flex": "1", "paddingRight": "10px"}),

                                                        html.Div([
                                                            gerar_cards_aprovacoes()
                                                        ], style={"flex": "1", "paddingLeft": "10px"})
                                                    ], style={"display": "flex", "width": "100%", "marginTop": "20px"}),

                                                    # Gráficos lado a lado
                                                    html.Div([
                                                        html.Div([
                                                            dcc.Graph(id="grafico-liberacao-mensal", style={"height": "300px", "width": "100%"})
                                                        ], style={"flex": "1", "paddingRight": "10px"}),

                                                        html.Div([
                                                            dcc.Graph(id="grafico-lanc-aprov-lib", style={"height": "300px", "width": "100%"})
                                                        ], style={"flex": "1", "paddingLeft": "10px"})
                                                    ], style={"display": "flex", "width": "100%", "marginTop": "20px"})
                                                ], style={
                                                    "border": "2px solid #0B5345",
                                                    "borderBottomLeftRadius": "8px",
                                                    "borderBottomRightRadius": "8px",
                                                    "padding": "10px",
                                                    "boxSizing": "border-box"
                                                })
                                            ], style={
                                                "flex": "1",
                                                "width": "50%",
                                                "padding": "20px",
                                                "boxSizing": "border-box"
                                            })
                                        ], style={
                                            "display": "flex",
                                            "width": "100%",
                                            "flexWrap": "nowrap"
                                        }),
                                        html.Div(id='cards-container')
                                        ])



                    
                    ),
            dbc.Tab(label="Desempenho", tab_id="aba2"),
            dbc.Tab(label="Resultado", tab_id="aba3"),
        ],
        id="tabs",
        active_tab="aba1",
    ),
])
