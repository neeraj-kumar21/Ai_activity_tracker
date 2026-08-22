import customtkinter as ctk
from ui.home import HomePage
from ui.analytics import AnalyticsPage
from ui.browser_page import BrowserPage
from ui.report_page import ReportsPage
from ui.settings import SettingsPage


def start_dashboard(app):
    """
    Builds the dashboard UI INSIDE an existing CTk root window
    (passed in as `app`). Does NOT create its own CTk() and does
    NOT call mainloop() — app.py owns the single mainloop.
    """
    # Appearance
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard)

    app.title("AI Activity Tracker")

    # ---- Resizable + minimize/maximize enabled ----
    app.resizable(True, True)
    app.minsize(900, 550)          # window ko itna chota se zyada shrink na hone dein

    # ---- Center on screen at the dashboard's default size ----
    width, height = 1200, 700
    app.update_idletasks()
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    app.geometry(f"{width}x{height}+{x}+{y}")

    # --------------Sidebar ------------------
    sidebar_frame = ctk.CTkFrame(app, width=200)
    sidebar_frame.pack(side="left", fill="y")

    title = ctk.CTkLabel(
        sidebar_frame,
        text="AI Activity Tracker",
        font=("Arial", 20, "bold")
    )
    title.pack(pady=30)

    # ================== Main Area =======================

    main_frame = ctk.CTkFrame(app)
    main_frame.pack(fill="both", expand=True)

    # =================== Page Functions =====================

    def clear_page():
        for widget in main_frame.winfo_children():
            widget.destroy()

    def show_home():
        clear_page()
        home_page = HomePage(main_frame)
        home_page.pack(fill="both", expand=True)

    def show_analytics():
        clear_page()
        analytics_page = AnalyticsPage(main_frame)
        analytics_page.pack(fill="both", expand=True)

    def show_browser():
        clear_page()
        browser_page = BrowserPage(main_frame)
        browser_page.pack(fill="both", expand=True)

    def show_reports():
        clear_page()
        reports_page = ReportsPage(main_frame)
        reports_page.pack(fill="both", expand=True)

    def show_settings():
        clear_page()
        settings_page = SettingsPage(main_frame)
        settings_page.pack(fill="both", expand=True)

    # ======================== Buttons =========================

    home_btn = ctk.CTkButton(sidebar_frame, text="🏠 Home", command=show_home)
    home_btn.pack(pady=10, padx=20)

    analytics_btn = ctk.CTkButton(sidebar_frame, text="📊 Analytics", command=show_analytics)
    analytics_btn.pack(pady=10, padx=20)

    browser_btn = ctk.CTkButton(sidebar_frame, text="🌐 Browser Extension", command=show_browser)
    browser_btn.pack(pady=10, padx=20)

    reports_btn = ctk.CTkButton(sidebar_frame, text="📄 Reports", command=show_reports)
    reports_btn.pack(pady=10, padx=20)

    settings_btn = ctk.CTkButton(sidebar_frame, text="⚙️ Settings", command=show_settings)
    settings_btn.pack(pady=10, padx=20)

    # ==================== Start with Home =====================

    show_home()