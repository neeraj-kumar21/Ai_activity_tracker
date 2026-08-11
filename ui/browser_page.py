import customtkinter as ctk
from database import get_browser_activity


class BrowserPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="🌐 Browser Activity",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        self.activity_frame = ctk.CTkScrollableFrame(
            self,
            width=800,
            height=500
        )
        self.activity_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        self.load_activity()

    def load_activity(self):

        activities = get_browser_activity()

        if not activities:
            label = ctk.CTkLabel(
                self.activity_frame,
                text="No Browser activity yet.",
                font=("Arial", 20)
            )
            label.pack(pady=50)
            return

        for timestamp, title, url in activities:

            card = ctk.CTkFrame(
                self.activity_frame,
                corner_radius=10
            )
            card.pack(
                fill="x",
                padx=10,
                pady=8
            )

            title_label = ctk.CTkLabel(
                card,
                text=f"Title: {title}",
                font=("Arial", 16, "bold"),
                anchor="w"
            )
            title_label.pack(
                fill="x",
                padx=15,
                pady=(10, 2)
            )

            url_label = ctk.CTkLabel(
                card,
                text=f"URL: {url}",
                font=("Arial", 13),
                anchor="w"
            )
            url_label.pack(
                fill="x",
                padx=15,
                pady=2
            )

            time_label = ctk.CTkLabel(
                card,
                text=f"Time: {timestamp}",
                font=("Arial", 12),
                anchor="w"
            )
            time_label.pack(
                fill="x",
                padx=15,
                pady=(2, 10)
            )