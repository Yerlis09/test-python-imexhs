import os
import pandas as pd
import logging

# Función leer archivo CSV
def read_csv_file(path, filename):
    """
    Lee un archivo CSV y muestra estadísticas descriptivas de las columnas numéricas.
    
    Parámetros:
    path (str): Ruta del directorio donde se encuentra el archivo.
    filename (str): Nombre del archivo CSV.
    
    Retorna:
    None
    """
      
    try:
        # Construye la ruta completa del archivo CSV
        file_path = os.path.join(path, filename)

        # Verifica si el archivo existe y si es un archivo CSV
        if os.path.exists(file_path) and filename.endswith('.csv'):
            # Lee el archivo CSV en un DataFrame de pandas
            df = pd.read_csv(file_path)

            # Imprime el número de columnas y sus nombres
            print(f"Number of columns: {len(df.columns)}")
            print(f"Column names: {df.columns.tolist()}")
            
            # Obtiene y muestra el número de filas en el DataFrame
            num_rows = df.shape[0]
            print(f"Number of rows: {num_rows}")
            
            # Selecciona solo las columnas numéricas para el análisis
            numeric_columns = df.select_dtypes(include='number')
            if not numeric_columns.empty:
                # Si hay columnas numéricas, muestra estadísticas descriptivas
                print("Numeric columns statistics:")
                print(numeric_columns.describe())
            else:
                # Registra un error si no se encuentran columnas numéricas
                logging.error("No numeric data found in the CSV file.")
        else:
            # Registra un error si el archivo no existe o no es un CSV
            logging.error(f"File {file_path} does not exist or is not a CSV file.")
    except Exception as e:
        # Registra cualquier error encontrado durante la lectura del archivo
        logging.error(f"Error reading CSV file: {e}")
