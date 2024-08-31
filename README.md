# Test Python imeXHS

Este repositorio contiene el código desarrollado como parte de la prueba técnica para imeXHS. El objetivo principal es demostrar habilidades en Python a través de varios ejercicios que abarcan desde el manejo de archivos hasta la creación de una API RESTful para la gestión de resultados de procesamiento de imágenes médicas.

## Sugerencias

Suguiero que para este proyecto se cree un entorno virtual para mantener las dependencias aisladas y facilitar la ejecución del proyecto. Para ello, puedes utilizar venv, el entorno virtual integrado de Python

## Creación y Activación del Entorno Virtual

   ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/MacOS
    venv\Scripts\activate  # Para Windows

   ```

## Instalación de Dependencias

Con el entorno virtual activado, instala las dependencias necesarias ejecutando:

   ```bash
    pip install -r requirements.txt

   ```
ya que esto garantizará que todos los paquetes requeridos estén instalados correctamente.

# Punto 1 - Manejo de Archivos y Operaciones con Arreglos

En esta sección, se desarrollan funciones para trabajar con archivos y directorios. Estas funciones permiten listar el contenido de carpetas, leer archivos CSV y DICOM, y calcular estadísticas básicas.

## Scripts Incluidos

- list_folder.py: Función para listar el contenido de una carpeta y contar el número de elementos.
- csv_operations.py: Función para leer archivos CSV, contar columnas y filas, y calcular estadísticas como la media y la desviación estándar para columnas numéricas.
- dicom_operations.py: Función para leer archivos DICOM e imprimir detalles específicos como el nombre del paciente, la fecha del estudio y la modalidad.

## Ejemplo de Uso

   ```bash
    python main.py 1 file_operations 
    python main.py 2 file_operations sample-01-csv.csv  
    python main.py 3 file_operations sample-01-dicom.dcm 0x0008 0x0016 

   ```
 
# Punto 2 - Programación Orientada a Objetos (OOP)

Aquí se implementan clases para modelar registros de pacientes y estudios médicos, utilizando conceptos de programación orientada a objetos.

## Clases Desarrolladas

- PatientRecord: Clase que almacena la información básica del paciente.
- StudyRecord: Clase que hereda de PatientRecord y añade detalles específicos del estudio.
- Diagnosis: Clase que extiende PatientRecord para incluir la funcionalidad de actualizar diagnósticos.

## Ejemplo de Uso

   ```bash
    python main.py 4 .\oop\sample-02-dicom.dcm

   ```

# Punto 3 - Multithreading y Concurrencia

En este punto, se desarrollan scripts que utilizan hilos para realizar tareas concurrentes, como imprimir números pares e impares, y procesar datos en paralelo a partir de un archivo JSON.

## Scripts Incluidos
- even_odd_threads.py: Script que utiliza hilos para imprimir números pares e impares entre 1 y 200.
- json_processor.py: Script que lee un archivo JSON, normaliza los datos y procesa cada entrada en hilos separados, con un límite de 4 hilos activos al mismo tiempo.

## Ejemplo de Uso

   ```bash
    python main.py 5 .\multithreading\sample-03-00-json.json   
    python main.py 6 .\multithreading\sample-03-00-json.json

   ```

# Punto 4 - API RESTful para Procesamiento de Imágenes Médicas

Este módulo implementa una API RESTful utilizando Django y Django REST Framework para gestionar los resultados del procesamiento de imágenes médicas. La API soporta operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los resultados, que se almacenan en una base de datos PostgreSQL.

## Configuración Inicial

Para iniciar la API, asegúrate de haber configurado correctamente la base de datos en settings.py. Si PostgreSQL no está disponible, la API utilizará SQLite como base de datos.

## Migraciones de Base de Datos

Antes de iniciar el servidor, aplica las migraciones para crear las tablas necesarias en la base de datos:

   ```bash
    python manage.py migrate
   ```

## Población de Datos

Puedes poblar la base de datos con registros de ejemplo utilizando el script populate_data.py:

   ```bash
    python medical_images_api/populate_data.py
   ```

## Ejecución del Servidor

Inicia el servidor de desarrollo de Django:

   ```bash
    python manage.py runserver
   ```

   La API estará disponible en http://localhost:8000/api/
