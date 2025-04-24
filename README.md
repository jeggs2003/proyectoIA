# Clasificador de Noticias por Categoría - Naïve Bayes

Este proyecto consiste en una aplicación de Inteligencia Artificial que clasifica automáticamente noticias en cinco categorías: **Business, Politics, Sport, Entertainment y Tech**. El modelo ha sido implementado desde cero usando el algoritmo **Naïve Bayes**, y cuenta con una interfaz web sencilla desarrollada con **Flask**.

---

##  Instrucciones para la primera ejecución

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

El archivo `limpiador.py` ahora detecta automáticamente la ruta al dataset usando `pathlib`, por lo que no es necesario cambiar rutas manualmente.

Asegúrate de que la carpeta `archive/BBC News Summary/Summaries` esté al mismo nivel que la raíz del proyecto (donde está el `README.md`).

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

Abre tu navegador y visita: [http://127.0.0.1:5000]

---

### 7. Probar con una noticia

Puedes probar con el siguiente texto de ejemplo en la web:

> **Texto:**  
> *The government announced a new economic policy to boost the tech industry.*

> **Categoría esperada:**  
> `Business`

---

##  Funcionalidades adicionales

- **Historial:** registra cada clasificación realizada.
- **Estadísticas:** muestra cuántas clasificaciones se han hecho por categoría.

---

## Desarrollado por:  

- Javier Estuardo Godínez Gudiel –  1179222
- Katherine Andrea Mayen Rivera –  1129222
- Diego Estuardo Azurdia Marín –  1010821
