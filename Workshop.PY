from tkinter import *
from datetime import date
 
window = Tk()
window.title("Workshop Participant Greeting")
window.geometry("400x300")
 
title_label = Label(
    text="Workshop Welcome Desk",
    fg="white",
    bg="#072F5F",
    height=1,
    width=300
)
 
name_label = Label(
    text="Participant Name",
    bg="#3895D3"
)
name_entry = Entry()
 
def display_welcome():
    attendee_name = name_entry.get()
 
    output_area.delete(1.0, END)
 
    greeting = "Hello " + attendee_name + "!\n"
    message = "Welcome to the workshop.\n"
    workshop_date = "Date: " + str(date.today())
 
    output_area.insert(END, greeting)
    output_area.insert(END, message)
    output_area.insert(END, workshop_date)
 
output_area = Text(
    height=4,
    width=40
)
 
submit_btn = Button(
    text="Check In",
    command=display_welcome,
    height=1,
    bg="#1261A0",
    fg="white"
)
 
title_label.pack()
name_label.pack(pady=10)
name_entry.pack()
submit_btn.pack(pady=10)
output_area.pack()
 
window.mainloop()
