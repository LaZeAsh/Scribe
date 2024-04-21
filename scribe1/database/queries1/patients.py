from typing import List, Optional

import sqlmodel

import reflex as rx
class AddPatient(rx.State):
    # Example attributes, add more as needed
    firstName: str = "John"
    middleName: str = "A."
    lastName: str = "Doe"
    address: str = "123 Main Street"
    city: str = "Anytown"
    state: str = "Anystate"
    zipCode: str = "12345"
    socialSecurity: str = "123-45-6789"
    age: str = "30"
    sex: str = "Male"
    alerts: list = ["Allergy: Penicillin"]
    healthPractitionerID: int = 1  # Assuming a valid ID for a HealthPractitioner

    def add_patient(self):
        with rx.session() as session:
            new_patient = Patient(
                firstName=self.firstName,
                middleName=self.middleName,
                lastName=self.lastName,
                address=self.address,
                city=self.city,
                state=self.state,
                zipCode=self.zipCode,
                socialSecurity=self.socialSecurity,
                age=self.age,
                sex=self.sex,
                alerts=self.alerts,
                healthPractitionerID=self.healthPractitionerID
            )
            session.add(new_patient)
            session.commit()
    
class GetPatient(rx.State):
    patientID: int = 1  # Example patientID, replace with the actual ID you're querying for

    def get_patient(self):
        with rx.session() as session:
            patient = session.exec(
                Patient.select.where(Patient.id == self.patientID)
            ).first()
            return patient

class GetPatientCurrentMeds(rx.State):
    patientID: int

    def get_patient_meds(self):
        with rx.session() as session:
            patient_meds = session.exec(
                PatientCurrentMeds.select().where(PatientCurrentMeds.patientID == self.patientID)
            ).first()
            return patient_meds

import reflex as rx

class UpdatePatientCurrentMeds(rx.State):
    patientID: int = 1  # Example patientID, replace with the target patient's ID
    # New medication details to be updated
    new_medication1: str = "UpdatedMedication1"
    new_dosage1: str = "UpdatedDosage1"
    new_frequency1: str = "UpdatedFrequency1"
    new_medication2: str = "UpdatedMedication2"
    new_dosage2: str = "UpdatedDosage2"
    new_frequency2: str = "UpdatedFrequency2"
    new_medication3: str = "UpdatedMedication3"
    new_dosage3: str = "UpdatedDosage3"
    new_frequency3: str = "UpdatedFrequency3"

    def update_patient_current_meds(self):
        with rx.session() as session:
            # Fetch the PatientCurrentMeds entry for the given patientID
            patient_meds = session.exec(
                PatientCurrentMeds.select().where(PatientCurrentMeds.patientID == self.patientID)
            ).first()

            # Update the fields with new values
            if patient_meds:
                patient_meds.medication1 = self.new_medication1
                patient_meds.dosage1 = self.new_dosage1
                patient_meds.frequency1 = self.new_frequency1
                patient_meds.medication2 = self.new_medication2
                patient_meds.dosage2 = self.new_dosage2
                patient_meds.frequency2 = self.new_frequency2
                patient_meds.medication3 = self.new_medication3
                patient_meds.dosage3 = self.new_dosage3
                patient_meds.frequency3 = self.new_frequency3

                session.commit()

class GetPatientMedHistory(rx.State):
    patientID: int  # Example patientID, replace with the actual ID you're querying for

    def get_patient_med_history(self):
        with rx.session() as session:
            patient_med_history = session.exec(
                PatientMedHistory.select().where(PatientMedHistory.patientID == self.patientID)
            ).first()
            return patient_med_history