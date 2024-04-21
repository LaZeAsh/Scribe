from typing import List, Optional

import sqlmodel

import reflex as rx

class HealthPractitioner(rx.Model, table=True):
    username: str
    password: str

    patients: List[Patient] = sqlmodel.Relationship(
        back_populates="HealthPractitioner"
    )

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
    alerts: [str]
    healthPractitionerID: int = sqlmodel.Field(foreign_key="healthPractitioner.id")
    
    visits: List[Visit] = sqlmodel.Relationship(
        back_populates="Patient"
    )

    healthPractitioner: Optional["HealthPractitioner"] = sqlmodel.Relationship(
        back_populates="patients"
    )


class PatientMedHistory(rx.Model, table=True):
    pastConditions: str
    surgicalProcedures: str
    allergies: str
    antecedents: str
    patientID: int = sqlmodel.Field(foreign_key="patient.id")

    patient: Optional["patient"] = sqlmodel.Relationship(
        back_populates="PatientMedHistory"
    )

class patientCurrentMeds(rx.Model, table=True)
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

    patient: Optional["patient"] = sqlmodel.Relationship(
        back_populates="patientCurrentMeds"
    )

class visit(rx.Model, table=True)
    dayOfVisit: str
    symtoms: str
    geolocation: str
    HPI: str
    ROS: str
    PE: str
    constitutional: str
    HENT: str
    eyes: str
    neck: str
    dosage3: str
    CV: str
    Lungs: str
    GI: str
    MSK: str
    NEURO: str
    hospitalCourse: str
    differentialDiagnosis: str
    additional: str
    patientID: int = sqlmodel.Field(foreign_key="patient.id")

    patient: Optional["patient"] = sqlmodel.Relationship(
        back_populates="visit"
    )




    class QueryUser(rx.State):
        name: str
        users: list[User]

        def get_users(self):
            with rx.session() as session:
                self.users = session.exec(
                    User.select().where(
                        User.username.contains(self.name)
                    )
                ).all()

     class QueryPatients(rx.State):
        healthPractitionerID: str
        patients: list[Patient]

        def get_users(self):
            with rx.session() as session:
                self.patients = session.exec(
                    Patient.select().where(
                        Patient.healthcarePractitionerID.contains(self.healthCarePractitionerID)
                    )
                ).all()
        
        class healthPractitionerQueries(rx.State):
            username: str
            email: str

            def add_healthPractitioner(self):
                with rx.session() as session:
                    session.add(
                        HealthPractitioner(
                            username=self.username, email=self.email
                        )
                    )
                    session.commit()

    
    class QueryVisits(rx.State):
        patientID: str
        visits: list[Visit]

        def get_visits(self):
            with rx.session() as session:
                self.visits = session.exec(
                    Visit.select().where(
                        Visit.patientID.contains(self.patientID)
                    )
                ).all()