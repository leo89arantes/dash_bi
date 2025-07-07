from data.queries import carregar_carteira
import plotly.graph_objects as go
import random
import pandas as pd
from dash import dcc, html



# Funções para gerar dados simulados
def gerar_series_temporais():
    dias = pd.date_range(start=pd.Timestamp.today().replace(day=1), periods=10).strftime('%d/%b').tolist()
    valores = [random.randint(100, 400) for _ in dias]
    df = pd.DataFrame({"Dia": dias, "Atualizações": valores})
    return df

def gerar_liberacao_mensal():
    meses = pd.date_range(start=pd.Timestamp.today().replace(month=1, day=1), periods=12, freq='MS').strftime('%b/%y').tolist()
    valores = [random.randint(500, 2000) for _ in meses]
    df = pd.DataFrame({"Mês": meses, "Liberações": valores})
    return df

def gerar_tabela():
    dados = [
        {"IP": 220, "Qtd": 32, "Tempo médio": "04:32:20", "Último Lançamento": "15:25:36", "Status": "Em execução"},
        {"IP": 221, "Qtd": 52, "Tempo médio": "04:30:01", "Último Lançamento": "15:26:36", "Status": "Em execução"},
        {"IP": 222, "Qtd": 12, "Tempo médio": "04:31:03", "Último Lançamento": "14:12:32", "Status": "Verificar"},
        {"IP": 223, "Qtd": 23, "Tempo médio": "03:59:35", "Último Lançamento": "15:25:35", "Status": "Em execução"}
    ]

    # Cabeçalho
    header = [
        html.Th(col, style={
            "backgroundColor": "#27AE60",
            "color": "white",
            "padding": "4px",
            "fontSize": "12px",
            "lineHeight": "1.2"
        }) for col in dados[0].keys()
    ]

    # Linhas da tabela
    rows = [
        html.Tr([
            html.Td(str(valor), style={
                "padding": "4px",
                "fontSize": "12px",
                "lineHeight": "1.2",
                "textAlign": "center",
                "backgroundColor": "#F2F4F4" if i % 2 == 0 else "#E8F6F3"
            })
            for valor in linha.values()
        ]) for i, linha in enumerate(dados)
    ]

    # Montagem da tabela
    return html.Table([
        html.Thead(html.Tr(header)),
        html.Tbody(rows)
    ], style={
        "width": "100%",
        "borderCollapse": "collapse",
        "marginTop": "20px"
    })

def gerar_tabela_atualizacao_1():
    dados = [
        {"IP": 220, "Qtd": 32, "Tempo médio": "04:32:20", "Último Lançamento": "15:25:36", "Status": "Em execução"},
        {"IP": 221, "Qtd": 52, "Tempo médio": "04:30:01", "Último Lançamento": "15:26:36", "Status": "Em execução"},
        {"IP": 222, "Qtd": 12, "Tempo médio": "04:31:03", "Último Lançamento": "14:12:32", "Status": "Verificar"},
        {"IP": 223, "Qtd": 23, "Tempo médio": "03:59:35", "Último Lançamento": "15:25:35", "Status": "Em execução"}
    ]

    # Cabeçalho
    header = [
        html.Th(col, style={
            "backgroundColor": "#27AE60",
            "color": "white",
            "padding": "4px",
            "fontSize": "12px",
            "lineHeight": "1.2"
        }) for col in dados[0].keys()
    ]

    # Linhas da tabela
    rows = [
        html.Tr([
            html.Td(str(valor), style={
                "padding": "4px",
                "fontSize": "12px",
                "lineHeight": "1.2",
                "textAlign": "center",
                "backgroundColor": "#F2F4F4" if i % 2 == 0 else "#E8F6F3"
            })
            for valor in linha.values()
        ]) for i, linha in enumerate(dados)
    ]

    # Montagem da tabela
    return html.Table([
        html.Thead(html.Tr(header)),
        html.Tbody(rows)
    ], style={
        "width": "100%",
        "borderCollapse": "collapse",
        "marginTop": "20px"
    })

# Novo: função para gerar dados de lançamentos, aprovações e liberações
def gerar_lancamentos_aprovacoes_liberacoes():
    dias = pd.date_range(start=pd.Timestamp.today().replace(day=1), periods=10).strftime('%d/%b').tolist()
    lancamentos = [random.randint(20, 80) for _ in dias]
    aprovacoes = [random.randint(20, 80) for _ in dias]
    liberacoes = [random.randint(20, 80) for _ in dias]
    df = pd.DataFrame({
        "Dia": dias,
        "Lançamentos": lancamentos,
        "Aprovações": aprovacoes,
        "Liberações": liberacoes
    })
    return df

