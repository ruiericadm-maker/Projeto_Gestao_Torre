# Relatório de Análise — Gestão de Pátio Logístico

## Resumo Executivo

Este relatório apresenta os resultados da simulação de operação de pátio logístico, com foco no cumprimento do SLA de 3 horas (180 minutos).

## Metodologia

- Foram gerados **50 registros fictícios**
- Cada registro contém: placa, horário de entrada, horário de saída, tempo de permanência e status
- O status é classificado como:
  - ✅ "Dentro do SLA" — permanência ≤ 180 min
  - ❌ "Fora do SLA" — permanência > 180 min

## Resultados Obtidos

| Indicador | Valor |
| :--- | :--- |
| **Total de caminhões** | 50 |
| **Dentro do SLA** | 34 (68%) |
| **Fora do SLA** | 16 (32%) |
| **Média de permanência** | 168 min (~2h48) |
| **Maior permanência** | 536 min (~8h56) |

## Análise dos Gargalos

Os 5 maiores tempos de permanência foram:

| Placa | Tempo (min) | Status |
| :--- | :--- | :--- |
| KZD 7 B 18 | 536 | Fora do SLA |
| NMR 7 D 89 | 475 | Fora do SLA |
| EHW 1 J 27 | 465 | Fora do SLA |
| HFX 1 N 28 | 460 | Fora do SLA |
| FZF 5 P 56 | 334 | Fora do SLA |

## Conclusão

A operação apresenta bom desempenho geral, com **68% dos veículos dentro do prazo**. No entanto, os **32% de gargalos** indicam a necessidade de:
- Investigação dos casos extremos (especialmente os Top 5)
- Revisão do fluxo de descarga nos horários de pico
- Implementação de alertas para permanências prolongadas