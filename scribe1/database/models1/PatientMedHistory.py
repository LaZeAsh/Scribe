from typing import List, Optional

import sqlmodel

import reflex as rx
class PatientMedHistory(rx.Model, table=True):
    pastConditions: str
    surgicalProcedures: str
    allergies: str
    antecedents: str
    patientID: int = sqlmodel.Field(foreign_key="patient.id")

    patient: Optional["patient"] = sqlmodel.Relationship(
        back_populates="PatientMedHistory"
    )