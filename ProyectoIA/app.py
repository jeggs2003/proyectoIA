from flask import Flask, render_template, request
from backend.modelo_naive import NaiveBayesClassifier
from collections import Counter
import json
import os

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

#--------------------------------------------------------------------------------------
# Historial file path
HISTORIAL_PATH = 'historial.json'

def cargar_historial():
    if os.path.exists(HISTORIAL_PATH):
        with open(HISTORIAL_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_en_historial(texto, categoria):
    historial = cargar_historial()
    historial.append({'texto': texto, 'categoria': categoria})
    with open(HISTORIAL_PATH, 'w', encoding='utf-8') as f:
        json.dump(historial, f, ensure_ascii=False, indent=4)
#-----------------------------------------------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    clase_categoria = 'default-box'
    texto_original = ''

    if request.method == 'POST':
        texto = request.form['texto']
        texto_original = texto
        texto_limpio = limpiar_texto(texto)
        prediccion = modelo.predecir(texto_limpio)

        # Mapeo de colores para cada categoría
        color_por_categoria = {
            'business': 'business',
            'entertainment': 'entertainment',
            'politics': 'politics',
            'sport': 'sport',
            'tech': 'tech'
        }

        clase_categoria = color_por_categoria.get(prediccion.lower(), 'default-box')
        resultado = prediccion.capitalize()

        guardar_en_historial(texto, resultado)
    return render_template('index.html', resultado=resultado, clase_categoria=clase_categoria, texto_original=texto_original)
    
        #clase_categoria = color_por_categoria.get(prediccion.lower(), 'bg-secondary')
        #resultado = f"Categoría predicha: {prediccion.capitalize()}"
    #return render_template('index.html', resultado=resultado, clase_categoria=clase_categoria)


@app.route('/historial')
def historial():
    datos = cargar_historial()
    return render_template('historial.html', historial=datos)

@app.route('/estadisticas')
def estadisticas():
    datos = cargar_historial()
    conteo = Counter(item['categoria'] for item in datos)
    return render_template('estadisticas.html', conteo=conteo)



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
