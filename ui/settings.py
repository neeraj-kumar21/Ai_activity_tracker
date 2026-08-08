import customtkinter as ctk

class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        #  -------------Title ------------------

        title = ctk.CTkLabel(
            self,
            text="⚙️ Settings",
            font=("Arial", 32, "bold")
        )
        title.pack(pady=30)
