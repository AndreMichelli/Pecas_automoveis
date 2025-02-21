from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Configurar Chrome para rodar em segundo plano
chrome_options = Options()
chrome_options.add_argument("--headless")  # Roda sem interface gráfica
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 🚀 Baixa e instala automaticamente o ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Lista de peças para buscar
pecas = [
    "Pastilha de Freio", "Filtro de Óleo", "Bateria 60Ah", "Amortecedor Dianteiro",
    "Correia Dentada", "Vela de Ignição", "Bomba de Combustível", "Radiador de Água",
    "Disco de Freio", "Sensor de Oxigênio"
]

# Lista para armazenar os dados
dados_pecas = []

# Percorrer todas as peças no Mercado Livre
for peca in pecas:
    print(f"Buscando preços para: {peca}")

    # Formatar a URL de busca
    url = f"https://lista.mercadolivre.com.br/{peca.replace(' ', '-')}"
    driver.get(url)

    # Esperar carregar os produtos
    time.sleep(3)

    # Coletar os elementos dos produtos
    produtos = driver.find_elements(By.CLASS_NAME, "ui-search-result__content-wrapper")

    for produto in produtos[:5]:  # Capturar os 5 primeiros produtos
        try:
            titulo = produto.find_element(By.TAG_NAME, "h2").text
            preco = produto.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
            preco = float(preco.replace(".", "").replace(",", "."))  # Converter para float
            
            dados_pecas.append({"peca": peca, "titulo": titulo, "preco": preco})
        except:
            continue  # Se der erro, pula para o próximo

# Fechar o navegador
driver.quit()

# Criar DataFrame e salvar como CSV
df = pd.DataFrame(dados_pecas)
df.to_csv("precos_pecas.csv", index=False, encoding="utf-8")
print("✅ Dados salvos em 'precos_pecas.csv'")
