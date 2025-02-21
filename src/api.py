# src/api.py
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carregar os dados ao iniciar a API
dados = pd.read_csv("../data/pecas.csv")

def calcular_preco_medio(peca):
    df_filtrado = dados[dados['peca'].str.lower() == peca.lower()]
    if df_filtrado.empty:
        return None
    return df_filtrado['preco'].mean()

@app.route('/preco_medio', methods=['GET'])
def preco_medio():
    peca = request.args.get('peca')
    if not peca:
        return jsonify({'erro': 'Parâmetro "peca" é obrigatório.'}), 400
    media = calcular_preco_medio(peca)
    if media is None:
        return jsonify({'erro': f'Peça "{peca}" não encontrada.'}), 404
    return jsonify({'peca': peca, 'preco_medio': round(media, 2)})

if __name__ == '__main__':
    app.run(debug=True)
