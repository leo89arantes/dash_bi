from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Div(
            html.Img(src="/assets/logo.png", style={'height': '60px'}),
            style={'textAlign': 'center'} 
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("RPA", href="/monitoramento-rpa", active="exact"),
                dbc.NavLink("Share Mercado", href="/share-mercado", active="exact"),
                dbc.NavLink("Cartão", href="/carteira-cartao", active="exact"),
                dbc.NavLink("Cobrança", href="/carteira-cobranca", active="exact"),
                dbc.NavLink("Crédito", href="/carteira-credito", active="exact"),
                dbc.NavLink("Depositos", href="/carteira-depositos", active="exact"),
                dbc.NavLink("Previdência", href="/carteira-previdencia", active="exact"),
                dbc.NavLink("Seguros", href="/carteira-seguros", active="exact"),
                dbc.NavLink("Sipag", href="/carteira-sipag", active="exact"),
                dbc.NavLink("Orçamento", href="/carteira-orcamento", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)
