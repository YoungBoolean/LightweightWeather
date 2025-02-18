import tkinter as tk
import image_selection
from datetime import datetime
from web_api import Weather, MyIpInfo
from hourly_statistics import Diagrams


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ip = MyIpInfo
        self.weather = Weather
        self.ip.get_data()
        self.weather.get_data()
        self.geometry("500x245")
        self.title("Lightweight Weather")
        self.resizable(width=False, height=False)
        self.day_time = None
        self.weather_image = None
        self.time_lbl = None
        self.ui_element1 = None
        self.temperature_lbl = None
        self.weather_name_lbl = None
        self.wind_speed_lbl = None
        self.precipitation_lbl = None
        self.humidity_lbl = None
        self.status_lbl = None
        self.city_lbl = None
        self.create_menu()
        self.l_frame = tk.Frame(self)
        self.r_frame = tk.Frame(self)
        self.create_widgets()
        self.run_managers()

    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M")
        self.time_lbl.config(text=current_time)
        self.after(1000, self.update_clock)

    def set_day_or_night(self):
        current_time = int(self.time_lbl.cget("text")[:2])
        if current_time >= 6 and current_time < 21:
            self.day_time = True
        else:
            self.day_time = False

    def show_about(self):
        about_window = tk.Toplevel()
        about_window.title("About")
        about_window.geometry("200x100")
        about_text = "Lightweight Weather\n\nDeveloped by Paulius Uvarovas\n"
        lbl_info = tk.Label(about_window, text=about_text)
        lbl_info.pack()
        ok_btn = tk.Button(about_window, text="Close", command=about_window.destroy)
        ok_btn.pack()

    def show_statistics(self):
        Diagrams.get_lineplot()

    def reset_ip(self):
        self.ip.get_data()
        self.weather.get_data()
        self.create_widgets()
        self.run_managers()

    def change_theme(self):
        current_bg = self.cget("bg")
        if current_bg == "gray25":
            self.configure(bg="gray94")
            self.l_frame.configure(bg="gray94")
            self.r_frame.configure(bg="gray94")
            self.weather_image.configure(bg="gray94")
            self.ui_element1.configure(bg="gray94")
        else:
            self.configure(bg="gray25")
            self.l_frame.configure(bg="gray25")
            self.r_frame.configure(bg="gray25")
            self.weather_image.configure(bg="gray25")
            self.ui_element1.configure(bg="gray25")

    def create_menu(self):
        main_menu = tk.Menu(self)
        self.config(menu=main_menu)
        sub_menu_help = tk.Menu(main_menu, tearoff=0)
        sub_menu_help.add_command(label="About", command=self.show_about)
        sub_menu_settings = tk.Menu(main_menu, tearoff=0)
        sub_menu_settings.add_command(label="Dark/Light theme", command=self.change_theme)
        sub_menu_settings.add_command(label="Hourly Weather Statistics", command=self.show_statistics)
        sub_menu_settings.add_command(label="Reset IP", command=self.reset_ip)
        main_menu.add_cascade(label="Settings", menu=sub_menu_settings)
        main_menu.add_cascade(label="Help", menu=sub_menu_help)

    def check_connection_status(self):
        if self.weather.connected and self.ip.connected:
            self.status_lbl.config(text="Connected")
            self.after(10000, self.hide_status_label)
        else:
            self.status_lbl.config(text="Could not connect to server")

    def hide_status_label(self):
        self.status_lbl.pack_forget()

    def esc(self):
        exit()

    def create_widgets(self):
        self.time_lbl = tk.Label(self, text="", font=("Helvetica", 24), relief=tk.SOLID, borderwidth=2, width=5)
        self.update_clock()
        self.set_day_or_night()
        if self.day_time:
            img = tk.PhotoImage(file=image_selection.weather_status[self.weather.weather_code])
        else:
            img = tk.PhotoImage(file=image_selection.weather_status_night[self.weather.weather_code])
        self.weather_image = tk.Label(self.l_frame, image=img)
        self.weather_image.img = img  # <-- solution for bug with images & garbage collection !!!!!!!
        img2 = tk.PhotoImage(file=f"{image_selection.ui_images_dir}/ui_element1.png")
        self.ui_element1 = tk.Label(self.r_frame, image=img2, width=300)
        self.ui_element1.img = img2
        self.city_lbl = tk.Label(self, text=self.ip.city, font=("Helvetica", 30),
                                 relief=tk.SOLID, borderwidth=2, width=5)
        self.temperature_lbl = tk.Label(self, text=self.weather.temperature, font=("Helvetica", 16))
        self.weather_name_lbl = tk.Label(self, text=f"\"{self.weather.weather_name}\"", font=("Helvetica", 10))
        self.wind_speed_lbl = tk.Label(self, text=self.weather.wind_speed, font=("Helvetica", 16))
        self.precipitation_lbl = tk.Label(self, text=self.weather.precipitation, font=("Helvetica", 16))
        self.humidity_lbl = tk.Label(self, text=self.weather.humidity, font=("Helvetica", 16))
        self.status_lbl = tk.Label(self,
                                   text="",
                                   bd=1,
                                   relief=tk.SUNKEN
                                   )
        self.bind("<Escape>", lambda event: self.esc())
        if not self.day_time:
            self.change_theme()

    def run_managers(self):
        self.status_lbl.pack(side=tk.BOTTOM, fill=tk.X)
        self.check_connection_status()
        self.weather_image.grid(row=0, column=0)
        self.ui_element1.grid(row=0, column=0)
        self.time_lbl.place(x=55, y=185)
        self.temperature_lbl.place(x=120, y=100)
        self.wind_speed_lbl.place(x=275, y=50)
        self.precipitation_lbl.place(x=275, y=85)
        self.humidity_lbl.place(x=275, y=120)
        self.weather_name_lbl.place(x=240, y=0)
        self.city_lbl.place(x=290, y=173)
        self.l_frame.pack(side=tk.LEFT, anchor=tk.N)
        self.r_frame.pack(side=tk.RIGHT, expand=False, anchor=tk.N)


if __name__ == "__main__":
    win = App()
    win.mainloop()
