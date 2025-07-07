import pandas as pd
import plotly.graph_objects as go
from data.queries import carregar_carteira

# 🔥 Dicionário global de modalidades
modalidade_dict = {
    'Empréstimos': 'VERBETE_160_OPERACOES_DE_CREDITO',
    'Empréstimos e TD': '161_EMPRES_E_TIT_DESCONTADOS',
    'Financiamentos': '162_FINANCIAMENTOS',
    'Financiamentos Custeio e Investimento': '163_FIN_RURAIS_AGRICUL_CUST_INVEST',
    'Financiamentos Agroindustriais': '167_FINANCIAMENTOS_AGROINDUSTRIAIS',
    'Financiamento Imobiliário': '169_FINANCIAMENTOS_IMOBILIARIOS',
    'Outras operações de Crédito': '171_OUTRAS_OPERACOES_DE_CREDITO',
    'Outros Créditos': '172_OUTROS_CREDITOS',
    'Provisão': '174_PROV_P_OPER_CREDITOS'
}




def listar_municipios_disponiveis():
    df = carregar_carteira()
    if df.empty:
        return []

    municipios = sorted(df['MUNICIPIO'].dropna().unique())
    return municipios

import dash_bootstrap_components as dbc
from dash import html


def gerar_cards(populacao, pib, empresas=0, outro=0):
    cards = dbc.Col([
        dbc.Card(dbc.CardBody([html.H4(f"{populacao:,}".replace(",", ".")), html.P("População")]),
                 color="primary", inverse=True),
        dbc.Card(dbc.CardBody([html.H4(f"{pib/1_000_000:.1f} M"), html.P("PIB")]),
                 color="success", inverse=True),
        dbc.Card(dbc.CardBody([html.H4(f"{empresas} mil"), html.P("Empresas")]),
                 color="danger", inverse=True),
        dbc.Card(dbc.CardBody([html.H4(f"{outro} mil"), html.P("Outro")]),
                 color="warning", inverse=True),
    ], width=2)

    return cards


def gerar_graficos_por_municipio(municipio, modalidade):
    df = carregar_carteira()

    if df.empty:
        return go.Figure(), go.Figure(), pd.DataFrame()

    df['DATA_BASE'] = pd.to_datetime(df['DATA_BASE'], errors='coerce')

    # 🔍 Mapear modalidade para coluna
    modalidade_dict = {
        'Empréstimos e TD': '161_EMPRES_E_TIT_DESCONTADOS',
        'Financiamentos': '162_FINANCIAMENTOS',
        'Financiamentos Custeio e Investimento': '163_FIN_RURAIS_AGRICUL_CUST_INVEST',
        'Financiamentos Agroindustriais': '167_FINANCIAMENTOS_AGROINDUSTRIAIS',
        'Financiamento Imobiliário': '169_FINANCIAMENTOS_IMOBILIARIOS',
        'Outras operações de Crédito': '171_OUTRAS_OPERACOES_DE_CREDITO',
        'Outros Créditos': '172_OUTROS_CREDITOS',
        'Provisão': '174_PROV_P_OPER_CREDITOS'
    }

    if modalidade not in modalidade_dict:
        print(f"⚠️ Modalidade inválida: {modalidade}")
        return go.Figure(), go.Figure(), pd.DataFrame()

    coluna_modalidade = modalidade_dict[modalidade]

    # 🔍 Filtrar município
    df_municipio = df[df['MUNICIPIO'].str.upper() == municipio.upper()]

    if df_municipio.empty:
        return go.Figure(), go.Figure(), pd.DataFrame()

    # 🔥 Filtrar instituições com soma > 0
    soma_por_inst = df_municipio.groupby('NOME_INSTITUICAO')[coluna_modalidade].sum().reset_index()
    instituicoes_validas = soma_por_inst[soma_por_inst[coluna_modalidade] > 0]['NOME_INSTITUICAO'].tolist()

    df_municipio = df_municipio[df_municipio['NOME_INSTITUICAO'].isin(instituicoes_validas)]

    if df_municipio.empty:
        return go.Figure(), go.Figure(), pd.DataFrame()

    # 📈 Gráfico de linha
    df_agg = df_municipio.groupby(['DATA_BASE', 'NOME_INSTITUICAO'])[coluna_modalidade].sum().reset_index()

    fig_linha = go.Figure()

    for inst in df_agg['NOME_INSTITUICAO'].unique():
        df_inst = df_agg[df_agg['NOME_INSTITUICAO'] == inst]

        fig_linha.add_trace(go.Scatter(
            x=df_inst['DATA_BASE'],
            y=df_inst[coluna_modalidade],
            mode='lines+markers',
            name=inst
        ))

    fig_linha.update_layout(
        title=f"Evolução - {modalidade} - {municipio}",
        xaxis_title="Data",
        yaxis_title="Valor (R$)",
        template="plotly_white",
        showlegend=False
    )

    # 🎯 Gráfico de rosca
    ultimo_mes = df_municipio['DATA_BASE'].max()

    df_pie = df_municipio[df_municipio['DATA_BASE'] == ultimo_mes] \
        .groupby('NOME_INSTITUICAO')[coluna_modalidade].sum().reset_index()

    df_pie = df_pie[df_pie[coluna_modalidade] > 0]

    fig_pie = go.Figure(data=[go.Pie(
        labels=df_pie['NOME_INSTITUICAO'],
        values=df_pie[coluna_modalidade],
        hole=0.5,
        textinfo='none'
    )])

    fig_pie.update_layout(
        title=f"Participação no mês {ultimo_mes.strftime('%m/%Y')} - {modalidade}",
        template="plotly_white",
        showlegend=False
    )

    # 📑 Tabela
    df_tabela = df_pie.rename(columns={
        'NOME_INSTITUICAO': 'Instituição',
        coluna_modalidade: 'Valor Op. Crédito'
    })

    df_tabela['Valor Op. Crédito'] = df_tabela['Valor Op. Crédito'].apply(
        lambda x: f"R$ {x:,.0f}".replace(",", ".")
    )

    return fig_linha, fig_pie, df_tabela
