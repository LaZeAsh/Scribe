"""Sidebar component for the app."""

from scribe1 import styles

import reflex as rx

def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        rx.heading("Scribe", size='9'),
        rx.spacer(),
        align="center",
        width="100%",
        border_bottom=styles.border,
        padding_x="1em",
        padding_y="2em",
    )



class SidebarState(rx.State):
    patients: list[dict[str, str]] = [
        {"name": "John Eastwood", "patientID": "1"},
        {"name": "Paul Wu", "patientID": "2"},
        {"name": "Leena Khan", "patientID": "3"},
    ]
    def load_patient_info(self, patient_id: str):
        # Placeholder: Load patient info based on patient_id
        # This is where you'd query your data source for the patient's info
        self.patient_name = f"Loaded info for patient {patient_id}"


def sidebar_item(text: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == url.lower()) | (
        (rx.State.router.page.path == "/") & text == "Home"
    )

    return rx.link(
        rx.hstack(
            rx.text(
                text,
            ),
            bg=rx.cond(
                active,
                rx.color("accent", 2),
                "transparent",
            ),
            border=rx.cond(
                active,
                f"1px solid {rx.color('accent', 6)}",
                f"1px solid {rx.color('gray', 6)}",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            padding="1em",
        ),
        href=url,
        width="100%",
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
               
                rx.foreach(
                    SidebarState.patients,
                    lambda patient, idx: sidebar_item(
                            text=patient["name"],
                            url="/profile/" + patient['patientID'],
                        )
                ), 


                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
            ),
            rx.spacer(),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        border_right=styles.border,
    )
