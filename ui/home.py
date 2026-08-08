import customtkinter as ctk
from activity_tracker import get_active_window_

class HomePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="#1f1f1f")  # Dark background color

        #  -------------Title ------------------

        title = ctk.CTkLabel(
            self,
            text="🏠 Home Dashboard",
            font=("Arial", 32, "bold")

        )
        title.pack(pady=40)

        # -----------------CARDS -------------------

        cards_frame = ctk.CTkFrame(self,fg_color="transparent")
        cards_frame.pack(pady=20)

        self.current_app = self.create_card(
            cards_frame,
            "Current Application",
            "Loading..."
        )

        self.current_app.grid(row=0, column=0, padx=20,)

         #website card  
        self.current_site = self.create_card(
            cards_frame,
            "Current Website",
            "Waiting..."
        )

        self.current_site.grid(row=0, column=1, padx=20, )

        # status card
        self.status = self.create_card(
            cards_frame,
            "Tracker Status",
            "Running "
        )
        self.status.grid(row=0, column=2, padx=20, )

        #Start updating current application and website
        self.update_current_app()

    def create_card(self, parent, title, value):

        frame = ctk.CTkFrame(
            parent,
            width=220,
            height=120,
            corner_radius=15, 
        ) 

        frame.grid_propagate(False)  # Prevent frame from resizing to fit its content   
    
        title_lable =  ctk.CTkLabel(
            frame,
            text=title,
            font=("Arial", 16, "bold")
        )
        title_lable.pack(pady=(15,5))  # Top padding of 20, bottom padding of 5   
    
        value_label = ctk.CTkLabel(
            frame,
            text=value,
            font=("Arial", 20)
        )
        value_label.pack()

        return value_label

    def update_current_app(self):

        # Get the current active window
        current_window = get_active_window_()

        # Update the label with the current window title
        if current_window:
             self.current_app.configure(
                 text=current_window
        )

        # Schedule the next update after 2 seconds (2000 milliseconds)
        self.after(2000, self.update_current_app)





         