import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validar_integridade(dados):
    logging.info("Iniciando auditoria de integridade...")[span_0](start_span)[span_0](end_span)
    erros = []
    for registro in dados:
        if registro.get('valor', 0) < 0:
            erros.append(f"Erro: Valor negativo encontrado em {registro.get('id')}")
    if not erros:
        logging.info("Auditoria concluída com sucesso.")[span_1](start_span)[span_1](end_span)
    return erros

if __name__ == "__main__":
    dados_teste = [{'id': 1, 'valor': 100}, {'id': 2, 'valor': -50}]
    validar_integridade(dados_teste)
