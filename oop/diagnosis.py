import logging
from typing import Optional
from oop.patient_record import PatientRecord


class Diagnosis(PatientRecord):
    """
    Clase que extiende PatientRecord para incluir diagnóstico.
    """
    diagnosis: Optional[str] = None

    def update_diagnosis(self, new_diagnosis: str):
        """
        Actualiza el diagnóstico y registra el cambio.
        """
        old_diagnosis = self.diagnosis
        self.diagnosis = new_diagnosis
        logging.info(f"Diagnosis updated from '{old_diagnosis}' to '{new_diagnosis}'")
