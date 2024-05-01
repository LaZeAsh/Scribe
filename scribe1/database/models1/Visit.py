from typing import List, Optional

import sqlmodel

import reflex as rx

from scribe1.database.models1.Patient import Patient

class Visit(rx.Model, table=True):
    dayOfVisit: str
    symtoms: str
    HPI: str
    PE: str
    constitutional: str
    differentialDiagnosis: str
    additional: str
    patientID: int = sqlmodel.Field(foreign_key="patient.id")

    patient: Optional[Patient] = sqlmodel.Relationship(
        back_populates="visits"
    )