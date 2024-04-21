class PatientState(rx.State):

    patients: list[dict[str, str]] = [
        {
            "name": "John Eastwood",
            "patientID": "1",
        },
        {
            "name": "Paul Wu",
            "patientID": "2",
        },
        {
            "name": "Leena Khan",
            "patientID": "3",
        },
    ]

    @rx.var
    def patient_info(self) -> str:
        args = self.router.page.params
        patient_id = args.get("patient_id", [])
        return f"Profile for Patient ID: {', '.join(patient_id)}"

    @rx.page(route="/patient-profile/[...patient_id]")
    def patient_profile():
        return rx.center(rx.text(State.patient_info))

app = rx.App()