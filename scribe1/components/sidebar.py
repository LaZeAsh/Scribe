"""Sidebar component for the app."""

from scribe1 import styles

import reflex as rx
from scribe1.pages.patientData import testData

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
    
    
    patients_list: list[dict[str, str]] = [
            {"name": f"{info[0]['patientInfo1']['firstName']} {info[0]['patientInfo1']['lastName']}", "patientID": pid}
            for pid, info in testData.items()
        ]


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
                    SidebarState.patients_list,
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
