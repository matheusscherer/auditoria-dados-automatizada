"""Configurações da auditoria."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class RegrasAuditoria:
    """Regras de negócio para validação de integridade."""

    valor_minimo: float = 0.0
    colunas_obrigatorias: List[str] = field(
        default_factory=lambda: ["id", "data", "produto", "quantidade", "valor_unitario", "valor_total"]
    )
    tolerancia_arredondamento: float = 0.01  # diferença aceitável em valor_total
