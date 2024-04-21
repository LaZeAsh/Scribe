from typing import List, Optional

import sqlmodel

import reflex as rx
class GetVisit(rx.State):
    visitID: int = 1  # Example visitID, replace with the actual ID you're querying for

    def get_visit(self):
        with rx.session() as session:
            visit = session.exec(
                Visit.select().where(Visit.id == self.visitID)
            ).first()
            return visit

class AddVisit(rx.State):
    # Example attributes for a Visit, add or modify as needed
    dayOfVisit: str = "2023-09-30"
    symptoms: str = "Cough, fever"
    HPI: str = "History of present illness details"
    PE: str = "Physical examination details"
    constitutional: str = "Constitutional symptoms details"
    differentialDiagnosis: str = "Differential diagnosis details"
    additional: str = "Additional notes"
    patientID: int = 1  # Assuming a valid patientID

    def add_visit(self):
        with rx.session() as session:
            new_visit = Visit(
                dayOfVisit=self.dayOfVisit,
                symptoms=self.symptoms,
                HPI=self.HPI,
                PE=self.PE,
                constitutional=self.constitutional,
                differentialDiagnosis=self.differentialDiagnosis,
                additional=self.additional,
                patientID=self.patientID
            )
            
            session.add(new_visit)
            session.commit()