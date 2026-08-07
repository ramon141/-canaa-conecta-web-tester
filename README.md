# Conecta Canaã — Testes Funcionais Automatizados

Suíte de testes funcionais automatizados do sistema web Conecta Canaã, plataforma
de gestão de ocorrências urbanas da Prefeitura Municipal de Canaã dos Carajás (PA).

Os testes seguem o protocolo de documentação da norma IEEE 829-2008 e são analisados
segundo a adequação funcional da ISO/IEC 25010. Trata-se do material de apoio do
artigo *"Planejamento, Execução e Análise de Testes de Funcionalidade no Sistema
Conecta Canaã"*.

## Ambiente

| Componente | Versão |
|---|---|
| Python | 3.10 |
| Selenium | 4.21.0 |
| selenium-wire | 5.1.0 |
| pytest | 8.3.2 |
| pytest-html-reporter | 0.2.9 |
| ChromeDriver | provisionado por `chromedriver-autoinstaller` 0.6.4 |
| Sistema operacional | Ubuntu 22.04 |
| Navegador | Google Chrome |

## Instalação

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Configuração

Os testes leem as credenciais e os parâmetros esperados de variáveis de ambiente.
Copie o arquivo de exemplo e preencha com os dados do **ambiente de homologação**:

```bash
cp .env.example .env
```

O arquivo `.env` está no `.gitignore` e **não deve ser versionado**. Use exclusivamente
contas de teste do ambiente de homologação — nunca credenciais de produção.

## Execução

```bash
pytest --html-report=./report
```

O relatório HTML é gravado em `report/`, junto com o `output.json` das execuções.

Para executar um caso específico:

```bash
pytest test_login.py
```

## Correspondência entre scripts e casos de teste

| Script | Função | Caso de teste |
|---|---|---|
| `test_controller_report_executor.py` | `test_controller_report_executor` | TC 01 (adicionar parecer), TC 02 e TC 03 (visualização pelo executor) |
| `test_login.py` | `test_login` | TC 04 (login com credenciais válidas) |
| `test_login.py` | `test_login_invalid_credentials` | TC 05 (login com credenciais inválidas) |
| `test_register_user.py` | `test_register_user` | TC 06 (cadastrar novo usuário) |
| `test_register_user.py` | `test_register_existing_user` | TC 07 (cadastrar usuário já existente) |
| `test_occurrence_no_location.py` | `test_occurrence_no_location_with_filter` | TC 08 (filtro de busca por código) |
| `test_occurrence_no_location.py` | `test_occurrence_no_location_with_invalid_filter` | TC 09 (busca com código inexistente) |
| `test_dashboard.py` | `test_occurrences_open` | TC 10 (ocorrências em aberto) |
| `test_dashboard.py` | `test_occurrence_attendance` | TC 11 (ocorrências concluídas) |
| `test_occurrence_no_location.py` | `test_occurrence_no_location` | TC 12 (ocorrências sem localização) |

Os doze casos de teste possuem função automatizada correspondente.

## Módulos auxiliares

- `browser.py` — inicialização e configuração do WebDriver
- `login.py` — rotina de autenticação reutilizada pelos testes
- `register_user.py` — cadastro de usuário com dados sintéticos (Faker)
- `register_report.py` — inclusão e leitura de parecer técnico
- `dashboard.py` — leitura dos indicadores do painel
- `complaint.py` — manipulação de ocorrências

## Licença e uso

Material acadêmico. Os testes devem ser executados exclusivamente em ambiente de
homologação, sem interferência sobre dados reais do município.
