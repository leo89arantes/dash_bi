from dash.dependencies import Input, Output
from dash import html, dcc, dash_table
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

from app import app

# Função para gerar dados de exemplo para a tabela principal
def generate_table_data():
    data = {
        'PA': [1, 2, 3, 4, 5, 5, 5, 7, 2, 3, 4, 5, 97],
        'Cooperado': ['Cooperado LTDA 01'] * 13,
        'Qtd Vencidos': [79265, 79907, 80596, 81178, 81619, 82172, 82466, 82742, 82854, 83177, 83615, 83976, 84329],
        'Valor Vencidos': [60268, 60651, 61069, 54357, 54459, 54686, 54837, 55282, 54766, 55586, 55673, 56847, 55966],
        'Qtd a Vencer': [70.57, 71.29, 70.27, 62.17, 61.86, 61.71, 61.55, 61.46, 61.36, 61.19, 61.14, 61.14, 61.14],
        'Valor a Vencer': [25925, 25901, 25909, 26256, 25764, 26305, 26643, 26676, 26473, 26749, 26667, 26454, 26676],
        'Qtd Baixa': [43.02, 42.70, 42.43, 48.30, 48.10, 48.10, 48.40, 48.39, 4.90, 47.13, 47.90, 47.66, 47.66],
        'Valor Baixa': [5.45, 5.10, 5.46, 5.91, 5.68, 6.21, 5.91, 5.07, 5.07, 4.66, 4.49, 5.20, 5.20],
        'Qtd Total': [11731, 11192, 11067, 11739, 11150, 12632, 12889, 12483, 12899, 11095, 12753, 14250, 14323],
        'Valor Total': [3282, 3091, 3337, 3215, 3093, 3394, 3239, 2805, 2805, 2921, 2502, 2843, 2912],
        'Prazo Médio': [260, 227, 186, 164, 149, 156, 170, 178, 178, 191, 106, 182, 215]
    }
    return pd.DataFrame(data)

# Função para gerar dados de exemplo para os gráficos
def generate_graph_data():
    dates = pd.to_datetime(['2024-05', '2024-06', '2024-07', '2024-08', '2024-09', '2024-10', '2024-11', '2024-12', '2025-01', '2025-02', '2025-03', '2025-04', '2025-05'])
    boletos_emitidos = [60000, 61000, 59000, 54000, 53000, 53500, 54000, 55000, 54500, 56000, 55500, 57000, 56500]
    percent_emissao_credito = [70, 71, 72, 65, 64, 63, 62, 61, 60, 61, 62, 63, 64]
    contas_compras_cr = [26000, 26500, 27000, 25500, 25000, 25200, 25400, 25600, 25800, 26000, 26200, 26400, 26600]
    percent_ativacao_credito = [45, 46, 47, 48, 47, 46, 45, 44, 43, 44, 45, 46, 47]

    df_boletos = pd.DataFrame({
        'Date': dates,
        'Boletos Emitidos': boletos_emitidos,
        '% Emissão de Crédito': percent_emissao_credito
    })

    df_mortalidade = pd.DataFrame({
        'Date': dates,
        'Contas com compras no CR': contas_compras_cr,
        '% Ativação Crédito': percent_ativacao_credito
    })
    return df_boletos, df_mortalidade

# Função para gerar dados de exemplo para os gráficos de rosca
def generate_donut_data():
    return {
        'qtd_emitidos': 137453,
        'qtd_liquidado': 117720,
        'valor_emitido': 161131535,
        'valor_liquidado': 135343686
    }

# Função para gerar dados de exemplo para a tabela de metas
def generate_metas_data():
    data = {
        'Metas': ['Projeto 123', 'Gestão de Metas'],
        'Realizadas': [200, 0],
        'Falta': [1017, 1217],
        'Total': [1217, 1217]
    }
    return pd.DataFrame(data)

# Função para gerar dados de exemplo para a aba Liquidação
def generate_liquidacao_data():
    return {
        'liq_cooperativa': 32235,
        'liq_rede_externa': 10265,
        'liq_sicoob': 4235,
        'valor_emitido_mes': 161131535,
        'valor_liquidado_mes': 135343686,
        'valor_emitido_mes_2': 161131535
    }

