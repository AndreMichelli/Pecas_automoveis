# src/main.py
import pandas as pd

def carregar_dados(caminho):
    """Carrega os dados do arquivo CSV."""
    try:
        df = pd.read_csv(caminho)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def calcular_preco_medio(df, nome_peca):
    """Calcula a média de preço para a peça especificada."""
    df_filtrado = df[df['peca'].str.lower() == nome_peca.lower()]
    if df_filtrado.empty:
        print(f"Nenhum dado encontrado para a peça: {nome_peca}")
        return None
    media = df_filtrado['preco'].mean()
    return media

if __name__ == "__main__":
    caminho_dados = "../data/pecas.csv"
    dados = carregar_dados(caminho_dados)
    
    if dados is not None:
        nome_peca = input("Digite o nome da peça que deseja consultar: ")
        media_preco = calcular_preco_medio(dados, nome_peca)
        if media_preco is not None:
            print(f"O preço médio da peça '{nome_peca}' é: R$ {media_preco:.2f}")
