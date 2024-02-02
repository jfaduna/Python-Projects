from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=50)
window.config(padx=50, pady=20)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

km_result_label = Label()
km_result_label.grid(column=1, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km:.2f}")


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
