# Script para download de dados na CVM 
 Scripts para baixar, processar e analisar dados fundamentalistas da CVM, voltados para pesquisa e algoritmos de análise financeira.

---

### **Escopo do projeto**
   - Quais dados serão coletados (e.g., ITRs, DFIs, etc.)?

    FCA (geral), DFPs, ITRs, IPE e FRE (apenas dados cadastrais).


   - Como os dados serão utilizados (armazenamento, análise, visualização)?

    Será para armazenamento e visualização.


   - Quais são os pontos de entrada da API ou do site da CVM?

    Diretamente no site da CVM.
[CVM Dados - CIA ABERTA](https://dados.cvm.gov.br/dados/CIA_ABERTA/)

---

### 2. **Estruturar o projeto**
Organize o projeto em pastas e módulos, como mostrado abaixo:

```
cvm-fundamentalist-analysis/
├── data/                   # Armazenamento local (opcional)
├── src/                    # Código-fonte do projeto
│   ├── collectors/         # Classes para coleta de dados
│   │   ├── base_collector.py
│   │   ├── cvm_collector.py
│   ├── parsers/            # Classes para análise e transformação
│   │   ├── base_parser.py
│   │   ├── financial_parser.py
│   ├── models/             # Classes representando entidades (e.g., Empresa, Relatório)
│   │   ├── company.py
│   │   ├── report.py
│   ├── storage/            # Classes para salvar dados (e.g., banco de dados, CSV)
│   │   ├── database.py
│   │   ├── file_storage.py
│   ├── utils/              # Funções auxiliares (e.g., logs, validações)
│   │   ├── helpers.py
│   │   ├── logger.py
│   ├── main.py             # Ponto de entrada do programa
├── tests/                  # Testes unitários
├── README.md               # Documentação do projeto
├── requirements.txt        # Dependências do projeto
└── setup.py                # Configuração para pacotes (opcional)
```

---

### **Dependências**
Liste as bibliotecas no `requirements.txt`:

```
requests
unittest
```

---

### **Executar o projeto**
- Instale as dependências: `pip install -r requirements.txt`
- Execute o script principal: `python src/main.py`
