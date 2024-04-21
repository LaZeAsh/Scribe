import firebase_admin 
from firebase_admin import db, credentials

class backendState(rx.State):
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred, "databaseURL": "https://scribe-b7437-default-rtdb.firebaseio.com/")
    
    ref = db.reference("/")




















    # A base var for the list of colors to cycle through.
    colors: list[str] = [
        "black",
        "red",
        "green",
        "blue",
        "purple",
    ]

    # A base var for the index of the current color.
    index: int = 0

    def next_color(self):
        """An event handler to go to the next color."""
        # Event handlers can modify the base vars.
        # Here we reference the base vars `colors` and `index`.
        self.index = (self.index + 1) % len(self.colors)

    @rx.var
    def color(self) -> str:
        """A computed var that returns the current color."""
        # Computed vars update automatically when the state changes.
        return self.colors[self.index]