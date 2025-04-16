from flask import Flask, render_template, request
from backend.modelo_naive import NaiveBayesClassifier
from collections import Counter
import json

app = Flask(__name__)

# Cargar modelo entrenado
def cargar_modelo(ruta='modelo_naive.json'):
    with open(ruta, 'r') as f:
        data = json.load(f)

    modelo = NaiveBayesClassifier()
    modelo.clases = set(data['prior'].keys())
    modelo.prior = data['prior']
    modelo.palabras_por_clase = {k: Counter(v) for k, v in data['palabras_por_clase'].items()}
    modelo.total_palabras_por_clase = data['total_palabras_por_clase']
    modelo.vocabulario = set(data['vocabulario'])
    return modelo

modelo = cargar_modelo()

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ""
    if request.method == 'POST':
        texto = request.form['texto']
        texto_limpio = limpiar_texto(texto)
        prediccion = modelo.predecir(texto_limpio)
        resultado = f"Categoría predicha: {prediccion.capitalize()}"
    return render_template('index.html', resultado=resultado)

def limpiar_texto(texto):
    import re
    from nltk.corpus import stopwords
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z\s]', '', texto)
    tokens = texto.split()
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]
    return ' '.join(tokens)

if __name__ == '__main__':
    import nltk
    nltk.download('stopwords')
    app.run(debug=True)
