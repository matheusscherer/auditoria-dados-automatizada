"""Testes das validações de auditoria."""

import pandas as pd
import pytest

from auditoria_dados.config import RegrasAuditoria
from auditoria_dados.validators import (
    validar_valores_negativos,
    validar_consistencia_valor_total,
    executar_auditoria,
)


@pytest.fixture
def df_ok():
    return pd.DataFrame([
        {"id": 1, "data": "2025-01-10", "produto": "A", "quantidade": 2, "valor_unitario": 10.0, "valor_total": 20.0},
        {"id": 2, "data": "2025-01-11", "produto": "B", "quantidade": 1, "valor_unitario": 15.5, "valor_total": 15.5},
    ])


@pytest.fixture
def df_com_erros():
    return pd.DataFrame([
        {"id": 1, "data": "2025-01-10", "produto": "A", "quantidade": -1, "valor_unitario": 10.0, "valor_total": -10.0},
        {"id": 2, "data": "2025-01-11", "produto": "B", "quantidade": 2, "valor_unitario": 10.0, "valor_total": 25.0},
    ])


def test_sem_erros(df_ok):
    relatorio = executar_auditoria(df_ok)
    assert relatorio["status"] == "OK"
    assert relatorio["total_erros"] == 0


def test_valores_negativos(df_com_erros):
    erros = validar_valores_negativos(df_com_erros, RegrasAuditoria())
    assert len(erros) >= 1


def test_inconsistencia_valor_total(df_com_erros):
    erros = validar_consistencia_valor_total(df_com_erros, RegrasAuditoria())
    assert any("Inconsistência" in e for e in erros)
