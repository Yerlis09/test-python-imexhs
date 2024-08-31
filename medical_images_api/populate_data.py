import requests
import json
import numpy as np

# Cargar el archivo JSON
with open('sample-04-json.json', 'r') as file:
    data = json.load(file)

# Función para calcular la media antes y después de la normalización
def calculate_means(data_list):
    mean_before = np.mean(data_list)
    mean_after = mean_before / 100.0  # Ejemplo de normalización simple
    return mean_before, mean_after

# Iterar sobre cada entrada en el JSON y enviar un POST request para crear el registro
for key, record in data.items():
    # Convertir los datos en una lista de enteros
    data_list = [int(num) for num in ' '.join(record['data']).split()]

    # Calcular valores requeridos
    mean_before, mean_after = calculate_means(data_list)
    data_size = len(data_list)
    
    # Crear el payload para la solicitud
    payload = {
        "id": record["id"],
        "device_name": record["deviceName"],
        "mean_before_normalization": mean_before,
        "mean_after_normalization": mean_after,
        "data_size": data_size,
        "raw_data": data_list
    }

    # Enviar la solicitud POST al servidor
    response = requests.post('http://localhost:8000/api/results/', json=payload)
    if response.status_code == 201:
        print(f"Record {record['id']} created successfully.")
    else:
        print(f"Failed to create record {record['id']}: {response.status_code} - {response.text}")
