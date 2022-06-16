from cgitb import text
from tkinter import *


window = Tk()
window.title('Miles to Km convertor')
window.minsize(width=220, height=120)
window.config(padx=20, pady=20)

#functions
def miles_to_km():
    miles = float(miles_entry.get())
    km = miles * 1.609
    km_value_label.config(text=km)

#labels
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

km_value_label = Label(text='0')
km_value_label.grid(column=1,row=1)

#entries
miles_entry = Entry(width=5)
miles_entry.grid(column=1, row=0)


#buttons
calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1,row=2)












window.mainloop()