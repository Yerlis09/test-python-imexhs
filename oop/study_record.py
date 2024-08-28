from typing import Optional
from oop.patient_record import PatientRecord

class StudyRecord(PatientRecord):
    """
    Clase que representa un estudio médico, extendiendo la información del paciente.
    """
    modality: Optional[str] = None
    study_date: Optional[str] = None
    study_time: Optional[str] = None
    study_instance_uid: Optional[str] = None
    series_number: Optional[int] = None
    number_of_frames: Optional[int] = None

    def get_study_info(self):
        """
        Retorna la información del estudio en forma de diccionario.
        """
        return {
            "Modality": self.modality,
            "Study Date": self.study_date,
            "Study Time": self.study_time,
            "Study Instance UID": self.study_instance_uid,
            "Series Number": self.series_number,
            "Number of Frames": self.number_of_frames
        }

    def set_study_info(self, modality=None, study_date=None, study_time=None, study_instance_uid=None, series_number=None, number_of_frames=None):
        """
        Establece la información del estudio.
        """
        if modality is not None:
            self.modality = modality
        if study_date is not None:
            self.study_date = study_date
        if study_time is not None:
            self.study_time = study_time
        if study_instance_uid is not None:
            self.study_instance_uid = study_instance_uid
        if series_number is not None:
            self.series_number = series_number
        if number_of_frames is not None:
            self.number_of_frames = number_of_frames
