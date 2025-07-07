from sqlalchemy import create_engine
import pandas as pd


def connect_to_db():
    user = "root"
    password = ""
    host = "localhost"
    port = "3306"
    database = "projetos"

    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

    try:
        engine = create_engine(connection_string)
        print("✅ Conectado ao banco de dados!")
        return engine
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        return None
