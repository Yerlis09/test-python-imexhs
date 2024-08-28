import os
import pydicom
import logging

# Función leer DICOM
def read_dicom_file(path, filename, *tags):
    try:
        # Construye la ruta completa del archivo DICOM
        file_path = os.path.join(path, filename)

        # Verifica si el archivo existe y si es un archivo DICOM
        if os.path.exists(file_path) and filename.endswith('.dcm'):
            # Lee el archivo DICOM usando pydicom
            dicom_file = pydicom.dcmread(file_path)

            # Muestra información básica del archivo DICOM
            print(f"Patient's Name: {dicom_file.PatientName}")
            print(f"Study Date: {dicom_file.StudyDate}")
            print(f"Modality: {dicom_file.Modality}")

            # Si se proporcionan etiquetas específicas, muestra sus valores
            if tags:
                # Convertir los tags a una lista de cadenas
                tags = [str(tag) for tag in tags]
                try:
                    # Usar un solo print para mostrar todos los tags juntos
                    print(f"Tag {tags}: {dicom_file[tags].value}")
                except KeyError:
                    logging.error(f"Tag {tags} not found in the DICOM file.")
            else:
                logging.error("No tags provided.")
        else:
            logging.error("File does not exist or is not a DICOM file.")
    except Exception as e:
        logging.error(f"Error reading DICOM file: {e}")
