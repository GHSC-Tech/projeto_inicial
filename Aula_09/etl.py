import pandas as pd
import os
import glob

from utils_log import log_decorator

# uma função de extract que le e consolida os json

@log_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# uma função que transforma

@log_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Valor"]
    return df


#parametro para definir se será "csv" ou "parquet" ou "os dois"

@log_decorator
def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    parametro para definir se será "csv" ou "parquet" ou "os dois"
    """
    for formato in format_saida:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet", index=False)

@log_decorator
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, format_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    date_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(date_frame_calculado, format_saida=["csv", "parquet"])

# uma função que da load em csv ou parquet

# if __name__ == "__main__":
#     pasta_argumento: str = 'data'
#     data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
#     date_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
#     formato_de_saida: list = ["csv", "parquet"]
#     carregar_dados(date_frame_calculado, format_saida=["csv", "parquet"])

# pasta = 'data'
# arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
# df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
# df_total = pd.concat(df_list, ignore_index=True)

# print(df_list)