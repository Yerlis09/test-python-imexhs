import logging
import pydicom
from oop.study_record import StudyRecord

class DICOMStudyLoader(StudyRecord):
    """
    Clase que carga los detalles de un estudio desde un archivo DICOM.
    """
    def load_from_dicom(self, dicom_file_path: str):
        """
        Carga los detalles del estudio desde un archivo DICOM.
        """
        try:
            dicom_file = pydicom.dcmread(dicom_file_path)
            # Cargar información del paciente
            self.name = dicom_file.get('PatientName', None)
            self.patient_id = dicom_file.get('PatientID', None)
            self.birth_date = dicom_file.get('PatientBirthDate', None)
            self.sex = dicom_file.get('PatientSex', None)
            # Cargar información del estudio
            self.study_date = dicom_file.get('StudyDate', None)
            self.study_time = dicom_file.get('StudyTime', None)
            self.modality = dicom_file.get('Modality', None)
            self.study_instance_uid = dicom_file.get('StudyInstanceUID', None)
            self.series_number = dicom_file.get('SeriesNumber', None)
            self.number_of_frames = dicom_file.get('NumberOfFrames', None)
        except Exception as e:
            logging.error(f"Error loading DICOM file: {e}")

    def __str__(self):
        """
        Retorna una representación en cadena de la información del paciente y del estudio.
        """
        patient_info = self.get_patient_info()
        study_info = self.get_study_info()
        combined_info = {**patient_info, **study_info}
        return "\n".join([f"{key}: {value}" for key, value in combined_info.items()])
