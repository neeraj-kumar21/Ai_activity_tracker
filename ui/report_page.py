import customtkinter as ctk

class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        #  -------------Title ------------------

        title = ctk.CTkLabel(
            self,
            text="📄 Reports",
            font=("Arial", 32, "bold")
        )
        title.pack(pady=30)

        info = ctk.CTkLabel(
            self,
            text="Reports page is under development. Stay tuned for updates!",
            font=("Arial", 18)
        )
        info.pack(pady=20)