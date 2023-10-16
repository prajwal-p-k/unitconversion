import tkinter as tk
from tkinter import ttk, StringVar

def convert():
    value = float(entry.get())
    
    if dropdown_var.get() == "Centimeter to Feet":
        result.set(value * 0.0328084)
    elif dropdown_var.get() == "Feet to Inches":
        result.set(value * 12)
    elif dropdown_var.get() == "Sqft to Sqmtrs":
        result.set(value * 0.092903)
    elif dropdown_var.get() == "Sqft to Acres":
        result.set(value * 2.29568e-5)

app = tk.Tk()
app.title("Unit Conversion")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

dropdown_var = StringVar()
options = [
    "Centimeter to Feet",
    "Feet to Inches",
    "Sqft to Sqmtrs",
    "Sqft to Acres"
]
dropdown = ttk.Combobox(frame, textvariable=dropdown_var, values=options, state="readonly")
dropdown.grid(row=0, column=0, sticky=tk.W, pady=5)
dropdown_var.set(options[0])

entry_label = ttk.Label(frame, text="Enter Value:")
entry_label.grid(row=1, column=0, sticky=tk.W, pady=5)
entry = ttk.Entry(frame)
entry.grid(row=1, column=1, pady=5)

convert_button = ttk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=2, pady=5)

result_label = ttk.Label(frame, text="Result:")
result_label.grid(row=3, column=0, sticky=tk.W, pady=5)
result = StringVar()
result_entry = ttk.Entry(frame, textvariable=result, state="readonly")
result_entry.grid(row=3, column=1, pady=5)

app.mainloop()
