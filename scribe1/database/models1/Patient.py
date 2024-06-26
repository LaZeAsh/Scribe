from typing import List, Optional

import sqlmodel

import reflex as rx

from scribe1.database.models1.Visit import Visit

class Patient(rx.Model, table=True):
    firstName: str
    middleName: str
    lastName: str
    address: str
    city: str
    state: str
    zipCode: str
    socialSecurity: str
    age: str
    sex: str
    alerts: List[str]
    healthPractitionerID: int = sqlmodel.Field(foreign_key="healthPractitioner.id")

    visits: List[Visit] = sqlmodel.Relationship(
        back_populates="Patient"
    )

    healthPractitioner: Optional["HealthPractitioner"] = sqlmodel.Relationship(
        back_populates="patients"
    )

class HealthPractitioner(rx.Model, table=True):
    username: str
    password: str

    patients: List[Patient] = sqlmodel.Relationship(
        back_populates="HealthPractitioner"
    )