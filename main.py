import sys
import logging
from file_operations import list_folder_contents, read_csv_file, read_dicom_file
from oop.dicom_study_loader import DICOMStudyLoader

# Configuración del sistema de logging para manejar errores
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Verifica que se hayan pasado al menos 3 argumentos (script, operación, y ruta)
    if len(sys.argv) < 3:
        # Muestra un mensaje de uso si faltan argumentos
        print("Usage: python main.py <operation> <path> [<filename> [<tag> ...]]")
        print("Options:")
        print("  1: List the contents of a directory.")
        print("  2: Read a CSV file and show column details and statistics.")
        print("  3: Read a DICOM file and show metadata. Optionally, specify DICOM tags to display.")
        print("  4: Load and display patient and study information from a DICOM file (Point 2)")
        return

    operation = int(sys.argv[1])
    path = sys.argv[2]

    # Determina la operación a realizar en función del valor de 'operation'
    if operation == 1:
        # Listar el contenido de la carpeta
        list_folder_contents(path)
    elif operation == 2:
        # Leer un archivo CSV
        if len(sys.argv) < 4:
            # Muestra un mensaje de error si no se proporciona un nombre de archivo CSV
            print("Error: Missing filename for CSV operation.")
            return
        filename = sys.argv[3]
        read_csv_file(path, filename)
    elif operation == 3:
        # Leer un archivo DICOM y mostrar metadatos
        if len(sys.argv) < 4:
            # Muestra un mensaje de error si no se proporciona un nombre de archivo DICOM
            print("Error: Missing filename for DICOM operation.")
            return
        filename = sys.argv[3]
        # Pasar los tags como están, sin convertirlos
        # Recoge cualquier tag adicional pasado como argumento y los pasa como lista
        tags = sys.argv[4:]
        read_dicom_file(path, filename, *tags)
    elif operation == 4:
        # Cargar y mostrar información de paciente y estudio desde DICOM (Punto 2)
        dicom_file_path = sys.argv[2]
        dicom_loader = DICOMStudyLoader()  # Crear instancia de DICOMStudyLoader
        dicom_loader.load_from_dicom(dicom_file_path)  # Cargar detalles desde el archivo DICOM
        print(dicom_loader)  # Mostrar la información del paciente y del estudio
    else:
        # Muestra un mensaje de error si se proporciona un número de operación inválido
        logging.error("Invalid operation number. Must be 1, 2, or 3.")

if __name__ == "__main__":
    main()
