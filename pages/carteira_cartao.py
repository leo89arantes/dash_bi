from dash import html, dcc, dash_table, register_page
from utils.componentes_tabelas import gerar_tabela_cartao_credito
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

register_page(__name__, path="/carteira-cartao", name="Cartão")

# Simulação de dados (substitua pelo real)
df = pd.DataFrame({
    "Mês": ["mai/24", "jun/24", "jul/24", "ago/24", "set/24", "out/24", "nov/24", "dez/24", "jan/25", "fev/25", "mar/25", "abr/25", "mai/25"],
    "Conta cartão com Limite": [60268, 60651, 61069, 61069, 61000, 62000, 62500, 62700, 62800, 62900, 63000, 64000, 55966],
    "% Emissão de crédito": [70.57, 71.29, 70.27, 62.43, 61.86, 61.71, 61.55, 61.46, 61.29, 61.13, 61.19, 62.00, 61.14],
    "Contas com compras no CR": [25925, 25090, 25640, 26305, 25764, 26453, 26453, 26749, 26669, 26657, 26594, 26456, 26576],
    "% Ativação Crédito": [43.02, 42.70, 42.43, 48.30, 47.31, 48.13, 48.24, 48.39, 47.09, 47.30, 46.65, 45.90, 47.66],
})

# Gráfico 1: Limite x Emissão
fig1 = px.bar(df, x="Mês", y="Conta cartão com Limite", labels={"value": "Qtd"}, barmode="group")
fig1.add_scatter(x=df["Mês"], y=df["% Emissão de crédito"], mode="lines+markers", name="% Emissão de crédito", yaxis="y2")

# Gráfico 2: Compras x Ativação
fig2 = px.bar(df, x="Mês", y="Contas com compras no CR", labels={"value": "Qtd"}, barmode="group")
fig2.add_scatter(x=df["Mês"], y=df["% Ativação Crédito"], mode="lines+markers", name="% Ativação Crédito", yaxis="y2")

# Layout da aba Base
aba_base = html.Div([
    html.H4("Indicadores de Cartão de Crédito"),
    html.Div([
        html.Div([
            html.H2("84.329", style={"color": "#00A091"}),
            html.P("Contas Correntes")
        ], style={"flex": "1", "padding": "10px", "border": "1px solid #e0e0e0", "borderRadius": "8px", "textAlign": "center", "boxShadow": "2px 2px 8px #ccc"}),

        html.Div([
            html.H2("55.966", style={"color": "#00A091"}),
            html.P("Contas com Limite")
        ], style={"flex": "1", "padding": "10px", "border": "1px solid #e0e0e0", "borderRadius": "8px", "textAlign": "center", "boxShadow": "2px 2px 8px #ccc"}),

        html.Div([
            html.H2("66,37%", style={"color": "#00A091"}),
            html.P("Emissão de Crédito")
        ], style={"flex": "1", "padding": "10px", "border": "1px solid #e0e0e0", "borderRadius": "8px", "textAlign": "center", "boxShadow": "2px 2px 8px #ccc"}),

        html.Div([
            html.H2("26.678", style={"color": "#00A091"}),
            html.P("Contas com Compras Crédito")
        ], style={"flex": "1", "padding": "10px", "border": "1px solid #e0e0e0", "borderRadius": "8px", "textAlign": "center", "boxShadow": "2px 2px 8px #ccc"}),
    ], style={"display": "flex", "gap": "10px", "marginBottom": "20px"}),

    dash_table.DataTable(
        columns=[{"name": col, "id": col} for col in df.columns],
        data=df.to_dict("records"),
        style_table={"overflowX": "auto"},
        style_cell={"fontSize": "12px", "textAlign": "center"}
    ),

    html.Hr(),

    html.Div([
        dcc.Graph(figure=fig1, style={"flex": "1", "marginRight": "10px"}),
        dcc.Graph(figure=fig2, style={"flex": "1"})
    ], style={"display": "flex"})
])

# Tabs com aba base preenchida
layout = html.Div([
    html.H1("Cartão de Crédito"),
    dbc.Tabs(
        [
            dbc.Tab(
                html.Div([
                    html.H4("Base de Indicadores", style={"marginTop": "20px"}),
                    gerar_tabela_cartao_credito()
                ]),
                label="Base",
                tab_id="aba-1",
                label_style={"color": "#00A091"},
                active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            dbc.Tab(html.P("Aba 2 aberta!"), label="Faturamento", tab_id="aba-2",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            dbc.Tab(html.P("Aba 3 aberta!"), label="Inadimplência", tab_id="aba-3",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            dbc.Tab(html.P("Aba 4 aberta!"), label="Ranking", tab_id="aba-4",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            dbc.Tab(html.P("Aba 5 aberta!"), label="Resultado", tab_id="aba-5",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),

            dbc.Tab(html.P("Aba 6 aberta!"), label="Propensos", tab_id="aba-6",
                    label_style={"color": "#00A091"}, active_label_style={"color": "#00A091", "fontWeight": "bold"}),
        ],
        id="tabs",
        active_tab="aba-1",
    )
])
