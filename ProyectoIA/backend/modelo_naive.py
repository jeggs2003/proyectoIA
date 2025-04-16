import pandas as pd
import random
from collections import defaultdict, Counter
import math
import json

# Cargar datos limpios
df = pd.read_csv("noticias_limpias.csv")

# Mezclar datos (importante para evitar sesgo si están ordenados)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Separar 80% para entrenamiento, 20% para prueba
split_index = int(0.8 * len(df))
train_df = df[:split_index]
test_df = df[split_index:]

print(f"Entrenamiento: {len(train_df)} noticias")
print(f"Prueba: {len(test_df)} noticias")


class NaiveBayesClassifier:
    def __init__(self):
        self.clases = set()
        self.prior = {}
        self.palabras_por_clase = defaultdict(Counter)
        self.total_palabras_por_clase = defaultdict(int)
        self.vocabulario = set()

    def entrenar(self, datos):
        total_docs = len(datos)

        # Contar documentos por clase
        docs_por_clase = datos['categoria'].value_counts().to_dict()

        # Calcular probabilidad a priori
        for clase, count in docs_por_clase.items():
            self.clases.add(clase)
            self.prior[clase] = count / total_docs

        # Contar palabras por clase
        for _, fila in datos.iterrows():
            clase = fila['categoria']
            palabras = fila['texto_limpio'].split()
            self.palabras_por_clase[clase].update(palabras)
            self.total_palabras_por_clase[clase] += len(palabras)
            self.vocabulario.update(palabras)

    def guardar_modelo(self, ruta='modelo_naive.json'):
        modelo = {
            "prior": self.prior,
            "palabras_por_clase": {k: dict(v) for k, v in self.palabras_por_clase.items()},
            "total_palabras_por_clase": dict(self.total_palabras_por_clase),
            "vocabulario": list(self.vocabulario)
        }
        with open(ruta, 'w') as f:
            json.dump(modelo, f, indent=4)

    def predecir(self, texto):
        palabras = texto.split()
        scores = {}

        V = len(self.vocabulario)

        for clase in self.clases:
            log_prob = math.log(self.prior[clase])
            total_palabras = self.total_palabras_por_clase[clase]

            for palabra in palabras:
                # Suavizado de Laplace
                frecuencia = self.palabras_por_clase[clase][palabra] if palabra in self.palabras_por_clase[clase] else 0
                prob = (frecuencia + 1) / (total_palabras + V)
                log_prob += math.log(prob)

            scores[clase] = log_prob

        # Devolver la clase con mayor probabilidad
        return max(scores, key=scores.get)

# Entrenar el modelo
modelo = NaiveBayesClassifier()
modelo.entrenar(train_df)
modelo.guardar_modelo()