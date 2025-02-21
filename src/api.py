# src/api.py
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carrega os dados do CSV
dados = pd.read_csv("data/pecas.csv")

@app.route('/preco_medio', methods=['POST'])
def preco_medio():
    """
    Endpoint para retornar o preço médio de uma peça, recebendo os dados via JSON no body.
    Exemplo de JSON:
    {
        "peca": "Pastilha de Freio"
    }
    """
    conteudo = request.get_json()
    if not conteudo or 'peca' not in conteudo:
        return jsonify({'erro': 'O parâmetro "peca" é obrigatório no corpo da requisição.'}), 400

    peca_param = conteudo['peca']
    
    # Filtrar os dados ignorando diferenças de maiúsculas/minúsculas
    df_filtrado = dados[dados['peca'].str.lower() == peca_param.lower()]
    if df_filtrado.empty:
        return jsonify({'erro': f'Peça "{peca_param}" não encontrada.'}), 404

    media = df_filtrado['preco'].mean()
    resposta = {
        'peca': peca_param,
        'preco_medio': round(media, 2),
        'total_registros': int(df_filtrado.shape[0])
    }
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
