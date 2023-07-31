import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.year_var = 2023
        self.month_var = 11
        self.day_var = 25
        self.hour_var = 7
        self.minute_var = 0
        self.second_var = 0

        self.timer_label = tk.Label(root, text="", font=("Helvetica", 30))
        self.timer_label.grid(row=7, column=0, columnspan=2)

        self.target_time = datetime(year=self.year_var, month=self.month_var, day=self.day_var,
                                    hour=self.hour_var, minute=self.minute_var, second=self.second_var)
        self.update_timer()


    def update_timer(self):
        now = datetime.now()
        if now < self.target_time:
            time_left = self.target_time - now
            self.timer_label.config(text=self.format_time(time_left))
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Chegou a hora!")
            messagebox.showinfo("Timer", "Acabou o tempo!")

    def format_time(self, td):
        days, hours, minutes, seconds = td.days, td.seconds // 3600, td.seconds // 60 % 60, td.seconds % 60
        return f"{days} dias, {hours} horas, {minutes} minutos, {seconds} segundos"


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tempo para o vestibular")
    app = TimerApp(root)
    root.mainloop()
