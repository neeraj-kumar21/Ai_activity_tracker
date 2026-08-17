import sqlite3
import os
from datetime import datetime,timedelta

from openpyxl import Workbook
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph,Spacer,Table
from reportlab.lib.styles import getSampleStyleSheet

DB_PATH = "data/activity_tracker.db"
REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)

def get_activity_data(start_time,end_time):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT start_time, end_time, duration, window_title
        FROM activity_log
        WHERE start_time >= ?
        AND start_time < ?
        ORDER BY id ASC
    """, (
        start_time,
        end_time
    ))

    rows = cursor.fetchall()

    conn.close()

    return rows

def create_excel_report(rows, start_time, end_time):

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    filename = (
        f"activity_report_"
        f"{start_time.strftime('%Y%m%d_%H%M')}_"
        f"{end_time.strftime('%Y%m%d_%H%M')}.xlsx"
    )

    filepath = os.path.join(REPORT_FOLDER, filename)

    workbook = Workbook()
    sheet = workbook.active

    sheet.title = "Activity Report"

    sheet.append([
        "Start Time",
        "End Time",
        "Duration",
        "Application"
    ])

    for row in rows:
        sheet.append(row)

    workbook.save(filepath)

    return filepath


def create_pdf_report(rows, start_time, end_time):

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    filename = (
        f"activity_report_"
        f"{start_time.strftime('%Y%m%d_%H%M')}_"
        f"{end_time.strftime('%Y%m%d_%H%M')}.pdf"
    )

    filepath = os.path.join(REPORT_FOLDER, filename)

    document = SimpleDocTemplate(
        filepath,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI Activity Tracker - 8 Hour Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"Start: {start_time}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"End: {end_time}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    table_data = [
        [
            "Start Time",
            "End Time",
            "Duration",
            "Application"
        ]
    ]

    for row in rows:
        table_data.append(list(row))

    table = Table(table_data)

    elements.append(table)

    document.build(elements)

    return filepath

# ====================== Save Report in Database ================


def save_report_to_database(
    start_time,
    end_time,
    excel_path,
    pdf_path
):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Ensure the reports table exists (auto-creates on first run,
    # fixes "no such table: reports" error)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            generated_at TEXT,
            start_time TEXT,
            end_time TEXT,
            excel_path TEXT,
            pdf_path TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO reports
        (
            generated_at,
            start_time,
            end_time,
            excel_path,
            pdf_path
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        str(start_time),
        str(end_time),
        excel_path,
        pdf_path
    ))

    conn.commit()
    conn.close()


# ===================

def generate_report(start_time, end_time):

    print("\n==============================")
    print("Generating 8 Hour Report...")
    print("==============================")

    rows = get_activity_data(
        start_time,
        end_time
    )

    if not rows:
        print("No activity found for this period.")
        return

    excel_path = create_excel_report(
        rows,
        start_time,
        end_time
    )

    pdf_path = create_pdf_report(
        rows,
        start_time,
        end_time
    )

    save_report_to_database(
        start_time,
        end_time,
        excel_path,
        pdf_path
    )

    print("Excel Report:", excel_path)
    print("PDF Report:", pdf_path)

    print("==============================")
    print("Report Generated Successfully")
    print("==============================")