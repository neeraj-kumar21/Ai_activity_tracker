import customtkinter as ctk
from database import get_all_activity
from ai_analyzer import generate_insight


class HomePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # ================= HEADER =================

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=30, pady=(25, 10))

        title = ctk.CTkLabel(
            header,
            text="🏠 AI Activity Dashboard",
            font=("Arial", 32, "bold")
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Monitor your activity and productivity",
            font=("Arial", 15)
        )
        subtitle.pack(anchor="w", pady=(5, 0))

    def load_ai_insight(self):

        try:

            insight = generate_insight()

            score = insight["score"]
            productive = insight["productive_time"]
            distracting = insight["distracting_time"]
            top_app = insight["top_app"]
            message = insight["message"]

            self.score_card.value_label.configure(
                text=f"{score}%"
            )

            self.insight_label.configure(
                text=(
                    f"{message}\n\n"
                    f"🚀 Productive: {productive}\n"
                    f"⚠️ Distracting: {distracting}\n"
                    f"💻 Most Used: {top_app}"
                )
            )

        except Exception as e:

            print("AI Insight Error:", e)

            self.insight_label.configure(
                text="Unable to analyze activity."
            )


        # ================= STATUS =================

        status_frame = ctk.CTkFrame(self)
        status_frame.pack(fill="x", padx=30, pady=15)

        status_title = ctk.CTkLabel(
            status_frame,
            text="● Tracking Active",
            font=("Arial", 17, "bold")
        )
        status_title.pack(side="left", padx=20, pady=15)


        # ================= STATISTICS =================

        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(fill="x", padx=30, pady=10)

        # Total Activity
        self.total_card = self.create_card(
            stats_frame,
            "⏱ Total Activity",
            "0h 0m"
        )
        self.total_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        # Productive
        self.productive_card = self.create_card(
            stats_frame,
            "🚀 Productive",
            "0h 0m"
        )
        self.productive_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10
        )

        # Applications
        self.apps_card = self.create_card(
            stats_frame,
            "💻 Applications",
            "0"
        )
        self.apps_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10
        )

        # Productivity Score
        self.score_card = self.create_card(
            stats_frame,
            "📊 Productivity",
            "0%"
        )
        self.score_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0)
        )


        # ================= TODAY'S ACTIVITY =================

        activity_title = ctk.CTkLabel(
            self,
            text="📈 Today's Activity",
            font=("Arial", 22, "bold")
        )
        activity_title.pack(
            anchor="w",
            padx=30,
            pady=(25, 10)
        )

        self.activity_frame = ctk.CTkScrollableFrame(
            self,
            height=220
        )
        self.activity_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 20)
        )


        # ================= LOAD DATA =================

        self.load_dashboard()



        # ================= AI INSIGHT =================

        insight_title = ctk.CTkLabel(
            self,
            text="🤖 AI Productivity Insight",
            font=("Arial", 22, "bold")
        )
        insight_title.pack(
            anchor="w",
            padx=30,
            pady=(10, 5)
        )

        self.insight_label = ctk.CTkLabel(
            self,
            text="Analyzing your activity...",
            font=("Arial", 15),
            wraplength=900,
            justify="left"
        )
        self.insight_label.pack(
            anchor="w",
            padx=30,
            pady=(0, 20)
        )

        self.load_ai_insight()

                


    # ==================================================
    # CREATE STAT CARD
    # ==================================================

    def create_card(self, parent, title, value):

        card = ctk.CTkFrame(parent)

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 15)
        )
        title_label.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 26, "bold")
        )
        value_label.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        card.value_label = value_label

        return card


    # ==================================================
    # LOAD DASHBOARD DATA
    # ==================================================

    def load_dashboard(self):

        try:

            activities = get_all_activity()

            if not activities:
                self.show_no_activity()
                return


            # Total activity
            total_seconds = 0

            applications = set()


            for activity in activities:

                window_title = activity[4]
                duration = activity[3]

                applications.add(window_title)

                total_seconds += self.duration_to_seconds(
                    duration
                )


            # Convert total time
            total_time = self.format_duration(
                total_seconds
            )


            # Update cards
            self.total_card.value_label.configure(
                text=total_time
            )

            self.apps_card.value_label.configure(
                text=str(len(applications))
            )


            # Temporary productivity calculation
            #
            # Later we will replace this with
            # real AI analysis.

            analysis = generate_insight()

            self.productive_card.value_label.configure(
                text=analysis["productive_time"]
            )

            self.score_card.value_label.configure(
                text=f'{analysis["score"]}%'
            ) 

            # Show activity list
            self.show_activities(activities)


        except Exception as e:

            print("Dashboard error:", e)


    # ==================================================
    # SHOW ACTIVITIES
    # ==================================================

    def show_activities(self, activities):

        for widget in self.activity_frame.winfo_children():
            widget.destroy()


        # Latest 10 activities
        for activity in activities[:10]:

            start_time = activity[1]
            end_time = activity[2]
            duration = activity[3]
            window_title = activity[4]


            card = ctk.CTkFrame(
                self.activity_frame
            )

            card.pack(
                fill="x",
                padx=10,
                pady=5
            )


            title = ctk.CTkLabel(
                card,
                text=f"💻 {window_title}",
                font=("Arial", 15, "bold"),
                anchor="w"
            )

            title.pack(
                fill="x",
                padx=15,
                pady=(10, 2)
            )


            info = ctk.CTkLabel(
                card,
                text=f"⏱ {duration}   |   {start_time}",
                anchor="w"
            )

            info.pack(
                fill="x",
                padx=15,
                pady=(2, 10)
            )


    # ==================================================
    # NO ACTIVITY
    # ==================================================

    def show_no_activity(self):

        for widget in self.activity_frame.winfo_children():
            widget.destroy()


        label = ctk.CTkLabel(
            self.activity_frame,
            text="No activity recorded yet.",
            font=("Arial", 18)
        )

        label.pack(pady=40)


    # ==================================================
    # DURATION → SECONDS
    # ==================================================

    def duration_to_seconds(self, duration):

        try:

            # Example:
            # 0:00:05.123456

            parts = str(duration).split(":")

            hours = int(parts[0])
            minutes = int(parts[1])

            seconds = float(parts[2])

            return (
                hours * 3600
                + minutes * 60
                + seconds
            )

        except:

            return 0


    # ==================================================
    # SECONDS → READABLE TIME
    # ==================================================

    def format_duration(self, seconds):

        seconds = int(seconds)

        hours = seconds // 3600

        minutes = (seconds % 3600) // 60

        if hours > 0:

            return f"{hours}h {minutes}m"

        return f"{minutes}m"