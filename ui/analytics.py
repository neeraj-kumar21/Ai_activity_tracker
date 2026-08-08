import customtkinter as ctk

class AnalyticsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        #  -------------Title ------------------

        title = ctk.CTkLabel(
            self,
            text="📊 Analytics Dashboard",
            font=("Arial", 32, "bold")
        )
        title.pack(pady=30)

        info = ctk.CTkLabel(
            self,
            text="Analytics page is under development. Stay tuned for updates!",
            font=("Arial", 18)
        )
        info.pack(pady=20)

        # lable = ctk.CTkLabel(
        #     self,
        #     text="Analytics",
        #     font=("Arial" , 30 ,"bold")
        # )

        # lable.pack(pady=30)