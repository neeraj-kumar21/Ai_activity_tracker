import customtkinter as ctk

# Appearrance 
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard),

# Create window
app = ctk.CTk()
app.title("AI Activity Tracker")
app.geometry("1200x700")

# --------------Sidebar ------------------
sidebar_frame = ctk.CTkFrame(app, width=200)
sidebar_frame.pack(side="left", fill="y")

title = ctk.CTkLabel(
    sidebar_frame,
    text="AI Activity Tracker",
    font=("Arial", 20, "bold")
)
title.pack(pady=30)

home_btn = ctk.CTkButton(sidebar_frame, text="🏠 Home")
home_btn.pack(pady=10, padx=20, )


analytics_btn = ctk.CTkButton(sidebar_frame, text="📊 Analytics")
analytics_btn.pack(pady=10, padx=20, )

browser_btn = ctk.CTkButton(sidebar_frame, text="🌐 Browser Extension")
browser_btn.pack(pady=10, padx=20, )    


reports_btn = ctk.CTkButton(sidebar_frame, text="📄 Reports")
reports_btn.pack(pady=10, padx=20, )


settings_btn = ctk.CTkButton(sidebar_frame, text="⚙️ Settings")
settings_btn.pack(pady=10, padx=20, )


# ------------------------ Main Area ------------------

main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True)

heading = ctk.CTkLabel(
    main_frame, 
    text="Welcome to AI Activity Tracker",
    font=("Arial", 24, "bold")
)
heading.pack(pady=40)

status = ctk.CTkLabel(
    main_frame,
    text="Status: Running 🟢",
    font=("Arial", 20)
)
status.pack(pady=20)

app.mainloop()

