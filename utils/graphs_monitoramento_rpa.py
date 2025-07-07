import plotly.express as px
from data.transform import gerar_series_temporais, gerar_liberacao_mensal, gerar_atualizacao_mensal, gerar_lancamentos_aprovacoes_liberacoes


def gerar_grafico_renda():
    df = gerar_series_temporais()
    fig = px.bar(
        df, x="Dia", y="Atualizações",
        color_discrete_sequence=["#00b7ff"]
    )
    fig.update_layout(margin=dict(t=30, b=30, l=20, r=20),
                      xaxis_title=None, yaxis_title=None)
    return fig

def gerar_grafico_atualizacao_mensal():
    df = gerar_atualizacao_mensal()
    fig = px.bar(
        df, x="Mês", y="Atualizações",
        color_discrete_sequence=["#2ca02c"]
    )
    fig.update_layout(margin=dict(t=30, b=30, l=20, r=20),
                      xaxis_title=None, yaxis_title=None)
    return fig

def gerar_grafico_liberacao_mensal():
    df = gerar_liberacao_mensal()
    fig = px.bar(
        df, x="Mês", y="Liberações",
        color_discrete_sequence=["#2ca02c"]
    )
    fig.update_layout(margin=dict(t=30, b=30, l=20, r=20),
                      xaxis_title=None, yaxis_title=None)
    return fig

def gerar_grafico_lanc_aprov_lib():
    df = gerar_lancamentos_aprovacoes_liberacoes()
    fig = px.bar(
        df, x="Dia", y=["Lançamentos", "Aprovações", "Liberações"],
        color_discrete_map={
            "Lançamentos": "#7DCEA0",
            "Aprovações": "#1E8449",
            "Liberações": "#884EA0"
        }
    )
    fig.update_layout(
        barmode="group",
        margin=dict(t=10, b=30, l=20, r=20),
        title=None,
        xaxis_title=None,
        yaxis_title=None
    )
    return fig
