import customtkinter as ctk
from database import get_analytics_data


class AnalyticsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # =========================================
        # TITLE
        # =========================================

        title = ctk.CTkLabel(
            self,
            text="📊 Analytics Dashboard",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=(30, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Analyze your computer activity",
            font=("Arial", 16)
        )

        subtitle.pack(pady=(0, 20))

        # =========================================
        # STATS FRAME
        # =========================================

        stats_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        stats_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        # Total Time
        self.total_time_label = ctk.CTkLabel(
            stats_frame,
            text="⏱️ Total Time\n0m",
            font=("Arial", 20, "bold")
        )

        self.total_time_label.pack(
            side="left",
            expand=True,
            pady=20
        )

        # Sessions
        self.sessions_label = ctk.CTkLabel(
            stats_frame,
            text="🔄 Sessions\n0",
            font=("Arial", 20, "bold")
        )

        self.sessions_label.pack(
            side="left",
            expand=True,
            pady=20
        )

        # Most Used
        self.most_used_label = ctk.CTkLabel(
            stats_frame,
            text="🏆 Most Used\nNone",
            font=("Arial", 20, "bold")
        )

        self.most_used_label.pack(
            side="left",
            expand=True,
            pady=20
        )

        # =========================================
        # APPLICATION USAGE TITLE
        # =========================================

        usage_title = ctk.CTkLabel(
            self,
            text="Application Usage",
            font=("Arial", 24, "bold")
        )

        usage_title.pack(
            anchor="w",
            padx=30,
            pady=(20, 10)
        )

        # =========================================
        # USAGE CONTAINER
        # =========================================

        self.usage_frame = ctk.CTkScrollableFrame(
            self,
            corner_radius=15
        )

        self.usage_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        # =========================================
        # REFRESH BUTTON
        # =========================================

        refresh_button = ctk.CTkButton(
            self,
            text="🔄 Refresh Analytics",
            command=self.load_analytics,
            width=180
        )

        refresh_button.pack(
            pady=15
        )

        # Load data
        self.load_analytics()

    # =========================================
    # LOAD ANALYTICS
    # =========================================

    def load_analytics(self):

        # Clear old application widgets
        for widget in self.usage_frame.winfo_children():
            widget.destroy()

        # Get database data
        rows = get_analytics_data()

        if not rows:

            self.total_time_label.configure(
                text="⏱️ Total Time\n0m"
            )

            self.sessions_label.configure(
                text="🔄 Sessions\n0"
            )

            self.most_used_label.configure(
                text="🏆 Most Used\nNone"
            )

            no_data = ctk.CTkLabel(
                self.usage_frame,
                text="📭 No activity data available yet.",
                font=("Arial", 18)
            )

            no_data.pack(pady=40)

            return

        # =====================================
        # CALCULATE DATA
        # =====================================

        application_time = {}

        total_seconds = 0

        for window_title, duration in rows:

            seconds = self.convert_duration_to_seconds(
                duration
            )

            total_seconds += seconds

            if window_title:

                if window_title not in application_time:
                    application_time[window_title] = 0

                application_time[window_title] += seconds

        # =====================================
        # TOTAL TIME
        # =====================================

        total_text = self.format_duration(
            total_seconds
        )

        self.total_time_label.configure(
            text=f"⏱️ Total Time\n{total_text}"
        )

        # =====================================
        # SESSIONS
        # =====================================

        self.sessions_label.configure(
            text=f"🔄 Sessions\n{len(rows)}"
        )

        # =====================================
        # MOST USED
        # =====================================

        if application_time:

            most_used = max(
                application_time,
                key=application_time.get
            )

            most_used_time = self.format_duration(
                application_time[most_used]
            )

            # Limit long window title
            display_name = most_used[:35]

            self.most_used_label.configure(
                text=f"🏆 Most Used\n{display_name}"
            )

        # =====================================
        # SORT APPLICATIONS
        # =====================================

        sorted_apps = sorted(
            application_time.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # =====================================
        # DISPLAY TOP APPLICATIONS
        # =====================================

        for app_name, seconds in sorted_apps[:10]:

            duration_text = self.format_duration(
                seconds
            )

            card = ctk.CTkFrame(
                self.usage_frame,
                corner_radius=10
            )

            card.pack(
                fill="x",
                padx=10,
                pady=5
            )

            name_label = ctk.CTkLabel(
                card,
                text=app_name,
                font=("Arial", 15, "bold"),
                anchor="w"
            )

            name_label.pack(
                side="left",
                padx=15,
                pady=12
            )

            time_label = ctk.CTkLabel(
                card,
                text=duration_text,
                font=("Arial", 15)
            )

            time_label.pack(
                side="right",
                padx=15,
                pady=12
            )

    # =========================================
    # CONVERT DURATION
    # =========================================

    def convert_duration_to_seconds(self, duration):

        try:

            # Example:
            # 0:02:15.123456

            parts = str(duration).split(":")

            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = float(parts[2])

            return (
                hours * 3600
                + minutes * 60
                + seconds
            )

        except Exception:

            return 0

    # =========================================
    # FORMAT DURATION
    # =========================================

    def format_duration(self, seconds):

        seconds = int(seconds)

        hours = seconds // 3600

        minutes = (
            seconds % 3600
        ) // 60

        remaining_seconds = seconds % 60

        if hours > 0:

            return f"{hours}h {minutes}m"

        elif minutes > 0:

            return f"{minutes}m {remaining_seconds}s"

        else:

            return f"{remaining_seconds}s"