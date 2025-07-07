import requests
from data.queries import carregar_carteira


# 🔍 Buscar população
def obter_populacao(codigo_municipio):
    url = f'https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/{codigo_municipio}'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return dados['projecao']['populacao']
    return None


# 🔍 Buscar PIB (último ano)
def obter_pib(codigo_municipio):
    url = f'https://apisidra.ibge.gov.br/values/t/5938/n6/{codigo_municipio}/v/37/p/last/c11255/90707'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        valor = dados[1]['V']
        return float(valor.replace('.', '').replace(',', '.'))
    return None


# 🔍 (Opcional) Buscar outras informações

mapeamento_cod_ibge = {
    'BELO HORIZONTE': '3106200',
    'SAO SEBASTIAO DA GRAMA': '3549401',
    'POCOS DE CALDAS': '3151800',
    'MUZAMBINHO': '3144102',
    # 🔥 Inclui os municípios que estão no seu df
}


def listar_municipios_e_codigos():
    df = carregar_carteira()

    municipios = df['MUNICIPIO'].dropna().str.upper().unique()

    # 🔥 Aqui você faz o merge com seu dicionário de códigos IBGE
    resultado = []

    for municipio in municipios:
        codigo = mapeamento_cod_ibge.get(municipio, None)
        if codigo:
            resultado.append({'municipio': municipio, 'codigo_ibge': codigo})
        else:
            print(f"⚠️ Código IBGE não encontrado para {municipio}")

    return resultado

def buscar_codigo_municipio(municipio_nome):
    municipio_nome = municipio_nome.upper()
    return mapeamento_cod_ibge.get(municipio_nome, None)