def gerar_atualizacao_mensal():
    meses = pd.date_range(start=pd.Timestamp.today().replace(month=1, day=1), periods=12, freq='MS').strftime('%b/%y').tolist()
    valores = [random.randint(500, 2000) for _ in meses]
    df = pd.DataFrame({"Mês": meses, "Atualizações": valores})
    return df

# Tabela com barra de progresso (somente na linha Total)
def gerar_tabela_atualizacao():
    status = ["Realizada", "Falta", "Total"]
    dados_atualizacao = [700, 900, 1600]
    dados_crl = [0, 1600, 1600]

    def barra_progresso(realizado, total):
        largura_realizado = int((realizado / total) * 100) if total > 0 else 0
        largura_falta = 100 - largura_realizado
        return html.Div([
            html.Div(style={
                "width": f"{largura_realizado}%",
                "height": "10px",
                "backgroundColor": "#27AE60",
                "borderRadius": "4px",
                "display": "inline-block"
            }),
            html.Div(style={
                "width": f"{largura_falta}%",
                "height": "10px",
                "backgroundColor": "#BDC3C7",
                "borderRadius": "4px",
                "display": "inline-block"
            })
        ], style={
            "width": "100%",
            "backgroundColor": "#E5E7E9",
            "borderRadius": "4px",
            "marginTop": "4px"
        })

    linhas = []
    for i in range(len(status)):
        row = [
            html.Td(status[i], style={
                "padding": "4px",
                "fontSize": "12px",
                "lineHeight": "1.2",
                "textAlign": "center",
                "backgroundColor": "#F2F4F4"
            })
        ]
        for dados in [dados_atualizacao, dados_crl]:
            celula = [
                html.P(str(dados[i]), style={"margin": "0", "fontSize": "12px", "fontWeight": "bold", "lineHeight": "1.2"})
            ]
            if status[i] == "Total":
                celula.append(barra_progresso(dados[0], dados[i]))
            row.append(html.Td(celula, style={
                "padding": "4px",
                "fontSize": "12px",
                "lineHeight": "1.2"
            }))
        linhas.append(html.Tr(row))

        header = html.Tr([
        html.Th("Status", style={
            "backgroundColor": "#27AE60", "color": "white", "padding": "4px", "fontSize": "12px", "lineHeight": "1.2"
        }),
        html.Th("Lançamento", style={
            "backgroundColor": "#27AE60", "color": "white", "padding": "4px", "fontSize": "12px", "lineHeight": "1.2"
        }),
        html.Th("Aprovação", style={
            "backgroundColor": "#27AE60", "color": "white", "padding": "4px", "fontSize": "12px", "lineHeight": "1.2"
        })
    ])

    return html.Table([
        html.Thead(header),
        html.Tbody(linhas)
    ], style={"width": "100%", "borderCollapse": "collapse", "marginTop": "20px"})

# Tabela com barra de progresso (somente na linha Total)
def gerar_tabela_majoracao():
    status = ["Realizada", "Falta", "Total"]
    dados_lancamento = [200, 1017, 1217]
    dados_aprovacao = [0, 1217, 1217]
    dados_liberacao = [0, 1217, 1217]
    
    def barra_progresso(realizado, total):
        largura_realizado = int((realizado / total) * 100) if total > 0 else 0
        largura_falta = 100 - largura_realizado
        return html.Div([
            html.Div(style={
                "width": f"{largura_realizado}%",
                "height": "10px",
                "backgroundColor": "#27AE60",
                "borderRadius": "4px",
                "display": "inline-block"
            }),
            html.Div(style={
                "width": f"{largura_falta}%",
                "height": "10px",
                "backgroundColor": "#BDC3C7",
                "borderRadius": "4px",
                "display": "inline-block"
            })
        ], style={
            "width": "100%",
            "backgroundColor": "#E5E7E9",
            "borderRadius": "4px",
            "marginTop": "4px"
        })

    linhas = []
    for i in range(len(status)):
        row = [
            html.Td(status[i], style={
                "padding": "4px",
                "fontSize": "12px",
                "lineHeight": "1.2",
                "textAlign": "center",
                "backgroundColor": "#F2F4F4"
            })
        ]
        for dados in [dados_lancamento, dados_aprovacao, dados_liberacao]:
            celula = [
                html.P(str(dados[i]), style={"margin": "0", "textAlign": "center", "fontSize": "12px", "fontWeight": "bold", "lineHeight": "1.2"})
            ]
            if status[i] == "Total":
                celula.append(barra_progresso(dados[0], dados[i]))
            row.append(html.Td(celula, style={
                "padding": "4px",
                "fontSize": "12px",
                "lineHeight": "1.2"
            }))
        linhas.append(html.Tr(row))

    header = html.Tr([
        html.Th("Status", style={
            "backgroundColor": "#27AE60", "color": "white", "padding": "4px", "fontSize": "12px", "lineHeight": "1.2"
        }),
        html.Th("Lançamento", style={
            "backgroundColor": "#27AE60", "color": "white", "padding": "4px", "fontSize": "12px", "lineHeight": "1.2"
        }),
        html.Th("Aprovação", style={
            "backgroundColor": "#27AE60", "color": "white", "padding": "4px", "fontSize": "12px", "lineHeight": "1.2"
        }),
        html.Th("Liberação", style={
            "backgroundColor": "#27AE60", "color": "white", "padding": "4px", "fontSize": "12px", "lineHeight": "1.2"
        })
    ])

    return html.Table([
        html.Thead(header),
        html.Tbody(linhas)
    ], style={"width": "100%", "borderCollapse": "collapse", "marginTop": "20px"})

