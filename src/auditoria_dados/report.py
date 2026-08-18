"""Geração de relatório de auditoria."""

from pathlib import Path
from typing import Dict, Any
from datetime import datetime

import logging

logger = logging.getLogger(__name__)


def gerar_relatorio_texto(relatorio: Dict[str, Any], caminho: str = "relatorio_auditoria.txt") -> str:
    """Gera relatório em texto simples."""
    linhas = [
        "=" * 60,
        "RELATÓRIO DE AUDITORIA DE DADOS DE VENDAS",
        f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 60,
        f"Total de registros analisados: {relatorio['total_registros']}",
        f"Total de erros encontrados:    {relatorio['total_erros']}",
        f"Status: {relatorio['status']}",
        "-",
    ]

    if relatorio["erros"]:
        linhas.append("DETALHES DOS ERROS:")
        for i, erro in enumerate(relatorio["erros"], 1):
            linhas.append(f"  {i}. {erro}")
    else:
        linhas.append("Nenhum problema de integridade detectado.")

    linhas.append("=" * 60)
    conteudo = "\n".join(linhas)

    Path(caminho).write_text(conteudo, encoding="utf-8")
    logger.info("Relatório salvo em: %s", caminho)
    return caminho