def generate_liquidacao_graph_data():
    dates = pd.to_datetime(['2024-05', '2024-06', '2024-07', '2024-08', '2024-09', '2024-10', '2024-11', '2024-12', '2025-01', '2025-02', '2025-03', '2025-04', '2025-05'])
    qtd_cooperativa = [10000, 11000, 9000, 8000, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000]
    qtd_rede_externa = [5000, 5500, 4500, 4000, 3500, 3750, 4000, 4250, 4500, 4750, 5000, 5250, 5500]
    qtd_sicoob = [2000, 2200, 1800, 1600, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200]

    valor_cooperativa = [1000000, 1100000, 900000, 800000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000, 1050000, 1100000]
    valor_rede_externa = [500000, 550000, 450000, 400000, 350000, 375000, 400000, 425000, 450000, 475000, 500000, 525000, 550000]
    valor_sicoob = [200000, 220000, 180000, 160000, 140000, 150000, 160000, 170000, 180000, 190000, 200000, 210000, 220000]

    df_qtd = pd.DataFrame({
        'Date': dates,
        'Cooperativa': qtd_cooperativa,
        'Rede Externa': qtd_rede_externa,
        'Sicoob': qtd_sicoob
    })

    df_valor = pd.DataFrame({
        'Date': dates,
        'Cooperativa': valor_cooperativa,
        'Rede Externa': valor_rede_externa,
        'Sicoob': valor_sicoob
    })
    return df_qtd, df_valor

def generate_resultado_data():
    # Datas dos últimos 12 meses
    datas = pd.date_range(end=pd.Timestamp.today(), periods=12, freq='M')
    receita = np.random.randint(80000, 120000, size=12)
    despesa = np.random.randint(50000, 90000, size=12)
    resultado = receita - despesa
    df = pd.DataFrame({
        'Data': datas.strftime('%Y-%m'),
        'Receita': receita,
        'Despesa': despesa,
        'Resultado': resultado
    })
    # Variação Mensal (MoM)
    df['Receita_MoM'] = df['Receita'].pct_change().fillna(0) * 100
    df['Despesa_MoM'] = df['Despesa'].pct_change().fillna(0) * 100
    # Variação Anual (YoY)
    df['Receita_YoY'] = df['Receita'].pct_change(periods=12).fillna(0) * 100
    df['Despesa_YoY'] = df['Despesa'].pct_change(periods=12).fillna(0) * 100
    return df

# Callbacks para a aba Resultado
@app.callback(
    Output('tabela-cobranca', 'children'),
    Input('input-pa', 'value'),
    Input('input-ano-mes', 'value'),
    Input('input-modalidade', 'value')
)
def update_table(pa, ano_mes, modalidade):
    df = generate_table_data()
    # Aqui você pode adicionar a lógica de filtragem com base nos inputs
    # Por enquanto, retorna a tabela completa
    return dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'padding': '5px'},
        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'}
    )

@app.callback(
    Output('grafico-boletos-emitidos', 'figure'),
    Input('input-pa', 'value'),
    Input('input-ano-mes', 'value'),
    Input('input-modalidade', 'value')
)
def update_boletos_chart(pa, ano_mes, modalidade):
    df_boletos, _ = generate_graph_data()
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_boletos['Date'],
        y=df_boletos['Boletos Emitidos'],
        name='Boletos Emitidos',
        marker_color='teal'
    ))
    fig.add_trace(go.Scatter(
        x=df_boletos['Date'],
        y=df_boletos['% Emissão de Crédito'],
        name='% Emissão de Crédito',
        mode='lines+markers',
        yaxis='y2',
        line=dict(color='purple')
    ))
    fig.update_layout(
        xaxis_title="Data",
        yaxis_title="Boletos Emitidos",
        yaxis2=dict(
            title='% Emissão de Crédito',
            overlaying='y',
            side='right'
        ),
        legend_title="Legenda",
        hovermode="x unified"
    )
    return fig

@app.callback(
    Output('grafico-mortalidade-carteira', 'figure'),
    Input('input-pa', 'value'),
    Input('input-ano-mes', 'value'),
    Input('input-modalidade', 'value')
)
def update_mortalidade_chart(pa, ano_mes, modalidade):
    _, df_mortalidade = generate_graph_data()
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_mortalidade['Date'],
        y=df_mortalidade['Contas com compras no CR'],
        name='Contas com compras no CR',
        marker_color='teal'
    ))
    fig.add_trace(go.Scatter(
        x=df_mortalidade['Date'],
        y=df_mortalidade['% Ativação Crédito'],
        name='% Ativação Crédito',
        mode='lines+markers',
        yaxis='y2',
        line=dict(color='purple')
    ))
    fig.update_layout(
        xaxis_title="Data",
        yaxis_title="Contas com compras no CR",
        yaxis2=dict(
            title='% Ativação Crédito',
            overlaying='y',
            side='right'
        ),
        legend_title="Legenda",
        hovermode="x unified"
    )
    return fig