def gerar_tabela_erros_rpa():
    dados_erros = [
        {"Erro": "Etapa 1 – Falha no Lançamento", "Qtd.": 32},
        {"Erro": "Etapa 1 – Proposta não encontrada", "Qtd.": 12},
        {"Erro": "Etapa 2 – Limite não se encontra nessa fase", "Qtd.": 22},
        {"Erro": "Etapa 3 – Outros erros", "Qtd.": 17},
        {"Erro": "Etapa 2 – Não encontrado", "Qtd.": 32},
        {"Erro": "Etapa 4 – Falha de comunicação", "Qtd.": 15},
        {"Erro": "Etapa 5 – Problema no sistema", "Qtd.": 10}
    ]

    header = html.Thead(
        html.Tr([
            html.Th("Erro ⚠️", style={
                "backgroundColor": "#E67E22",
                "color": "white",
                "padding": "4px",
                "fontSize": "12px",
                "lineHeight": "1.2",
                "position": "sticky",
                "top": "0",
                "zIndex": "1"
            }),
            html.Th("Qtd.", style={
                "backgroundColor": "#E67E22",
                "color": "white",
                "padding": "4px",
                "fontSize": "12px",
                "lineHeight": "1.2",
                "position": "sticky",
                "top": "0",
                "zIndex": "1"
            })
        ])
    )

    rows = [
        html.Tr([
            html.Td(item["Erro"], style={
                "padding": "4px",
                "fontSize": "12px",
                "lineHeight": "1.2",
                "backgroundColor": "#F2F4F4"
            }),
            html.Td(str(item["Qtd."]), style={
                "padding": "4px",
                "fontSize": "12px",
                "lineHeight": "1.2",
                "textAlign": "center",
                "backgroundColor": "#F2F4F4"
            })
        ]) for item in dados_erros
    ]

    table = html.Table([
        header,
        html.Tbody(rows)
    ], style={"width": "100%", "borderCollapse": "collapse"})

    return html.Div(table, style={
        "width": "100%",
        "maxHeight": "120px",  # Ajuste para alinhar com a tabela verde
        "overflowY": "auto",
        "border": "1px solid #ddd",
        "marginTop": "20px",
        "boxShadow": "2px 2px 5px rgba(0,0,0,0.1)"
    })

# Adicione esta função para gerar os cards de Aprovações e Tempo médio
def gerar_cards_aprovacoes():
    cards = []

    # Lista de cards para exibir (6 cards: 3 por linha)
    dados_cards = [
        ("12", "Aprovações"),
        ("19:30", "Tempo médio"),
        ("23525", "Majorações")
    ]

    for valor, titulo in dados_cards:
        card = html.Div([
            html.P(valor, style={"fontSize": "18px", "margin": "0", "color": "white", "fontWeight": "bold"}),
            html.P(titulo, style={"fontSize": "12px", "margin": "0", "color": "white"})
        ], style={
            "backgroundColor": "#0B5345",
            "padding": "10px",
            "borderRadius": "5px",
            "textAlign": "center",
            "width": "calc(33.33% - 20px)",  # Divide a linha em 3 cards com espaçamento
            "boxSizing": "border-box",
            "marginBottom": "10px"
        })
        cards.append(card)

    return html.Div(cards, style={
        "display": "flex",
        "flexWrap": "wrap",
        "gap": "10px",
        "justifyContent": "center",
        "width": "100%"
    })

