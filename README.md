# CVM Fundamentalist Analysis

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

