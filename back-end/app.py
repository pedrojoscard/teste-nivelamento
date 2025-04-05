from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

try:
    df = pd.read_csv('Relatorio_cadop.csv', sep=';', encoding='utf-8')
    print("Arquivo Relatorio_cadop.csv carregado com sucesso!")
except FileNotFoundError:
    print("ERRO: Arquivo Relatorio_cadop.csv não encontrado na pasta backend")
    print("Certifique-se que o arquivo está na mesma pasta que app.py")
    exit(1)
except Exception as e:
    print(f"Erro ao ler o arquivo: {str(e)}")
    print("Tente mudar o encoding para 'latin1' ou 'iso-8859-1' se houver erros de caracteres")
    exit(1)

@app.route('/api/operadoras', methods=['GET']) 
def buscar():
    termo = request.args.get('q', '').lower()
    if not termo:
        return jsonify([])
    
    resultados = df[
        df.apply(lambda row: any(str(cell).lower().find(termo) != -1 for cell in row), axis=1)
    ].head(50).fillna('').to_dict('records')
    
    return jsonify(resultados)
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)