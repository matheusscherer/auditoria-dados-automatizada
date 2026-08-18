"""Carregamento de dados de vendas."""

from pathlib import Path

import pandas as pd
import logging

logger = logging.getLogger(__name__)


def carregar_dados(caminho: str) -> pd.DataFrame:
    """Carrega planilha de vendas (CSV ou Excel)."""
    path = Path(caminho)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path, encoding="utf-8-sig")
    elif path.suffix.lower() in (".xlsx", ".xls"):
        df = pd.read_excel(path, engine="openpyxl")
    else:
        raise ValueError(f"Formato não suportado: {path.suffix}")

    logger.info("Dados carregados: %d registros", len(df))
    return df
