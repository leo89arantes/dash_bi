from dash import callback, Output, Input
from utils.graphs_monitoramento_rpa import (
    gerar_grafico_renda,
    gerar_grafico_atualizacao_mensal,
    gerar_grafico_liberacao_mensal,
    gerar_grafico_lanc_aprov_lib
)

@callback(
    Output("grafico-renda", "figure"),
    Output("grafico-atualizacao-mensal", "figure"),
    Output("grafico-liberacao-mensal", "figure"),
    Output("grafico-lanc-aprov-lib", "figure"),
    Input("interval", "n_intervals")
)
def atualizar_graficos(n):
    return (
        gerar_grafico_renda(),
        gerar_grafico_atualizacao_mensal(),
        gerar_grafico_liberacao_mensal(),
        gerar_grafico_lanc_aprov_lib()
    )
