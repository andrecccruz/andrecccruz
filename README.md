# 👨🏻‍💻 André

*Automação com Python · Web scraping · OCR · Ferramentas locais*

Escrevo ferramentas que trocam rotina manual por script: consultas em lote em portais públicos, leitura de documentos por OCR e aplicações locais que geram planilhas e relatórios. Gosto de coisas que rodam na máquina de quem usa, aguentam falhas no meio do caminho e não escondem o que fizeram.

📫 [acallou@outlook.com](mailto:acallou@outlook.com)

---

### 🚀 Projetos

| Projeto | O que faz | Stack |
|---|---|---|
| [**consulta_debitos_spu**](https://github.com/andrecccruz/consulta_debitos_spu) | Consulta em lote os débitos de imóveis da União no portal da SPU a partir de uma lista de RIPs. Opcionalmente traz o endereço oficial do cadastro. Retoma de onde parou e grava parciais a cada lote. | Python, requests, BeautifulSoup, openpyxl |
| [**conferir_rip_spu**](https://github.com/andrecccruz/conferir_rip_spu) | Lê por OCR as notificações de débito da SPU digitalizadas, extrai RIP, processo, CPF/CNPJ e endereço, valida dígitos verificadores e cruza com uma planilha-base. Roda 100% offline. | Python, Tesseract, OpenCV, PyMuPDF |
| [**iptu_lote**](https://github.com/andrecccruz/iptu_lote_info) | Consulta em lote de débitos de IPTU nos portais de prefeituras (Paulista, Recife, Jaboatão, Ipojuca, Rio de Janeiro), com resolução de CAPTCHA e saída padronizada por município. *Código privado; o link leva à página do projeto.* | Python, requests, Selenium, 2Captcha |
| [**comparador-contratos**](https://github.com/andrecccruz/comparador-contratos) | Compara um contrato devolvido com o modelo padrão, cláusula a cláusula, e gera relatório HTML/PDF/Excel, contraproposta em Word com marcações e nota de risco. Tudo local. | Python, Flask |
| [**rotina**](https://github.com/andrecccruz/rotina) | Rastreador de hábitos com tarefas, timer de foco, calendário e gráficos de evolução em SVG. Roda 100% local, com IA opcional que reaproveita respostas para não gastar tokens; inclui testes e guia de deploy com Docker. | Python, Flask, SQLite, Docker |
| [**feira**](https://github.com/andrecccruz/feira) | Controle de gastos de supermercado a partir do QR Code da NFC-e: busca o XML na SEFAZ, organiza os itens numa planilha e mostra um painel com gráficos. | Python, Flask, Chart.js, zxing-cpp |

> Os dois projetos da SPU se complementam: o `conferir_rip_spu` tira os RIPs das cartas e o `consulta_debitos_spu` consulta os débitos deles.

### 🧩 Como costumo construir

- **Lote com retomada:** processamento em blocos, parciais salvas e continuação de onde parou depois de Ctrl+C, queda de rede ou bloqueio do portal
- **Saída padronizada:** planilhas com abas de resumo, detalhe e controle e um `STATUS` claro por linha
- **Configuração separada do código:** `config.example.json` documentado, chaves em variável de ambiente e nada sensível no repositório
- **Gravação segura:** backup antes de alterar a planilha de origem e escrita atômica
- **Testes offline:** parsers validados com páginas salvas e portais simulados antes de rodar ao vivo

### 🛠️ Tecnologias e áreas

<img align="left" alt="Python" title="Python" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
<img align="left" alt="Bash" title="Bash / Shell Script" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg" />
<img align="left" alt="Linux" title="Linux" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg" />
<img align="left" alt="Windows" title="Windows" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/windows11/windows11-original.svg" />
<img align="left" alt="Selenium" title="Selenium" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" />
<img align="left" alt="Flask" title="Flask" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" />
<img align="left" alt="pandas" title="pandas" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" />
<img align="left" alt="HTML" title="HTML" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" />
<img align="left" alt="CSS" title="CSS" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" />
<img align="left" alt="JavaScript" title="JavaScript" width="30px" style="padding-right: 10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" />

<br/>
<br/>

![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract%20OCR-3C3C3C?style=flat)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![openpyxl](https://img.shields.io/badge/openpyxl-217346?style=flat&logo=microsoftexcel&logoColor=white)
![Excel VBA](https://img.shields.io/badge/Excel%20VBA-217346?style=flat&logo=microsoftexcel&logoColor=white)
![Power Automate](https://img.shields.io/badge/Power%20Automate-0066FF?style=flat&logo=powerautomate&logoColor=white)
![Azure OpenAI](https://img.shields.io/badge/Azure%20OpenAI-0078D4?style=flat)
![Claude](https://img.shields.io/badge/Claude%20API-D97757?style=flat&logo=anthropic&logoColor=white)

- **Web scraping e RPA:** portais públicos com sessão, CAPTCHA e WAF; Selenium onde `requests` não basta
- **OCR e documentos:** extração de PDFs e imagens, validação de dígitos verificadores, geração de Word e PDF
- **Dados e relatórios:** pandas, openpyxl, dashboards HTML offline em arquivo único
- **IA aplicada:** integração de LLMs (Azure OpenAI, Claude e APIs compatíveis com OpenAI) como recurso opcional, como a análise de contratos no `comparador-contratos`, o assistente de gastos no `feira` e as sugestões de prioridade no `rotina`; uso de assistentes de código no desenvolvimento e na revisão
- **Aplicações locais:** Flask servindo interface em HTML/JS, empacotamento para Windows, Docker para rodar em servidor
- **Microsoft 365:** Excel VBA e Power Automate para rotinas de escritório
- **Sistemas:** Linux no dia a dia, Windows, Bash/CMD, noções de redes
