import logging
from pydantic import BaseModel, condecimal, conint, field_validator
from typing import Optional
import re

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PatientRecord(BaseModel):
    """
    Clase que representa la información básica de un paciente.
    """
    name: Optional[str] = None
    age: Optional[conint(ge=0, le=120)] = None  # type: ignore
    birth_date: Optional[str] = None
    sex: Optional[str] = None
    weight: Optional[condecimal(gt=0, decimal_places=2)] = None  # type: ignore
    patient_id: Optional[str] = None
    patient_id_type: Optional[str] = None
    diagnosis: Optional[str] = None

    @field_validator('birth_date')
    def validate_birth_date(cls, v):
        """
        Valida el formato de la fecha de nacimiento si se proporciona.
        """
        if v is not None:
            # Validación simple para asegurarse de que la fecha esté en formato AAAA-MM-DD
            assert re.match(r'\d{4}-\d{2}-\d{2}', v), 'Invalid birth date'
        return v

    def get_patient_info(self):
        """
        Retorna la información del paciente en forma de diccionario.
        """
        return {
            "Name": self.name,
            "Age": self.age,
            "Birth Date": self.birth_date,
            "Sex": self.sex,
            "Weight": self.weight,
            "Patient Id": self.patient_id,
            "Patient Id Type": self.patient_id_type,
            "Diagnosis": self.diagnosis
        }

    def set_patient_info(self, name=None, age=None, birth_date=None, sex=None, weight=None, patient_id=None, patient_id_type=None, diagnosis=None):
        """
        Establece la información del paciente.
        """
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if birth_date is not None:
            self.birth_date = birth_date
        if sex is not None:
            self.sex = sex
        if weight is not None:
            self.weight = weight
        if patient_id is not None:
            self.patient_id = patient_id
        if patient_id_type is not None:
            self.patient_id_type = patient_id_type
        if diagnosis is not None:
            self.diagnosis = diagnosis

    def update_diagnosis(self, new_diagnosis: str):
            """
            Actualiza el diagnóstico y registra el cambio.
            """
            old_diagnosis = self.diagnosis
            self.diagnosis = new_diagnosis
            logging.info(f"Diagnosis updated from '{old_diagnosis}' to '{new_diagnosis}'")

    def __str__(self):
        return str(self.get_patient_info())