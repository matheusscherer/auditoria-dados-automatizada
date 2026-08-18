# auditoria-dados-automatizada

Sistema automatizado em Python para **auditoria de dados de vendas**, geração de relatórios e validação de integridade.

> Projeto de portfólio focado em qualidade de dados, regras de negócio e boas práticas de engenharia.

---

## O que o sistema valida

- Colunas obrigatórias presentes
- Valores negativos (quantidade, valor unitário, valor total)
- Consistência matemática: `valor_total ≈ quantidade × valor_unitario`
- Datas inválidas

Gera relatório textual com o status e detalhes dos erros encontrados.

---

## Estrutura

```text
auditoria-dados-automatizada/
├── src/
│   └── auditoria_dados/
│       ├── __init__.py
│       ├── config.py
│       ├── loader.py
│       ├── validators.py
│       ├── report.py
│       └── main.py
├── tests/
│   └── test_validators.py
├── data/examples/
│   └── vendas_exemplo.csv
├── .github/workflows/ci.yml
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## Instalação

```bash
git clone https://github.com/matheusscherer/auditoria-dados-automatizada.git
cd auditoria-dados-automatizada

python -m venv .venv
source .venv/bin/activate

pip install -e ".[dev]"
```

---

## Como usar

```bash
python -m auditoria_dados.main
# ou
auditoria-dados
```

Informe o caminho de uma planilha (CSV/Excel) com as colunas:

`id, data, produto, quantidade, valor_unitario, valor_total`

Exemplo de dados em `data/examples/vendas_exemplo.csv`.

---

## Testes

```bash
pytest -v
```

---

## Stack

- Python 3.10+
- Pandas
- pytest + GitHub Actions

---

**Matheus Scherer** · [github.com/matheusscherer](https://github.com/matheusscherer)

MIT License
