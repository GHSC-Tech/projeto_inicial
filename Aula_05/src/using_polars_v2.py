import polars as pl
import time
from pathlib import Path

# Autor original: Koen Vossen
# Adaptado e aprimorado para compatibilidade com Polars ≥1.25 e melhor legibilidade.

DATA_PATH = Path("data/measurements.txt")

def create_polars_df(file_path: Path) -> pl.DataFrame:
    """
    Cria um DataFrame do Polars a partir de um arquivo CSV muito grande, 
    processando em modo streaming para eficiência de memória.
    """

    # Define o tamanho de chunk para o modo streaming (4 milhões de linhas por bloco)
    pl.Config.set_streaming_chunk_size(4_000_000)

    # Cria o LazyFrame (processamento preguiçoso)
    lf = (
        pl.scan_csv(
            file_path,
            separator=";",
            has_header=False
        )
        .rename({"column_1": "station", "column_2": "measure"})  # garante nomes legíveis
        .with_columns(pl.col("measure").cast(pl.Float64))         # garante tipo numérico
        .group_by("station")
        .agg(
            pl.col("measure").max().alias("max"),
            pl.col("measure").min().alias("min"),
            pl.col("measure").mean().alias("mean")
        )
        .sort("station")
    )

    # Executa o plano em modo streaming (eficiente em memória)
    df = lf.collect(engine="streaming")
    return df


if __name__ == "__main__":
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {DATA_PATH.resolve()}")

    print("🔄 Processando arquivo com Polars...")
    start_time = time.time()

    df = create_polars_df(DATA_PATH)

    elapsed = time.time() - start_time
    print(df.head(10))  # mostra as 10 primeiras linhas
    print(f"✅ Polars terminou em {elapsed:.2f} segundos — shape: {df.shape}")
