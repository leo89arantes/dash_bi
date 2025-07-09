from dash import dcc, html, Input, Output
from app import app
from components.sidebar import sidebar
from utils import callbacks_share_mercado, callbacks_carteira_cobranca 
from pages import home, monitoramento_rpa, share_mercado, carteira_cartao, carteira_cobranca, carteira_credito, carteira_seguros, carteira_sipag, carteira_consorcio, carteira_previdencia, carteira_depositos, carteira_orcamento

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    html.Div(
        id="page-content",
        style={"margin-left": "18rem", "margin-right": "2rem", "padding": "2rem 1rem"}
    ),
])

# 🔁 Roteamento entre páginas
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/monitoramento-rpa":
        return monitoramento_rpa.layout
    elif pathname == "/share-mercado":
        return share_mercado.layout
    elif pathname == "/carteira-cartao":
        return carteira_cartao.layout
    elif pathname == "/carteira-cobranca":
        return carteira_cobranca.layout
    elif pathname == "/carteira-credito":
        return carteira_credito.layout
    elif pathname == "/carteira-seguros":
        return carteira_seguros.layout
    elif pathname == "/carteira-sipag":
        return carteira_sipag.layout
    elif pathname == "/carteira-consorcio":
        return carteira_consorcio.layout
    elif pathname == "/carteira-previdencia":
        return carteira_previdencia.layout
    elif pathname == "/carteira-depositos":
        return carteira_depositos.layout
    elif pathname == "/carteira-orcamento":
        return carteira_orcamento.layout
    return html.H1("404: Página não encontrada")

if __name__ == "__main__":
    app.run(debug=True, port=8888)
