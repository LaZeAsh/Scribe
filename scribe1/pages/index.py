"""The home page of the app."""

from scribe1 import styles
from scribe1.templates import template
from scribe1.components.geminiComponent import scribeGenerator
# from scribe1.database.queries1.healthPractitionerQueries import addHealthPractitioner 
import scribe1.database.queries1.healthPractitioner

import reflex as rx

class LoginState(rx.State):

    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        addHealthPractition
        self.form_data = form_data
        # scribeGenerator1=scribeGenerator
        # scribeGenerator(text_scribe)
        return rx.redirect("/profile/1")
    

@rx.page(route="/", title="Home")
def index() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.heading("Scribe", align="center"),
                rx.input(
                    placeholder="Username",
                    name="username",
                    size="lg",
                ),
                rx.input(
                    placeholder="Password",
                    name="password",
                    size="lg",
                ),
                rx.button("Submit", type="submit", size="4"),
                align="center",
            ),
            on_submit=LoginState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(LoginState.form_data.to_string()),
        )
        
    


    """The home page.

    Returns:
        The UI for the home page.
    """
    # with open("README.md", encoding="utf-8") as readme:
    #     content = readme.read()
    # return rx.markdown(content, component_map=styles.markdown_style)

