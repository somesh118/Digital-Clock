import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

window = tk.Tk()
window.title("Digital Clock")

clock_label = tk.Label(window, font=("Bahnschrift Condensed", 120), fg="red")
clock_label.pack(pady=50)

update_time()

window.mainloop()