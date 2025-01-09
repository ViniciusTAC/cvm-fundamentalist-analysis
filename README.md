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
Directory structure:
└── cvm-fundamentalist-analysis/
    ├── README.md
    ├── guia.md
    ├── requirements.txt
    ├── setup.py
    ├── logs/
    └── src/
        ├── main.py
        ├── collectors/
        │   └── coletor_cvm.py
        ├── models/
        │   ├── demonstrativo_financeiro.py
        │   ├── empresas.py
        │   ├── formulario_referencia.py
        │   ├── grupo_demonstrativo_financeiro.py
        │   ├── informacao_trimestral.py
        │   ├── parecer_demonstrativo.py
        │   ├── parecer_trimestral.py
        │   ├── periodicos_eventuais.py
        │   └── planos_contas.py
        ├── parsers/
        │   ├── base_parser.py
        │   └── financial_parser.py
        ├── storage/
        │   ├── database.py
        │   └── file_storage.py
        └── utils/
            ├── helpers.py
            └── logger.py
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