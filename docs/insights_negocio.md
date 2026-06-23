
---

### 📄 `docs/insights_negocio.md`

```markdown
# Insights para Gestores — Pátio Logístico

## O que os dados mostram

A simulação de 50 caminhões revelou:

- **32% dos caminhões extrapolaram o SLA** — risco de multas e custos operacionais elevados
- **Média de permanência: 168 min** — abaixo do SLA de 180 min, indicando operação eficiente
- **Top 5 gargalos** concentram os maiores desvios

## Recomendações

1. **Auditar os 5 casos críticos** (especialmente a placa `KZD 7 B 18` com 536 min)
2. **Revisar o fluxo de descarga nos horários de pico**
3. **Implementar alertas automáticos** para permanências > 2h30
4. **Monitorar o percentual de gargalos** mensalmente

## Perguntas para o time

- Por que alguns caminhões ficam quase 9 horas no pátio?
- Existe padrão por transportadora ou horário?
- Quais gargalos físicos contribuem para esses números?

## Conclusão

A operação está no caminho certo, mas os 32% de gargalos mostram oportunidade clara de melhoria.