# 📰 Clasificador de Noticias por Categoría - Naïve Bayes

Este proyecto consiste en una aplicación de Inteligencia Artificial que clasifica automáticamente noticias en cinco categorías: **Business, Politics, Sport, Entertainment y Tech**. El modelo ha sido implementado desde cero usando el algoritmo **Naïve Bayes**, y cuenta con una interfaz web sencilla desarrollada con **Flask**.

---

## 📁 Estructura del Proyecto

```
ProyectoIA/
│
├── limpiador.py            # Preprocesamiento del dataset
├── modelo_naive.py         # Implementación del algoritmo Naïve Bayes
├── main.py                 # Evaluación del modelo entrenado
├── app.py                  # Aplicación web en Flask
├── noticias_limpias.csv    # Dataset preprocesado
├── modelo_naive.json       # Modelo entrenado guardado
├── historial.json          # Historial de clasificaciones realizadas
├── templates/              # HTML para la interfaz
└── static/                 # CSS, imágenes, etc.
```

---

## 🔧 Requisitos

- Python 3.x
- Flask
- NLTK
- Pandas

---

## 🚀 Instrucciones para la primera ejecución

### 1. Clonar o descargar este repositorio

```bash
git clone https://github.com/usuario/proyectoIA.git
cd ProyectoIA
```

### 2. Instalar dependencias necesarias

```bash
pip install flask nltk pandas
```

### 3. Descargar recursos de NLTK

Abrir terminal y ejecutar Python:

```bash
python
>>> import nltk
>>> nltk.download('stopwords')
>>> nltk.download('wordnet')
>>> nltk.download('punkt')
>>> exit()
```

### 4. Preprocesar los datos

Edita el archivo `limpiador.py` y cambia esta línea por la ruta local a tu dataset:

```python
DATASET_DIR = "C:\Ruta\a\la\carpeta\BBC News Summary\Summaries"
```

Luego ejecuta:

```bash
python limpiador.py
```

Esto generará el archivo `noticias_limpias.csv`.

---

### 5. Entrenar y guardar el modelo

```bash
python modelo_naive.py
```

Esto entrenará el clasificador y guardará el modelo como `modelo_naive.json`.

---

### 6. Ejecutar la aplicación web

```bash
python app.py
```

Abre tu navegador y visita: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 7. Probar con una noticia

Puedes probar con el siguiente texto de ejemplo en la web:

> **Texto:**  
> *The government announced a new economic policy to boost the tech industry.*

> **Categoría esperada:**  
> `Business`

---

## 📊 Funcionalidades adicionales

- **Historial:** registra cada clasificación realizada.
- **Estadísticas:** muestra cuántas clasificaciones se han hecho por categoría.
- **Interfaz interactiva:** resultado codificado por color según categoría.

---

## 📌 Observaciones

- El modelo ha sido implementado **sin librerías externas de machine learning**.
- Todos los diagramas, evidencias y documentación técnica están incluidos en el PDF entregado.
- Este proyecto fue desarrollado como parte del curso de **Inteligencia Artificial - Primer semestre 2025** en la **Universidad Rafael Landívar**.

---

## 🧠 Créditos

Desarrollado por:  
- Diego Azurdia (o el nombre de tu equipo)