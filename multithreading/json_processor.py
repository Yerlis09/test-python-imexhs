import json
import logging
from typing import List, Dict
from pydantic import BaseModel

# Define el modelo de datos con Pydantic
class DataItem(BaseModel):
    id: str
    data: List[str]
    deviceName: str

def read_and_validate_json(json_file_path: str) -> Dict[str, DataItem]:
    """
    Lee y valida un archivo JSON, retornando un diccionario de objetos DataItem.
    """
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    validated_data = {}
    for key, value in data.items():
        validated_data[key] = DataItem(**value)  # Valida usando Pydantic
    return validated_data

def setup_logging(log_file_path: str):
    """
    Configura el logging para incluir más detalles como el nombre del hilo y la marca de tiempo.
    """
    # Remueve los handlers previos si existen
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    # Configura el logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(threadName)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )

def process_data_item(data_item: DataItem):
    """
    Procesa cada DataItem: normaliza los datos, calcula y registra estadísticas.
    """
    logging.info(f"Processing ID: {data_item.id}")

    # Convertir las cadenas de datos en listas de enteros
    data_values = []
    for line in data_item.data:
        data_values.extend(map(int, line.split()))

    # Calcular la media antes de la normalización
    average_before = sum(data_values) / len(data_values)
    logging.info(f"Average before normalization for ID {data_item.id}: {average_before:.2f}")

    # Normalizar los datos
    max_value = max(data_values)
    normalized_data = [x / max_value for x in data_values]

    # Calcular la media después de la normalización
    average_after = sum(normalized_data) / len(normalized_data)
    logging.info(f"Average after normalization for ID {data_item.id}: {average_after:.2f}")

    # Tamaño de los datos
    data_size = len(data_values)
    logging.info(f"Data size for ID {data_item.id}: {data_size}")
