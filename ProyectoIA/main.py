from backend.modelo_naive import NaiveBayesClassifier
import pandas as pd
import json
from sklearn.metrics import classification_report
from collections import Counter

# Cargar el modelo guardado (JSON)
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

# Cargar datos de prueba
df = pd.read_csv("noticias_limpias.csv")
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
split_index = int(0.8 * len(df))
test_df = df[split_index:]

modelo = cargar_modelo()

# Evaluar
y_true = []
y_pred = []

for _, fila in test_df.iterrows():
    pred = modelo.predecir(fila["texto_limpio"])
    y_pred.append(pred)
    y_true.append(fila["categoria"])

# Reporte
print("📊 Resultados del modelo:\n")
print(classification_report(y_true, y_pred))
