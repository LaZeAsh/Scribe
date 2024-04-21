from typing import List, Optional

import sqlmodel

import reflex as rx

class Visit(rx.Model, table=True)
    dayOfVisit: str
    symtoms: str
    HPI: str
    PE: str
    constitutional: str
    differentialDiagnosis: str
    additional: str
    patientID: int = sqlmodel.Field(foreign_key="patient.id")

    patient: Optional["patient"] = sqlmodel.Relationship(
        back_populates="visits"
    )