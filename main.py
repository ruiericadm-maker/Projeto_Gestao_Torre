import pandas as pd
import random
import string
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# --- 1. CONFIGURAÇÕES ---
num_caminhoes = 50
data_base = datetime(2023, 10, 26, 6, 0, 0)

# --- 2. FUNÇÕES ---

def gerar_placa():
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numero1 = random.randint(0, 9)
    letra_inter = random.choices(string.ascii_uppercase, k=1)[0]
    numero2 = random.randint(10, 99)
    return f"{letras} {numero1} {letra_inter} {numero2}"

def gerar_tempos_permanencia():
    probabilidade = random.random()
    if probabilidade < 0.60:
        return random.randint(45, 150)
    elif probabilidade < 0.90:
        return random.randint(150, 240)
    else:
        return random.randint(240, 600)

def gerar_grafico_sla(df, caminho_saida):
    status_counts = df['Status'].value_counts()
    cores = ['#2ecc71' if 'Dentro' in status else '#e74c3c' for status in status_counts.index]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(status_counts.index, status_counts.values, color=cores, edgecolor='black')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                 f'{int(height)}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.title('Distribuição de Caminhões por Status de SLA', fontsize=16, fontweight='bold')
    plt.xlabel('Status', fontsize=12)
    plt.ylabel('Quantidade de Caminhões', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"📊 Gráfico salvo em: {caminho_saida}")

# --- 3. LOOP DE CRIAÇÃO DOS DADOS (APENAS A LISTA) ---
lista_torre = []

for _ in range(num_caminhoes):
    placa = gerar_placa()
    minutos_entrada = random.randint(0, 720)
    hora_entrada = data_base + timedelta(minutes=minutos_entrada)
    minutos_permanencia = gerar_tempos_permanencia()
    hora_saida = hora_entrada + timedelta(minutes=minutos_permanencia)
    status_sla = 'Gargalo (Fora SLA)' if minutos_permanencia > 180 else "Concluído (Dentro SLA)"

    lista_torre.append({
        'Placa_Caminhao': placa,
        'Hora_entrada': hora_entrada.strftime('%Y-%m-%d %H:%M:%S'),
        'Hora_Saida': hora_saida.strftime('%Y-%m-%d %H:%M:%S'),
        'Permanencia_Minutos': minutos_permanencia,
        'Status': status_sla
    })

# --- 4. CRIAÇÃO DO DATAFRAME (FORA DO LOOP) ---
df_torres = pd.DataFrame(lista_torre)

# --- 5. EXIBIR AMOSTRA ---
print("\n--- Primeiras 10 linhas do Dataset de Gestão de Torre ---")
print(df_torres.head(10))

# --- 6. SALVAR EXCEL (FORA DO LOOP) ---
df_torres.to_excel('dados_ficticios_gestao_torre.xlsx', index=False)
print("\n✅ Arquivo 'dados_ficticios_gestao_torre.xlsx' gerado com sucesso!")

# --- 7. GERAR GRÁFICO (FORA DO LOOP) ---
gerar_grafico_sla(df_torres, 'distribuicao_sla.png')

print("\n✅ SIMULAÇÃO CONCLUÍDA COM SUCESSO!")