@app.callback(
    Output('grafico-rosca-qtd', 'figure'),
    Output('grafico-rosca-valor', 'figure'),
    Input('input-pa', 'value'),
    Input('input-ano-mes', 'value'),
    Input('input-modalidade', 'value')
)
def update_donut_charts(pa, ano_mes, modalidade):
    data = generate_donut_data()

    fig_qtd = go.Figure(data=[go.Pie(labels=['Emitidos', 'Liquidado'], values=[data['qtd_emitidos'], data['qtd_liquidado']], hole=.7)])
    fig_qtd.update_layout(margin=dict(l=0, r=0, t=0, b=0), showlegend=False)

    fig_valor = go.Figure(data=[go.Pie(labels=['Emitido', 'Liquidado'], values=[data['valor_emitido'], data['valor_liquidado']], hole=.7)])
    fig_valor.update_layout(margin=dict(l=0, r=0, t=0, b=0), showlegend=False)

    return fig_qtd, fig_valor

@app.callback(
    Output('tabela-metas', 'children'),
    Input('input-pa', 'value'),
    Input('input-ano-mes', 'value'),
    Input('input-modalidade', 'value')
)
def update_metas_table(pa, ano_mes, modalidade):
    df_metas = generate_metas_data()
    return dash_table.DataTable(
        id='metas-table',
        columns=[{"name": i, "id": i} for i in df_metas.columns],
        data=df_metas.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'padding': '5px'},
        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'}
    )

@app.callback(
    Output('grafico-rosca-qtd-liq', 'figure'),
    Output('grafico-rosca-valor-liq', 'figure'),
    Input('input-pa-liq', 'value'),
    Input('input-ano-mes-liq', 'value'),
    Input('input-modalidade-liq', 'value')
)
def update_liquidacao_donut_charts(pa, ano_mes, modalidade):
    data = generate_liquidacao_data()

    fig_qtd_liq = go.Figure(data=[go.Pie(labels=['Cooperativa', 'Rede Externa', 'Sicoob'], values=[data['liq_cooperativa'], data['liq_rede_externa'], data['liq_sicoob']], hole=.7)])
    fig_qtd_liq.update_layout(margin=dict(l=0, r=0, t=0, b=0), showlegend=False)

    fig_valor_liq = go.Figure(data=[go.Pie(labels=['Emitido', 'Liquidado'], values=[data['valor_emitido_mes'], data['valor_liquidado_mes']], hole=.7)])
    fig_valor_liq.update_layout(margin=dict(l=0, r=0, t=0, b=0), showlegend=False)

    return fig_qtd_liq, fig_valor_liq

@app.callback(
    Output('grafico-qtd-liquidacao', 'figure'),
    Output('grafico-valor-liquidacao', 'figure'),
    Input('input-pa-liq', 'value'),
    Input('input-ano-mes-liq', 'value'),
    Input('input-modalidade-liq', 'value')
)
def update_liquidacao_bar_charts(pa, ano_mes, modalidade):
    df_qtd, df_valor = generate_liquidacao_graph_data()

    fig_qtd_bar = px.bar(df_qtd, x='Date', y=['Cooperativa', 'Rede Externa', 'Sicoob'], title='Qtd de Títulos emitidos por Local de Liquidação')
    fig_qtd_bar.update_layout(barmode='stack')

    fig_valor_bar = px.bar(df_valor, x='Date', y=['Cooperativa', 'Rede Externa', 'Sicoob'], title='Valor de Títulos emitidos por Local de Liquidação')
    fig_valor_bar.update_layout(barmode='stack')

    return fig_qtd_bar, fig_valor_bar

@app.callback(
    Output('grafico-receita-12m', 'figure'),
    Input('tabs', 'active_tab')
)
def update_grafico_receita_12m(active_tab):
    if active_tab != 'aba-3':
        return go.Figure()
    df = generate_resultado_data()
    fig = px.bar(df, x='Data', y='Receita', title='Receita dos últimos 12 meses', labels={'Receita': 'Receita (R$)'})
    fig.update_layout(xaxis_title='Mês', yaxis_title='Receita (R$)')
    return fig

@app.callback(
    Output('grafico-despesa-12m', 'figure'),
    Input('tabs', 'active_tab')
)
def update_grafico_despesa_12m(active_tab):
    if active_tab != 'aba-3':
        return go.Figure()
    df = generate_resultado_data()
    fig = px.bar(df, x='Data', y='Despesa', title='Despesa dos últimos 12 meses', labels={'Despesa': 'Despesa (R$)'}, color_discrete_sequence=['#d9534f'])
    fig.update_layout(xaxis_title='Mês', yaxis_title='Despesa (R$)')
    return fig

@app.callback(
    Output('grafico-resultado-12m', 'figure'),
    Input('tabs', 'active_tab')
)
def update_grafico_resultado_12m(active_tab):
    if active_tab != 'aba-3':
        return go.Figure()
    df = generate_resultado_data()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Data'], y=df['Resultado'], mode='lines+markers', name='Resultado', line=dict(color='green')))
    fig.update_layout(title='Resultado dos últimos 12 meses', xaxis_title='Mês', yaxis_title='Resultado (R$)')
    return fig

