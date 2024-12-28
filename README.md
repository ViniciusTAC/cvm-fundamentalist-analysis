# Script para download de dados na CVM 
 Scripts para baixar, processar e analisar dados fundamentalistas da CVM, voltados para pesquisa e algoritmos de análise financeira.

---

### **Escopo do projeto**
   - Quais dados serão coletados (e.g., ITRs, DFIs, etc.)?
        - FCA (geral), DFPs, ITRs, IPE e FRE (apenas dados cadastrais).

<br>

   - Como os dados serão utilizados (armazenamento, análise, visualização)?
        - Será para armazenamento e visualização.

<br>

   - Quais são os pontos de entrada da API ou do site da CVM?
        - Diretamente no site da CVM. Link: [CVM Dados - CIA ABERTA](https://dados.cvm.gov.br/dados/CIA_ABERTA/)

---

### **Estruturar o projeto**
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



### **Executar o projeto**
- Instale as dependências: `pip install -r requirements.txt`
- Execute o script principal: `python src/main.py`

---

## Convenções de Commit

Siga as convenções abaixo ao fazer commits para manter a clareza e consistência no histórico do Git:

- **feat**: Para adicionar uma nova funcionalidade.
  - Exemplo: `feat: Adiciona o menu global da aplicação.`
  
- **fix**: Para corrigir um bug.
  - Exemplo: `fix: Resolve o problema que impedia o login.`
  
- **docs**: Para atualizar documentação.
  - Exemplo: `docs: Atualiza o README com instruções claras sobre comandos de testes unitários.`
  
- **style**: Para ajustes de formatação que não afetam o comportamento do código.
  - Exemplo: `style: Corrige formatação do código.`

- **refactor**: Para reorganizar o código sem alterar funcionalidades.
  - Exemplo: `refactor: Reestrutura o componente de tabela.`

- **test**: Para adicionar ou modificar testes.
  - Exemplo: `test: Adiciona testes de unidade para o componente de botão.`