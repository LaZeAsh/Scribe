from typing import List, Optional

import sqlmodel

import reflex as rx

from scribe1.database.models1.Patient import HealthPractitioner
from scribe1.database.models1.Patient import Patient

class addHealthPractitioner(rx.State):
    username: str = "username1"
    password: str = "password1"

    def add_healthPractitioner(self):
        with rx.session() as session:
            hp = HealthPractitioner(username=self.username, password=self.password)
            print(hp)
            session.add(hp)
            session.commit()

class getPatients(rx.State):
    username: str
    healthPractitoners: list[HealthPractitioner]
    patients: list[Patient]

    def get_Patients(self):
        with rx.session() as session:
            self.healthPractitioner = session.exec(HealthPractitioner.select().where(HealthPractitioner.username.contains(self.username)),
                                                   patients=self.healthPractitioner[0].patients
            ).all()
        print("getPatients ", self.patients)
        return self.patients
