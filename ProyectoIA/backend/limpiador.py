import os
import re

import nltk as nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from nltk.tokenize import word_tokenize

# Cambia esto por la ruta local a la carpeta "bbc"
# DATASET_DIR = "C:\\Users\\javie\\Downloads\\archive\\BBC News Summary\\Summaries"
DATASET_DIR = "C:/Users/Diego/OneDrive/Desktop/ProyectoIA/proyectoIA/archive/BBC News Summary/BBC News Summary/Summaries"

# Cargar datos
def cargar_datos(dataset_dir):
    data = []
    for categoria in os.listdir(dataset_dir):
        categoria_dir = os.path.join(dataset_dir, categoria)
        if os.path.isdir(categoria_dir):
            for archivo in os.listdir(categoria_dir):
                ruta = os.path.join(categoria_dir, archivo)
                with open(ruta, 'r', encoding='latin-1') as f:
                    texto = f.read()
                    data.append((categoria, texto))
    return pd.DataFrame(data, columns=["categoria", "texto"])

# Limpieza de texto
def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z\s]', '', texto)
    tokens = texto.split()
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
    return ' '.join(tokens)


if __name__ == "__main__":
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

    df = cargar_datos(DATASET_DIR)
    print("Ejemplo antes de limpiar:")
    print(df.iloc[0])

    df["texto_limpio"] = df["texto"].apply(limpiar_texto)

    print("\nEjemplo después de limpiar:")
    print(df[["categoria", "texto_limpio"]].iloc[0])

    # Guardar CSV para entrenamiento posterior
    df.to_csv("noticias_limpias.csv", index=False)
