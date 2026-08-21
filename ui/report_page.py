import customtkinter as ctk
import os
import subprocess
from database import get_reports


class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # =========================================
        # HEADER
        # =========================================

        title = ctk.CTkLabel(
            self,
            text="📄 Reports",
            font=("Arial", 32, "bold")
        )
        title.pack(pady=(30, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Your generated activity reports",
            font=("Arial", 16)
        )
        subtitle.pack(pady=(0, 20))

        # =========================================
        # REPORT CONTAINER
        # =========================================

        self.report_container = ctk.CTkScrollableFrame(
            self,
            corner_radius=15
        )

        self.report_container.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        # Load reports
        self.load_reports()

    # =========================================
    # LOAD REPORTS
    # =========================================

    def load_reports(self):

        # Clear old widgets
        for widget in self.report_container.winfo_children():
            widget.destroy()

        reports = get_reports()

        if not reports:

            no_report = ctk.CTkLabel(
                self.report_container,
                text="📭 No reports generated yet.",
                font=("Arial", 20)
            )

            no_report.pack(pady=50)

            return

        # Show latest first
        for report in reports:

            (
                report_id,
                generated_at,
                start_time,
                end_time,
                excel_path,
                pdf_path
            ) = report

            self.create_report_card(
                report_id,
                generated_at,
                start_time,
                end_time,
                excel_path,
                pdf_path
            )

    # =========================================
    # CREATE REPORT CARD
    # =========================================

    def create_report_card(
        self,
        report_id,
        generated_at,
        start_time,
        end_time,
        excel_path,
        pdf_path
    ):

        card = ctk.CTkFrame(
            self.report_container,
            corner_radius=15
        )

        card.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # =====================================
        # REPORT TITLE
        # =====================================

        report_title = ctk.CTkLabel(
            card,
            text=f"📊 Activity Report #{report_id}",
            font=("Arial", 20, "bold")
        )

        report_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        # =====================================
        # GENERATED TIME
        # =====================================

        generated_label = ctk.CTkLabel(
            card,
            text=f"Generated: {generated_at}",
            font=("Arial", 14)
        )

        generated_label.pack(
            anchor="w",
            padx=20,
            pady=3
        )

        # =====================================
        # REPORT PERIOD
        # =====================================

        period_label = ctk.CTkLabel(
            card,
            text=f"Period: {start_time}  →  {end_time}",
            font=("Arial", 14)
        )

        period_label.pack(
            anchor="w",
            padx=20,
            pady=3
        )

        # =====================================
        # BUTTON FRAME
        # =====================================

        button_frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        button_frame.pack(
            anchor="w",
            padx=20,
            pady=15
        )

        # =====================================
        # EXCEL BUTTON
        # =====================================

        excel_button = ctk.CTkButton(
            button_frame,
            text="📊 Open Excel",
            width=150,
            command=lambda path=excel_path: self.open_file(path)
        )

        excel_button.pack(
            side="left",
            padx=(0, 10)
        )

        # =====================================
        # PDF BUTTON
        # =====================================

        pdf_button = ctk.CTkButton(
            button_frame,
            text="📄 Open PDF",
            width=150,
            command=lambda path=pdf_path: self.open_file(path)
        )

        pdf_button.pack(
            side="left"
        )

    # =========================================
    # OPEN FILE
    # =========================================

    def open_file(self, file_path):

        if not file_path:
            return

        if not os.path.exists(file_path):

            print("File not found:", file_path)

            return

        try:

            os.startfile(
                os.path.abspath(file_path)
            )

        except Exception as error:

            print("Could not open file:", error)