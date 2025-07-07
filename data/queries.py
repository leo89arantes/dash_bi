from data.connection import connect_to_db
import pandas as pd

QUERY_CARTEIRA = """
    SELECT
        DATA_BASE, UF, CODMUN, MUNICIPIO, 160_OPERACOES_DE_CREDITO, NOME_INSTITUICAO,
        AGEN_ESPERADAS, AGEN_PROCESSADAS, 161_EMPRES_E_TIT_DESCONTADOS,
        162_FINANCIAMENTOS, 163_FIN_RURAIS_AGRICUL_CUST_INVEST,
        167_FINANCIAMENTOS_AGROINDUSTRIAIS, 169_FINANCIAMENTOS_IMOBILIARIOS,
        171_OUTRAS_OPERACOES_DE_CREDITO, 172_OUTROS_CREDITOS,
        174_PROV_P_OPER_CREDITOS
    FROM projetos.dados_financeiros;
"""

def carregar_carteira():
    engine = connect_to_db()
    if engine is not None:
        df = pd.read_sql(QUERY_CARTEIRA, con=engine)
        df['DATA_BASE'] = pd.to_datetime(df['DATA_BASE'].astype(str), format='%Y%m')
        print("✅ Dados carregados!")
        return df
    else:
        print("❌ Conexão falhou, dados não carregados.")
        return None