@app.callback(
    Output('tabela-evolucao-receita-despesa', 'children'),
    Input('tabs', 'active_tab')
)
def update_tabela_evolucao_receita_despesa(active_tab):
    if active_tab != 'aba-3':
        return html.Div()
    df = generate_resultado_data()
    # Formatar variações
    df['Receita_MoM'] = df['Receita_MoM'].map(lambda x: f"{x:.1f}%")
    df['Despesa_MoM'] = df['Despesa_MoM'].map(lambda x: f"{x:.1f}%")
    df['Receita_YoY'] = df['Receita_YoY'].map(lambda x: f"{x:.1f}%")
    df['Despesa_YoY'] = df['Despesa_YoY'].map(lambda x: f"{x:.1f}%")
    return dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center', 'padding': '5px'},
        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'}
    )

def get_ranking_contrato_ativo():
    data = [
        ["PA16", 1626, 265, 16.2977], ["PA26", 1325, 165, 12.4528], ["PA19", 1124, 135, 12.0107], ["PA47", 1652, 198, 11.9855],
        ["PA18", 1265, 135, 10.6719], ["PA10", 1465, 132, 9.0102], ["PA24", 1623, 135, 8.3179], ["PA14", 1652, 126, 7.6271],
        ["PA22", 1362, 98, 7.1953], ["PA27", 4659, 298, 6.3962], ["PA15", 2642, 165, 6.2453], ["PA23", 2123, 132, 6.2176],
        ["PA21", 4652, 269, 5.7825], ["PA28", 3265, 174, 5.3292], ["PA8", 3262, 162, 4.9663], ["PA17", 3566, 165, 4.6270],
        ["PA11", 2969, 135, 4.5470], ["PA20", 5623, 250, 4.4460], ["PA25", 3652, 135, 3.6966], ["PA9", 4685, 168, 3.5859],
        ["PA2", 2653, 95, 3.5809], ["PA1", 3526, 88, 2.4957], ["PA97", 6595, 126, 1.9105], ["PA7", 3111, 55, 1.7679],
        ["PA5", 3265, 56, 1.7152], ["PA4", 2645, 43, 1.6257], ["PA3", 3652, 26, 0.7119], ["PA6", 3795, 26, 0.6851]
    ]
    df = pd.DataFrame(data, columns=["PA", "Cooperados", "Contatos ativos", "Proveitamento"])
    return df

def get_ranking_boletos():
    data = [
        ["PA6", 26, 646226, 2485484.6154], ["PA5", 56, 38465, 68687.5], ["PA3", 26, 15476, 59523.0769], ["PA7", 55, 29849, 54270.9091],
        ["PA1", 88, 26546, 30165.9091], ["PA2", 95, 26544, 27941.0526], ["PA15", 165, 38465, 23312.1212], ["PA11", 135, 29849, 22110.3704],
        ["PA14", 126, 26546, 21068.254], ["PA24", 135, 26544, 19662.2222], ["PA18", 135, 26541, 19660.0], ["PA19", 135, 26456, 19597.037],
        ["PA8", 162, 26546, 16386.4198], ["PA20", 250, 38465, 15386.0], ["PA28", 174, 26544, 15255.1724], ["PA4", 43, 4685, 10895.3488],
        ["PA27", 298, 29849, 10016.443], ["PA9", 168, 15476, 9211.9048], ["PA16", 265, 23415, 8835.8491], ["PA21", 269, 15476, 5753.1599],
        ["PA23", 132, 4685, 3549.2424], ["PA25", 135, 4685, 3470.3704], ["PA22", 98, 2984, 3044.898], ["PA97", 126, 2984, 2368.254],
        ["PA10", 132, 2654, 2010.6061], ["PA17", 165, 2984, 1808.4848], ["PA26", 165, 2356, 1427.8788], ["PA47", 198, 2654, 1340.404]
    ]
    df = pd.DataFrame(data, columns=["PA", "Contatos ativos", "Emissão", "Proveitamento"])
    return df

@app.callback(
    Output('tabela-ranking-contrato-ativo', 'children'),
    Input('tabs', 'active_tab')
)
def update_tabela_ranking_contrato_ativo(active_tab):
    if active_tab != 'aba-4':
        return html.Div()
    df = get_ranking_contrato_ativo()
    return dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center', 'padding': '5px'},
        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'}
    )

@app.callback(
    Output('tabela-ranking-boletos', 'children'),
    Input('tabs', 'active_tab')
)
def update_tabela_ranking_boletos(active_tab):
    if active_tab != 'aba-4':
        return html.Div()
    df = get_ranking_boletos()
    return dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'center', 'padding': '5px'},
        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'}
    )