from typing import List, Optional

import sqlmodel

import reflex as rx
from scribe1.database.models1.Patient import Patient

class PatientCurrentMeds(rx.Model, table=True):
    medication1: str
    dosage1: str
    frequency1: str
    medication1: str
    dosage1: str
    frequency2: str
    medication2: str
    dosage2: str
    frequency3: str
    medication3: str
    dosage3: str
    patientID: int = sqlmodel.Field(foreign_key="patient.id")

    patient: Optional[Patient] = sqlmodel.Relationship(
        back_populates="PatientCurrentMeds"
    )
