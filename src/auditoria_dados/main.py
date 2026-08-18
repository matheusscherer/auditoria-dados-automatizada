"""Ponto de entrada da auditoria de dados de vendas."""

import logging
import sys

from auditoria_dados.config import RegrasAuditoria
from auditoria_dados.loader import carregar_dados
from auditoria_dados.validators import executar_auditoria
from auditoria_dados.report import gerar_relatorio_texto

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def main() -> None:
    caminho = input("Caminho da planilha de vendas (.csv ou .xlsx): ").strip()
    if not caminho:
        logger.error("Caminho não informado.")
        sys.exit(1)

    try:
        df = carregar_dados(caminho)
        regras = RegrasAuditoria()
        relatorio = executar_auditoria(df, regras)
        gerar_relatorio_texto(relatorio)

        if relatorio["status"] != "OK":
            sys.exit(1)

    except Exception as e:
        logger.critical("Falha na auditoria: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
