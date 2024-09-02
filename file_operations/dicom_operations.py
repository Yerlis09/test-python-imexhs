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
            dicom_file = pydicom.dcmread(file_path) #retorna un dataset

            # Muestra información básica del archivo DICOM
            print(f"Patient's Name: {dicom_file.PatientName}")
            print(f"Study Date: {dicom_file.StudyDate}")
            print(f"Modality: {dicom_file.Modality}")

            # Si se ingresan etiquetas específicas, muestra sus valores
            if tags:
                for tag in tags:
                    try:
                        tag_hex = int(tag, 16)
                        print(tag_hex)
                        tag_value = dicom_file[tag_hex].value
                        print(f"Tag {tag_hex}: {tag_value}")
                    except KeyError:
                        logging.error(f"Tag {tag_hex} not found in the DICOM file.")
            else:
                logging.error("No tags provided.")
        else:
            logging.error("File does not exist or is not a DICOM file.")
    except Exception as e:
        logging.error(f"Error reading DICOM file: {e}")
