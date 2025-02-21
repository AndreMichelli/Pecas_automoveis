import random
import csv
from datetime import datetime, timedelta

# Listas de dados para sorteio
pecas = [
    "Pastilha de Freio", "Filtro de Óleo", "Disco de Freio",
    "Velas de Ignição", "Amortecedor", "Filtro de Ar"
]
modelos = [
    "Fiat Uno", "Volkswagen Gol", "Chevrolet Onix",
    "Hyundai HB20", "Renault Clio", "Volkswagen Golf", "Fiat Palio"
]

# Função para gerar uma data aleatória entre duas datas
def data_aleatoria(inicio, fim):
    delta = fim - inicio
    dias_aleatorios = random.randint(0, delta.days)
    return inicio + timedelta(days=dias_aleatorios)

# Define o intervalo de datas
data_inicio = datetime(2023, 1, 1)
data_fim = datetime(2023, 4, 30)

# Cria e escreve o CSV
with open("data/pecas.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "peca", "modelo_carro", "preco", "data"])
    
    for i in range(1, 401):
        peca = random.choice(pecas)
        modelo = random.choice(modelos)
        # Gera um preço aleatório entre R$ 50,00 e R$ 500,00
        preco = round(random.uniform(50, 500), 2)
        data_registro = data_aleatoria(data_inicio, data_fim).strftime("%Y-%m-%d")
        writer.writerow([i, peca, modelo, preco, data_registro])

print("Arquivo 'pecas.csv' criado com sucesso na pasta 'data/'!")
