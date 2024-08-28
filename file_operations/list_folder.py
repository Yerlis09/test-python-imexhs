import os
import logging

# Función para listar el contenido de una carpeta
def list_folder_contents(path):
    # Verifica si la ruta es un directorio
    try:
        if os.path.isdir(path):
            # Obtiene la lista de todos los elementos en el directorio
            contents = os.listdir(path)
            # Imprime el número total de elementos encontrados
            print(f"Number of elements in '{path}': {len(contents)}")
             # Imprime los nombres de todos los elementos en el directorio
            print("Contents:")
            for item in contents:
                print(f"- {item}")
        else:
            # Lanza un error si la ruta no es un directorio
            raise NotADirectoryError(f"The path '{path}' is not a directory.")
    except Exception as e:
        # Registra cualquier error encontrado durante el proceso
        logging.error(f"Error listing folder contents: {e}")
