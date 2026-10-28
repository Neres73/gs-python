# 🌊 Guia de Enchentes — Versão em Python

Programa de terminal com orientações básicas sobre enchentes: áreas de risco, sinais de alerta, ações de emergência e contatos de emergência, navegados por um menu.

Projeto da **Global Solution 2025 (FIAP)**, parte de Python. É a versão em terminal do [Guia de Enchentes em HTML, CSS e JavaScript](https://github.com/Neres73/gs-front-end).

---

## O que o programa faz

Mostra um menu e exibe o conteúdo da opção escolhida até a pessoa digitar `0`:

```
--- MENU PRINCIPAL ---
1. Ver Áreas de Risco
2. Ver Sinais de Alerta
3. Ver Ações de Emergência
4. Ver Contatos de Emergência
0. Sair da Aplicação
```

Exemplo da opção 4:

```
--- CONTATOS DE EMERGÊNCIA ---
- Bombeiros: 193
- Defesa Civil: 199
- SAMU (Ambulância): 192
```

Qualquer outra entrada mostra uma mensagem de opção inválida e volta ao menu.

## Conceitos praticados

- **Listas** para guardar áreas de risco, sinais de alerta e ações de emergência
- **Lista de dicionários** para os contatos (nome e número)
- **Laço `while`** para manter o menu aberto até a opção de sair
- **`if` / `elif` / `else`** para tratar cada opção e a entrada inválida
- **Laço `for`** e **f-strings** para listar o conteúdo

## Como rodar

Requisito: Python 3 (só biblioteca padrão).

```bash
git clone https://github.com/Neres73/gs-python.git
cd gs-python
python trabalho.py
```

---

Projeto acadêmico, desenvolvido por [Gustavo Neres](https://github.com/Neres73).
