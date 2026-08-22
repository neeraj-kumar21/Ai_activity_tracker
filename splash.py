import customtkinter as ctk


class SplashScreen:
    """
    Splash screen that renders INSIDE the app's existing root window
    (no separate CTk() instance, no separate mainloop()).
    Call SplashScreen(app_root, on_complete=callback) to show it.
    """

    def __init__(self, root, on_complete):

        self.root = root
        self.on_complete = on_complete

        self.root.title("AI Activity Tracker")
        self.root.geometry("600x380")
        self.root.resizable(False, False)
        self.root.configure(fg_color="#10141f")

        self.center_window()

        # =========================================
        # SPLASH FRAME (everything lives inside this
        # so we can cleanly destroy JUST this frame later)
        # =========================================

        self.frame = ctk.CTkFrame(self.root, fg_color="#10141f")
        self.frame.pack(fill="both", expand=True)

        # =========================================
        # MAIN TITLE (fades in)
        # =========================================

        self.title = ctk.CTkLabel(
            self.frame,
            text="AI ACTIVITY TRACKER",
            font=("Arial", 32, "bold"),
            text_color="#10141f"  # starts "invisible" (matches bg), fades to white
        )
        self.title.pack(pady=(80, 10))

        # =========================================
        # SUBTITLE
        # =========================================

        self.subtitle = ctk.CTkLabel(
            self.frame,
            text="Intelligent Productivity Monitoring",
            font=("Arial", 16),
            text_color="#10141f"
        )
        self.subtitle.pack(pady=5)

        # =========================================
        # LOADING TEXT
        # =========================================

        self.status = ctk.CTkLabel(
            self.frame,
            text="Initializing",
            font=("Arial", 14),
            text_color="gray70"
        )
        self.status.pack(pady=(45, 10))

        # =========================================
        # PROGRESS BAR
        # =========================================

        self.progress = ctk.CTkProgressBar(
            self.frame,
            width=400,
            progress_color="#3b82f6"
        )
        self.progress.pack(pady=10)
        self.progress.set(0)

        # =========================================
        # ANIMATION STATE
        # =========================================

        self.step = 0
        self.dot_count = 0
        self.after_id = None          # track scheduled callback so we can cancel it
        self.fade_step = 0

        self.fade_in()
        self.animate()

    # =========================================
    # CENTER WINDOW
    # =========================================

    def center_window(self):
        self.root.update_idletasks()
        width, height = 600, 380
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    # =========================================
    # FADE-IN TITLE + SUBTITLE
    # =========================================

    def fade_in(self):
        self.fade_step += 1
        ratio = min(self.fade_step / 20, 1.0)

        # interpolate from bg color (#10141f) to white for title
        shade = int(0x10 + ratio * (0xFF - 0x10))
        hex_shade = f"{shade:02x}"
        color = f"#{hex_shade}{hex_shade}{hex_shade}"
        self.title.configure(text_color=color)

        # subtitle fades to gray80
        shade2 = int(0x10 + ratio * (0xCC - 0x10))
        hex_shade2 = f"{shade2:02x}"
        color2 = f"#{hex_shade2}{hex_shade2}{hex_shade2}"
        self.subtitle.configure(text_color=color2)

        if self.fade_step < 20:
            self.root.after(20, self.fade_in)

    # =========================================
    # ANIMATED "..." DOTS ON STATUS TEXT
    # =========================================

    def animated_dots(self, base_text):
        self.dot_count = (self.dot_count + 1) % 4
        return base_text + "." * self.dot_count

    # =========================================
    # MAIN PROGRESS ANIMATION (with easing)
    # =========================================

    def animate(self):
        self.step += 1

        # ease-out curve so it feels smoother than linear
        linear = self.step / 100
        eased = 1 - (1 - linear) ** 2
        self.progress.set(eased)

        if self.step < 25:
            base = "Initializing AI Activity Tracker"
        elif self.step < 50:
            base = "Connecting to activity database"
        elif self.step < 75:
            base = "Loading analytics engine"
        elif self.step < 95:
            base = "Preparing dashboard"
        else:
            base = "Starting application"

        self.status.configure(text=self.animated_dots(base))

        if self.step >= 100:
            self.after_id = None
            self.finish()
            return

        self.after_id = self.root.after(22, self.animate)

    # =========================================
    # FINISH — destroy ONLY the splash frame,
    # keep the root window alive for the dashboard
    # =========================================

    def finish(self):
        # cancel any pending scheduled callback just in case
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.frame.destroy()
        self.on_complete()