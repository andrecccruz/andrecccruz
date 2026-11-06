"""Atualiza a lista "Mexido recentemente" do README do perfil.

Busca na API do GitHub os repositórios públicos ordenados pelo último push e
reescreve só o trecho entre os marcadores. Sem dependências externas.
Uso: python atualizar_readme.py  (GITHUB_TOKEN opcional, evita limite da API)
"""
import json
import os
import re
import urllib.request
from datetime import datetime
from pathlib import Path

USUARIO = "andrecccruz"
QUANTIDADE = 5
IGNORAR = {USUARIO, "sway_ricing", "iptu_lote_info"}
README = Path(__file__).with_name("README.md")
INICIO, FIM = "<!-- recentes inicio -->", "<!-- recentes fim -->"


def buscar_repos():
    url = f"https://api.github.com/users/{USUARIO}/repos?per_page=100&sort=pushed&type=owner"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def montar_lista(repos):
    linhas = []
    for repo in repos:
        if repo["name"] in IGNORAR or repo["fork"] or repo["archived"] or repo["private"]:
            continue
        data = datetime.fromisoformat(repo["pushed_at"].replace("Z", "+00:00"))
        linha = f"- [{repo['name']}]({repo['html_url']}) · {data:%d/%m/%Y}"
        if repo.get("description"):
            linha += f"<br><sub>{repo['description']}</sub>"
        linhas.append(linha)
        if len(linhas) == QUANTIDADE:
            break
    return "\n".join(linhas)


def substituir(texto, lista):
    padrao = re.compile(re.escape(INICIO) + r".*?" + re.escape(FIM), re.DOTALL)
    if not padrao.search(texto):
        raise SystemExit("Marcadores não encontrados no README.")
    return padrao.sub(lambda _: f"{INICIO}\n{lista}\n{FIM}", texto)


def main():
    atual = README.read_text(encoding="utf-8")
    novo = substituir(atual, montar_lista(buscar_repos()))
    if novo != atual:
        README.write_text(novo, encoding="utf-8")
        print("README atualizado.")
    else:
        print("Nada mudou.")


if __name__ == "__main__":
    main()
