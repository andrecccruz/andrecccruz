# André

Faço software para rotinas que hoje são feitas na mão: contratos conferidos linha a linha, débitos consultados imóvel por imóvel em portal público, relatório de obra preenchido no papel. Quase tudo em Python, rodando na máquina de quem usa, com o resultado final em planilha, PDF ou Word.

📫 [acallou@outlook.com](mailto:acallou@outlook.com)

<table>
<tr>
<td valign="top" width="58%">

### 🧰 O que já resolvi

**[comparador-contratos](https://github.com/andrecccruz/comparador-contratos)**<br>
Contrato voltou do fornecedor com mudanças? Compara com o modelo cláusula a cláusula, dá nota de risco e gera a contraproposta em Word com marcas de revisão.<br>
<sub>`Python` `Flask` `difflib` `openpyxl`</sub>

**[diario_obras](https://github.com/andrecccruz/diario_obras)**<br>
Relatório Diário de Obra pelo celular no canteiro: fotos, equipe, clima e assinaturas viram PDF e relatórios de homem-hora. ~450 testes e CI.<br>
<sub>`Python` `Flask` `SQLite` `Playwright`</sub>

**[consulta_debitos_spu](https://github.com/andrecccruz/consulta_debitos_spu)** + **[conferir_rip_spu](https://github.com/andrecccruz/conferir_rip_spu)**<br>
Notificações da SPU digitalizadas viram dados por OCR, e os débitos de cada imóvel são consultados em lote, retomando de onde parou.<br>
<sub>`Python` `Tesseract` `OpenCV` `requests`</sub>

**[feira](https://github.com/andrecccruz/feira)**<br>
Aponta a webcam para o QR Code da nota fiscal e a compra entra numa planilha com painel de gastos, usando o XML oficial da SEFAZ.<br>
<sub>`Python` `Flask` `zxing-cpp` `openpyxl`</sub>

**[rotina](https://github.com/andrecccruz/rotina)**<br>
Hábitos, tarefas e timer de foco num app local, com IA opcional que reaproveita respostas para não gastar tokens.<br>
<sub>`Python` `Flask` `SQLite` `Docker`</sub>

**[garmin_smart_trainer_mcp](https://github.com/andrecccruz/garmin_smart_trainer_mcp)**<br>
Servidor MCP: o Claude Code monta a semana de treino e ela chega no relógio Garmin do atleta, só depois de aprovada.<br>
<sub>`Python` `MCP` `Podman`</sub>

**[tv-tcl](https://github.com/andrecccruz/tcl-tv-vb)**<br>
Tira anúncios e apps de fábrica de uma TV TCL só com ADB, sem root, e troca a tela inicial por um launcher próprio.<br>
<sub>`Java` `Android` `ADB` `PowerShell`</sub>

**iptu_lote** <sub>(código privado)</sub><br>
Débitos de IPTU em lote em cinco prefeituras, passando por CAPTCHA, com saída padronizada por município.<br>
<sub>`Python` `Selenium` `2Captcha`</sub>

</td>
<td valign="top" width="42%">

### 🔄 Mexido recentemente

<!-- recentes inicio -->
- [tcl-tv-vb](https://github.com/andrecccruz/tcl-tv-vb) · 29/10/2026
- [garmin_smart_trainer_mcp](https://github.com/andrecccruz/garmin_smart_trainer_mcp) · 26/10/2026
- [diario_obras](https://github.com/andrecccruz/diario_obras) · 23/10/2026
- [rotina](https://github.com/andrecccruz/rotina) · 22/10/2026
- [consulta_debitos_spu](https://github.com/andrecccruz/consulta_debitos_spu) · 20/10/2026
<!-- recentes fim -->

<sub>Lista atualizada todo dia por um script Python no GitHub Actions.</sub>

### 📐 Em todos os projetos

- Lote que retoma de onde parou
- Dados ficam na máquina; IA é opcional e vem desligada
- Backup antes de gravar, escrita atômica
- Chaves fora do código e do log
- Testado com páginas salvas antes de ir ao portal de verdade
- Instala com dois cliques, sem pedir administrador

### 🛠️ Ferramentas

Python · Flask · SQLite · pandas · openpyxl · Selenium · Playwright · Tesseract · OpenCV · Docker · Azure OpenAI · Claude API · Excel VBA · Power Automate · Linux

</td>
</tr>
</table>
