from dash import html

def gerar_tabela_cartao_credito():
    # Cabeçalhos da tabela
    colunas = [
        "Mês", "Cooperados", "Contas Correntes", "Conta cartão com Limite", "% Emissão de crédito",
        "Contas com compras no CR", "% Ativação Crédito", "% Negada por Limite",
        "Quat. Trasações Negadas", "Contas com trasações Negadas", "Quant. Cessão"
    ]

    # Dados da tabela
    dados = [
        ["mai/24", 85400, 79265, 60268, "70,57%", 25925, "43,02%", "5,45%", 11731, 3282, 260],
        ["jun/24", 85080, 79907, 60651, "71,29%", 25901, "42,70%", "5,10%", 11192, 3091, 227],
        ["jul/24", 86902, 80596, 61069, "70,27%", 25909, "42,43%", "5,46%", 11067, 3337, 186],
        ["ago/24", 87437, 81178, 54357, "62,17%", 26256, "48,30%", "5,91%", 11739, 3215, 164],
        ["set/24", 88032, 81619, 54459, "61,86%", 25764, "47,31%", "5,68%", 11150, 3093, 149],
        ["out/24", 88622, 82172, 54686, "61,71%", 26305, "48,10%", "6,21%", 12632, 3394, 156],
        ["nov/24", 89099, 82466, 54837, "61,55%", 26453, "48,24%", "5,91%", 12889, 3239, 170],
        ["dez/24", 89498, 82854, 54766, "61,19%", 26473, "48,34%", "4,90%", 11587, 2685, 178],
        ["jan/25", 89955, 82742, 55282, "61,46%", 26749, "48,39%", "5,07%", 12483, 2805, 170],
        ["fev/25", 90592, 83177, 55586, "61,36%", 26199, "47,13%", "4,66%", 11095, 2591, 164],
        ["mar/25", 90990, 83615, 55673, "61,19%", 26667, "47,90%", "4,49%", 12753, 2502, 106],
        ["abr/25", 91410, 83976, 56847, "62,19%", 26454, "46,54%", "5,00%", 14250, 2843, 182],
        ["mai/25", 91535, 84329, 55966, "61,14%", 26676, "47,66%", "5,20%", 14323, 2912, 215],
    ]

    # Cabeçalho da tabela
    header = html.Tr([
        html.Th(col, style={
            "backgroundColor": "#00A091",
            "color": "white",
            "padding": "8px",
            "fontSize": "12px",
            "textAlign": "center",
            "border": "1px solid #ddd"
        }) for col in colunas
    ])

    # Corpo da tabela com alternância de cores
    body_rows = []
    for i, linha in enumerate(dados):
        bg_color = "#F9F9F9" if i % 2 == 0 else "#E8F6F3"
        row = html.Tr([
            html.Td(str(item), style={
                "padding": "8px",
                "fontSize": "12px",
                "textAlign": "center",
                "backgroundColor": bg_color,
                "border": "1px solid #ddd"
            }) for item in linha
        ])
        body_rows.append(row)

    # Tabela final com estilo responsivo
    return html.Div(
        html.Table(
            [html.Thead(header), html.Tbody(body_rows)],
            style={
                "width": "100%",
                "borderCollapse": "collapse",
                "boxShadow": "0 2px 6px rgba(0,0,0,0.1)",
            }
        ),
        style={"overflowX": "auto", "marginTop": "20px"}
    )
