class addHealthPractitioner(rx.State):
    username: str
    email: str

    def add_healthPractitioner(self):
        with rx.session() as session:
            hp = HealthPractitioner(username=self.username, email=self.email)
                print(hp)
            session.add(hp)
            session.commit()

class getPatients(rx.State):
    username: str
    healthPractitoners: list[HealthPractitioner]
    patients: list[Patient]

    def get_Patients(self):
        with rx.session() as session:
            self.healthPractitioner = session.exec(
                HealthPractitioner.select().where(
                    HealthPractitioner.username.contains(self.username)
                )
                patients = healthPractitioner[0].patients
            ).all()
        print("getPatients ", patients)
        return patients
