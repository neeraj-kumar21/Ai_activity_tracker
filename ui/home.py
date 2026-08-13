import customtkinter as ctk
from database import get_all_activity


class HomePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="#242424")

        # ================= HEADER =================

        header = ctk.CTkLabel(
            self,
            text="🏠 AI Activity Dashboard",
            font=("Arial", 32, "bold")
        )
        header.pack(pady=(25, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Monitor your activity and productivity",
            font=("Arial", 16)
        )
        subtitle.pack(pady=(0, 25))

        # ================= STATS =================

        self.stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.stats_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        self.sessions_card = ctk.CTkFrame(
            self.stats_frame,
            corner_radius=15
        )
        self.sessions_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10
        )

        self.sessions_label = ctk.CTkLabel(
            self.sessions_card,
            text="0",
            font=("Arial", 30, "bold")
        )
        self.sessions_label.pack(pady=(20, 5))

        ctk.CTkLabel(
            self.sessions_card,
            text="Total Sessions",
            font=("Arial", 15)
        ).pack(pady=(0, 20))

        # ================= TOTAL TIME =================

        self.time_card = ctk.CTkFrame(
            self.stats_frame,
            corner_radius=15
        )
        self.time_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10
        )

        self.time_label = ctk.CTkLabel(
            self.time_card,
            text="0 sec",
            font=("Arial", 30, "bold")
        )
        self.time_label.pack(pady=(20, 5))

        ctk.CTkLabel(
            self.time_card,
            text="Total Tracked Time",
            font=("Arial", 15)
        ).pack(pady=(0, 20))

        # ================= LATEST ACTIVITY =================

        self.latest_card = ctk.CTkFrame(
            self,
            corner_radius=15
        )
        self.latest_card.pack(
            fill="x",
            padx=40,
            pady=25
        )

        ctk.CTkLabel(
            self.latest_card,
            text="Latest Activity",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.latest_label = ctk.CTkLabel(
            self.latest_card,
            text="No activity yet.",
            font=("Arial", 15),
            anchor="w",
            justify="left"
        )
        self.latest_label.pack(
            anchor="w",
            padx=20,
            pady=(5, 20)
        )

        # ================= RECENT ACTIVITY =================

        ctk.CTkLabel(
            self,
            text="Recent Activity",
            font=("Arial", 22, "bold")
        ).pack(
            anchor="w",
            padx=40,
            pady=(5, 10)
        )

        self.activity_box = ctk.CTkScrollableFrame(
            self,
            height=250,
            corner_radius=15
        )
        self.activity_box.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=(0, 20)
        )

        # Load data
        self.load_data()

        # Refresh every 5 seconds
        self.after(5000, self.auto_refresh)

    # ==========================================
    # LOAD DATABASE DATA
    # ==========================================

    def load_data(self):

        activities = get_all_activity()

        print("HOME DATA:", activities)

        # Clear old activity cards
        for widget in self.activity_box.winfo_children():
            widget.destroy()

        if not activities:

            self.sessions_label.configure(text="0")
            self.time_label.configure(text="0 sec")
            self.latest_label.configure(
                text="No activity recorded yet."
            )

            ctk.CTkLabel(
                self.activity_box,
                text="No activity yet.",
                font=("Arial", 16)
            ).pack(pady=30)

            return

        # ================= SESSION COUNT =================

        total_sessions = len(activities)

        self.sessions_label.configure(
            text=str(total_sessions)
        )

        # ================= TOTAL TIME =================

        total_seconds = 0

        for activity in activities:

            duration = activity[3]

            try:

                # Example:
                # 0:00:10.123456

                parts = duration.split(":")

                hours = int(parts[0])
                minutes = int(parts[1])
                seconds = float(parts[2])

                total_seconds += (
                    hours * 3600
                    + minutes * 60
                    + seconds
                )

            except Exception:
                pass

        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)

        if minutes > 0:

            total_time = f"{minutes} min {seconds} sec"

        else:

            total_time = f"{seconds} sec"

        self.time_label.configure(
            text=total_time
        )

        # ================= LATEST =================

        latest = activities[0]

        latest_time = latest[1]
        latest_title = latest[4]
        latest_duration = latest[3]

        self.latest_label.configure(
            text=(
                f"Application: {latest_title}\n"
                f"Started: {latest_time}\n"
                f"Duration: {latest_duration}"
            )
        )

        # ================= ACTIVITY LIST =================

        for activity in activities[:20]:

            activity_id = activity[0]
            start_time = activity[1]
            end_time = activity[2]
            duration = activity[3]
            title = activity[4]

            card = ctk.CTkFrame(
                self.activity_box,
                corner_radius=10
            )

            card.pack(
                fill="x",
                padx=5,
                pady=5
            )

            ctk.CTkLabel(
                card,
                text=f"🖥 {title}",
                font=("Arial", 15, "bold"),
                anchor="w"
            ).pack(
                anchor="w",
                padx=15,
                pady=(10, 2)
            )

            ctk.CTkLabel(
                card,
                text=(
                    f"Start: {start_time}    "
                    f"End: {end_time}    "
                    f"Duration: {duration}"
                ),
                font=("Arial", 12),
                anchor="w"
            ).pack(
                anchor="w",
                padx=15,
                pady=(2, 10)
            )

    # ==========================================
    # AUTO REFRESH
    # ==========================================

    def auto_refresh(self):

        self.load_data()

        self.after(
            5000,
            self.auto_refresh
        )