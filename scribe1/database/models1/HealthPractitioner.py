from typing import List, Optional

import sqlmodel

import reflex as rx

class HealthPractitioner(rx.Model, table=True):
    username: str
    password: str

    patients: List[Patient] = sqlmodel.Relationship(
        back_populates="HealthPractitioner"
    )