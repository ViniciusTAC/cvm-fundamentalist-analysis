<!-- <!-- # CVM Fundamentalist Analysis

Este projeto realiza a coleta, extração, armazenamento e análise de dados fundamentalistas disponibilizados pela CVM (Comissão de Valores Mobiliários), com foco em empresas brasileiras de capital aberto.

## 📦 Escopo do Projeto

- **Dados coletados**: FCA, DFPs, ITRs, IPE e FRE (apenas dados cadastrais)
- **Objetivo**: Armazenamento e visualização de dados financeiros estruturados
- **Utilização**: Análises financeiras automatizadas e suporte à tomada de decisão

## 🧱 Estrutura do Projeto

```
src/
├── collectors/        # Scripts de coleta e download dos arquivos da CVM
├── extractor/         # Processamento e extração de dados dos arquivos
├── models/            # Definições das entidades de dados
├── service/           # Serviços que interpretam e transformam os dados
├── utils/             # Funções utilitárias (logger, helpers)
└── main.py            # Ponto de entrada da aplicação
```

## 🚀 Como usar

### Pré-requisitos

- Python 3.11+
- SQLite3

### Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/cvm-fundamentalist-analysis.git
cd cvm-fundamentalist-analysis
```

Crie e ative o ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Configuração do banco de dados

Execute o script SQL localizado em `sqlite-projeto` para criar o esquema necessário no SQLite:

```bash
python script-sqlite.sql
```

Configure as credenciais do banco no arquivo de configuração apropriado (normalmente em `src/utils` ou variáveis de ambiente).

### Execução

Rode o projeto usando:

```bash
python src/main.py
```

## 🛠 Tecnologias Utilizadas

- Python
- BeautifulSoup
- Requests
- Pandas
- SQLAlchemy
- SQLite3
- Tkinter

## 📄 Licença

Este projeto está licenciado sob a MIT License.

---
 -->

<!-- # CVM Fundamentalist Analysis

Este projeto realiza a coleta, extração, armazenamento e análise de dados fundamentalistas disponibilizados pela CVM (Comissão de Valores Mobiliários), com foco em empresas brasileiras de capital aberto.

## 📦 Escopo do Projeto

- **Fontes de dados**: FCA, DFPs, ITRs, IPE e FRE (dados cadastrais e financeiros)
- **Objetivo**: Estruturar e armazenar dados financeiros para análises fundamentalistas automatizadas
- **Utilização**: Geração de base de dados para suporte à decisão no mercado financeiro

## 🧱 Estrutura do Projeto

```text
src/
├── collectors/        # Coleta e download dos arquivos da CVM
├── extractor/         # Extração e transformação dos dados
├── models/            # Modelos das entidades e estrutura dos dados
├── service/           # Lógica de processamento e tratamento
├── utils/             # Funções auxiliares (logger, helpers, etc.)
└── main.py            # Script principal de execução
```

## 🚀 Como usar

### Pré-requisitos

- Python 3.11 ou superior
- SQLite3 ou MySQL (ajustável via repositórios)
- `pip` para instalação de dependências

### Instalação

```bash
git clone https://github.com/seu-usuario/cvm-fundamentalist-analysis.git
cd cvm-fundamentalist-analysis
pip install -r requirements.txt
python src/main.py
```

## 💾 Requisitos de Sistema

- **Espaço em disco**: pelo menos **16 GB** livres para armazenar arquivos CSV e extrair os dados
- **Memória RAM**: recomenda-se **8 GB ou mais**, pois o processamento pode ser intensivo

## 🔄 Fluxo de Execução

1. Coleta e download dos arquivos da CVM (.zip)
2. Extração e processamento dos dados CSV
3. Inserção em banco de dados relacional (SQLite3)
4. Disponibilização dos dados para análises futuras

## 📄 Licença

Este projeto é open-source sob a licença MIT. --> -->


# CVM Fundamentalist Analysis

Este projeto realiza a coleta, extração, armazenamento e análise de dados fundamentalistas disponibilizados pela CVM (Comissão de Valores Mobiliários), com foco em empresas brasileiras de capital aberto.

## 📦 Escopo do Projeto

- Fontes de dados: FCA, DFPs, ITRs, IPE e FRE (dados cadastrais e financeiros)
- Objetivo: Estruturar e armazenar dados financeiros para análises fundamentalistas automatizadas
- Utilização: Geração de base de dados para suporte à decisão no mercado financeiro

## 🧱 Estrutura do Projeto

```text
src/
├── collectors/        # Coleta e download dos arquivos da CVM
├── extractor/         # Extração e transformação dos dados
├── models/            # Modelos das entidades e estrutura dos dados
├── service/           # Lógica de processamento e tratamento
├── repository/        # Controle de conexão e inserção no banco
├── utils/             # Funções auxiliares (logger, helpers)
└── main.py            # Script principal de execução
```

## 🚀 Como usar

### Pré-requisitos

- Python 3.11 ou superior
- SQLite3 (ou MySQL, se adaptado)
- pip (gerenciador de pacotes Python)

### Instalação

```bash
git clone https://github.com/seu-usuario/cvm-fundamentalist-analysis.git
cd cvm-fundamentalist-analysis
pip install -r requirements.txt
```

### Execução

O script principal aceita argumentos opcionais para controle de log e detalhamento:

```bash
python src/main.py --debug     # Executa com log detalhado (nível DEBUG)
python src/main.py --verbose   # Mostra mensagens adicionais no console
```

Sem parâmetros, executa normalmente:

```bash
python src/main.py
```


Execute o script principal:

```bash
python src/main.py
```

Durante a execução, as etapas de processamento são exibidas no terminal com mensagens de status.

## 🐞 Logging e Depuração

O sistema utiliza um mecanismo robusto de logging que registra os eventos em arquivos separados por sucesso e erro:

- Logs de sucesso: `logs/logs_insercao/AAAA-MM-DD/sucesso.log`
- Logs de erro: `logs/logs_insercao/AAAA-MM-DD/erro.log`

Esses arquivos permitem identificar:
- Quais registros foram inseridos com sucesso
- Em quais etapas ocorreram falhas
- Qual foi a causa do erro (ex.: problemas de encoding, valores ausentes, falhas de chave primária)

### Exemplos de mensagens úteis nos logs:

```text
INFO - Registro salvo com sucesso: Empresa XPTO, CNPJ 00.000.000/0001-00
ERROR - Erro na etapa Empresas: [Errno 2] No such file or directory: ...
```

## 🔎 Como depurar

- Verifique primeiro o `erro.log` mais recente (dentro da pasta com data atual).
- Utilize prints temporários ou breakpoints em `src/main.py` e nos arquivos de `service/` para investigar transformações nos dados.
- Para rodar uma etapa específica manualmente, edite o `main.py` comentando as etapas que não deseja executar.

## 💾 Requisitos de Sistema

- Espaço em disco: **mínimo 16 GB** livres para armazenar os arquivos CSV da CVM
- Memória RAM: **8 GB ou mais** recomendados para evitar travamentos durante o parsing

## 🔄 Fluxo de Execução

1. Coleta e extração dos arquivos da CVM (.zip/.csv)
2. Leitura e tratamento dos dados
3. Inserção no banco SQLite
4. Registro em logs de sucesso/erro

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).