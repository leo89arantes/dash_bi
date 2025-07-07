from dash import callback, Output, Input
from utils.graphs import gerar_graficos_por_municipio, gerar_cards
from utils.ibge_api import obter_populacao, obter_pib

@callback(
    Output("grafico-linha", "figure"),
    Output("grafico-pie", "figure"),
    Output("tabela-resultados", "data"),
    Output("tabela-resultados", "columns"),
    Input("filtro-municipio", "value"),
    Input("filtro-modalidade", "value")
)
def atualizar_graficos(municipio, modalidade):
    if not municipio or not modalidade:
        return {}, {}, [], []

    fig_linha, fig_pie, df_tabela = gerar_graficos_por_municipio(municipio, modalidade)

    if not df_tabela.empty:
        data = df_tabela.to_dict('records')
        columns = [{"name": col, "id": col} for col in df_tabela.columns]
    else:
        data = []
        columns = []

    return fig_linha, fig_pie, data, columns
