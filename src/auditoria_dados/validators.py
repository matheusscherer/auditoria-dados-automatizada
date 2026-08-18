"""Validações de integridade dos dados de vendas."""

from typing import List, Dict, Any

import pandas as pd
import logging

from auditoria_dados.config import RegrasAuditoria

logger = logging.getLogger(__name__)


def validar_colunas_obrigatorias(df: pd.DataFrame, regras: RegrasAuditoria) -> List[str]:
    faltantes = [c for c in regras.colunas_obrigatorias if c not in df.columns]
    if faltantes:
        return [f"Colunas obrigatórias ausentes: {faltantes}"]
    return []


def validar_valores_negativos(df: pd.DataFrame, regras: RegrasAuditoria) -> List[str]:
    erros = []
    for col in ["quantidade", "valor_unitario", "valor_total"]:
        if col not in df.columns:
            continue
        negativos = df[df[col] < regras.valor_minimo]
        for _, row in negativos.iterrows():
            erros.append(
                f"Valor negativo em '{col}' (id={row.get('id', '?')}): {row[col]}"
            )
    return erros


def validar_consistencia_valor_total(df: pd.DataFrame, regras: RegrasAuditoria) -> List[str]:
    """Verifica se valor_total ≈ quantidade * valor_unitario."""
    erros = []
    if not all(c in df.columns for c in ["quantidade", "valor_unitario", "valor_total"]):
        return erros

    for _, row in df.iterrows():
        esperado = row["quantidade"] * row["valor_unitario"]
        diferenca = abs(row["valor_total"] - esperado)
        if diferenca > regras.tolerancia_arredondamento:
            erros.append(
                f"Inconsistência de valor_total (id={row.get('id', '?')}): "
                f"esperado {esperado:.2f}, encontrado {row['valor_total']:.2f}"
            )
    return erros


def validar_datas(df: pd.DataFrame) -> List[str]:
    erros = []
    if "data" not in df.columns:
        return erros

    datas = pd.to_datetime(df["data"], errors="coerce")
    invalidas = df[datas.isna()]
    for _, row in invalidas.iterrows():
        erros.append(f"Data inválida (id={row.get('id', '?')}): {row.get('data')}")
    return erros


def executar_auditoria(df: pd.DataFrame, regras: RegrasAuditoria | None = None) -> Dict[str, Any]:
    """Executa todas as validações e retorna relatório."""
    if regras is None:
        regras = RegrasAuditoria()

    logger.info("Iniciando auditoria de integridade...")

    todos_erros: List[str] = []
    todos_erros.extend(validar_colunas_obrigatorias(df, regras))
    todos_erros.extend(validar_valores_negativos(df, regras))
    todos_erros.extend(validar_consistencia_valor_total(df, regras))
    todos_erros.extend(validar_datas(df))

    relatorio = {
        "total_registros": len(df),
        "total_erros": len(todos_erros),
        "status": "OK" if not todos_erros else "FALHAS_ENCONTRADAS",
        "erros": todos_erros,
    }

    if not todos_erros:
        logger.info("Auditoria concluída com sucesso. Nenhum erro encontrado.")
    else:
        logger.warning("Auditoria concluída com %d erro(s).", len(todos_erros))

    return relatorio
