import reflex as rx
class VisitFormState(rx.State):
    visit_form_fields: list[str] = ["Symtoms", "HPI", "PE", "Constitutional", "differental_diagnosis", "Additional"]
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submission."""
        self.form_data = form_data

def visitLink(date) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(date)),
        rx.dialog.content(
            rx.dialog.title("Patient: " + "Visit: " + date),
            rx.dialog.description(
        rx.form(
            rx.vstack(
                rx.chakra.form(
                    rx.foreach(
                        VisitFormState.visit_form_fields,  
                        lambda field, idx: rx.chakra.form_control(
                            rx.chakra.form_label(field, html_for=field),
                            rx.text_area(),
                            is_required=True
                        )       
                    )
                ),
            ),
        ),
            ),
            rx.dialog.close(
                rx.button("Close Dialog", size="3"),
            ),
        ),
    )