# 🚛 Gestão de Pátio Logístico — Projeto com Python e SQL

![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![SQL Server](https://img.shields.io/badge/SQL%20Server-2019-red)
![Licença](https://img.shields.io/badge/licença-MIT-green)

---

## 📌 Sobre o Projeto

Este projeto simula o dia a dia de um **pátio logístico**, onde caminhões chegam, permanecem por um período e depois saem. O objetivo é identificar gargalos operacionais e avaliar o cumprimento do SLA (tempo máximo permitido dentro do pátio).

A ideia é demonstrar, na prática, como **dados podem ser usados para otimizar operações logísticas** — unindo habilidades em Python, SQL e análise de negócio.

---

## 🎯 O que este projeto faz?

Com um script em Python, o sistema gera dados fictícios de **50 caminhões**, com:

- Placa do veículo
- Horário de entrada
- Horário de saída
- Tempo total de permanência (em minutos)
- Status: dentro ou fora do SLA (3 horas)

Esses dados podem ser analisados no **SQL Server** para responder perguntas como:

- ✅ Quantos caminhões cumpriram o prazo?
- ❌ Quais foram os maiores atrasos?
- ⏱️ Qual o tempo médio de permanência no pátio?
- 🚨 Quais veículos merecem atenção da gestão?

---

## 🛠️ Ferramentas utilizadas

| Ferramenta | Finalidade |
| :--- | :--- |
| 🐍 **Python (Pandas)** | Geração automatizada dos dados |
| 📊 **Matplotlib** | Criação do gráfico de distribuição por SLA |
| 📁 **Excel / CSV** | Armazenamento e importação dos dados |
| 🗄️ **SQL Server** | Análise e consultas estruturadas |
| 📂 **GitHub** | Versionamento e compartilhamento do projeto |

---

## 📁 Estrutura do Projeto
