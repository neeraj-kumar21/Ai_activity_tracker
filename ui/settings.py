import customtkinter as ctk
import os

from config import load_settings, save_settings


class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.settings = load_settings()

        # =========================================
        # TITLE
        # =========================================

        title = ctk.CTkLabel(
            self,
            text="⚙️ Settings",
            font=("Arial", 32, "bold")
        )

        title.pack(
            pady=(30, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Customize AI Activity Tracker",
            font=("Arial", 16)
        )

        subtitle.pack(
            pady=(0, 20)
        )

        # =========================================
        # SETTINGS CONTAINER
        # =========================================

        container = ctk.CTkScrollableFrame(
            self,
            corner_radius=15
        )

        container.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=10
        )

        # =========================================
        # APPEARANCE
        # =========================================

        ctk.CTkLabel(
            container,
            text="🎨 Appearance",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.appearance_menu = ctk.CTkOptionMenu(
            container,
            values=[
                "Dark",
                "Light",
                "System"
            ]
        )

        self.appearance_menu.set(
            self.settings["appearance"].capitalize()
        )

        self.appearance_menu.pack(
            anchor="w",
            padx=20,
            pady=(5, 20)
        )

        # =========================================
        # ACCENT COLOR
        # =========================================

        ctk.CTkLabel(
            container,
            text="🌈 Accent Color",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(10, 5)
        )

        self.accent_menu = ctk.CTkOptionMenu(
            container,
            values=[
                "blue",
                "green",
                "dark-blue",
                "Pink",
                "Gray"
            ]
        )

        self.accent_menu.set(
            self.settings["accent_color"]
        )

        self.accent_menu.pack(
            anchor="w",
            padx=20,
            pady=(5, 20)
        )

        # =========================================
        # REPORT INTERVAL
        # =========================================

        ctk.CTkLabel(
            container,
            text="⏱️ Report Interval",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(10, 5)
        )

        self.report_interval = ctk.CTkOptionMenu(
            container,
            values=[
                "1 Hour",
                "2 Hours",
                "4 Hours",
                "6 Hours",
                "8 Hours",
                "12 Hours",
                "24 Hours"
            ]
        )

        current_hours = self.settings[
            "report_interval_hours"
        ]

        self.report_interval.set(
            f"{current_hours} Hours"
        )

        self.report_interval.pack(
            anchor="w",
            padx=20,
            pady=(5, 20)
        )

        # =========================================
        # AUTO REFRESH
        # =========================================

        ctk.CTkLabel(
            container,
            text="🔄 Auto Refresh",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(10, 5)
        )

        self.auto_refresh_switch = ctk.CTkSwitch(
            container,
            text="Automatically refresh dashboard"
        )

        if self.settings["auto_refresh"]:
            self.auto_refresh_switch.select()

        self.auto_refresh_switch.pack(
            anchor="w",
            padx=20,
            pady=(5, 20)
        )

        # =========================================
        # REPORT FOLDER
        # =========================================

        ctk.CTkLabel(
            container,
            text="📁 Report Folder",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(10, 5)
        )

        self.folder_entry = ctk.CTkEntry(
            container,
            width=400
        )

        self.folder_entry.insert(
            0,
            self.settings["report_folder"]
        )

        self.folder_entry.pack(
            anchor="w",
            padx=20,
            pady=(5, 10)
        )

        # =========================================
        # OPEN FOLDER
        # =========================================

        ctk.CTkButton(
            container,
            text="📂 Open Report Folder",
            command=self.open_reports_folder
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

        # =========================================
        # TRACKER STATUS
        # =========================================

        ctk.CTkLabel(
            container,
            text="▶️ Tracker",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(10, 5)
        )

        self.tracker_switch = ctk.CTkSwitch(
            container,
            text="Enable activity tracking"
        )

        if self.settings["tracker_enabled"]:
            self.tracker_switch.select()

        self.tracker_switch.pack(
            anchor="w",
            padx=20,
            pady=(5, 20)
        )

        # =========================================
        # STATUS
        # =========================================

        self.status_label = ctk.CTkLabel(
            container,
            text="",
            font=("Arial", 14)
        )

        self.status_label.pack(
            pady=15
        )

        # =========================================
        # SAVE BUTTON
        # =========================================

        ctk.CTkButton(
            self,
            text="💾 Save Settings",
            width=220,
            height=45,
            command=self.save
        ).pack(
            pady=20
        )

    # =========================================
    # SAVE
    # =========================================

    def save(self):

        appearance = self.appearance_menu.get().lower()

        accent_color = self.accent_menu.get()

        interval_text = self.report_interval.get()

        interval_hours = int(
            interval_text.split()[0]
        )

        auto_refresh = (
            self.auto_refresh_switch.get() == 1
        )

        tracker_enabled = (
            self.tracker_switch.get() == 1
        )

        report_folder = (
            self.folder_entry.get().strip()
        )

        if not report_folder:
            report_folder = "reports"

        # =====================================
        # UPDATE SETTINGS
        # =====================================

        self.settings = {

            "appearance": appearance,

            "accent_color": accent_color,

            "report_interval_hours":
                interval_hours,

            "auto_refresh":
                auto_refresh,

            "report_folder":
                report_folder,

            "tracker_enabled":
                tracker_enabled
        }

        save_settings(
            self.settings
        )

        # Apply theme immediately
        ctk.set_appearance_mode(
            appearance
        )

        ctk.set_default_color_theme(
            accent_color
        )

        # Create folder
        os.makedirs(
            report_folder,
            exist_ok=True
        )

        self.status_label.configure(
            text="✅ Settings saved successfully!"
        )

        print(
            "Settings saved:",
            self.settings
        )

    # =========================================
    # OPEN REPORT FOLDER
    # =========================================

    def open_reports_folder(self):

        folder = self.folder_entry.get().strip()

        if not folder:
            folder = "reports"

        folder = os.path.abspath(
            folder
        )

        os.makedirs(
            folder,
            exist_ok=True
        )

        os.startfile(folder)