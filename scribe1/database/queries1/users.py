from typing import List, Optional

import sqlmodel

import reflex as rx

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