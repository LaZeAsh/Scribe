import reflex as rx

class alertState(rx.State):
    alertNotifications: list[str] = ["Wrong Diagnosis", "Contradination", "Wrong dosage"]
def alerts() -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(rx.button("See Alerts")),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.flex(
                    rx.drawer.close(rx.box(rx.button("Close"))),
                    align_items="start",
                    direction="column",
                ),
                rx.vstack(
                    rx.foreach(
                        alertState.alertNotifications,
                        lambda alertNotification, idx: 
                        # rx.container(
                            rx.card(
                                alertNotification,
                                # width="100%",
                            ),
                        #     size="3",
                        # ),
                    ),
                ),
                top="auto",
                left="auto",
                height="100%",
                width="20em",
                # padding="2em",
                background_color="#FFF"
                # background_color=rx.color("green", 3)
            ),
        ),
        direction="right",
    )


