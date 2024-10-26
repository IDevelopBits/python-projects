import tkinter as tk
from tkinter import messagebox

def create_gui():
    global aEntry,bEntry, cEntry, root
    global equationLabel, xLabel, factorLabel

# Create the main window
    root = tk.Tk()
    root.title("Simple GUI")
    root.geometry("400x300")

    # The inputs
    aLabel = tk.Label(root, text="Enter ax^2:")
    aLabel.grid(row=0, column=0, padx=10, pady=10, )
    aEntry = tk.Entry(root)
    aEntry.grid(row=0, column=1, padx=10, pady=10)

    bLabel = tk.Label(root, text="Enter bx:")
    bLabel.grid(row=1, column=0, padx=10, pady=10)
    bEntry = tk.Entry(root)
    bEntry.grid(row=1, column=1, padx=10, pady=10)

    cLabel = tk.Label(root, text="Enter c:")
    cLabel.grid(row=2, column=0, padx=10, pady=10)
    cEntry = tk.Entry(root)
    cEntry.grid(row=2, column=1, padx=10, pady=10)

    # The output
    calcButton = tk.Button(root, text="Calculate", command=calculate)
    calcButton.grid(row=3, column=1, padx=10, pady=10)

    equationLabel = tk.Label(root, justify="center")
    equationLabel.grid(row=4, column=1, padx=10, pady=10)

    xLabel = tk.Label(root, text="ax^2 + bx + c = 0", justify="center")
    xLabel.grid(row=5, column=1, padx=10, pady=10)
        
    factorLabel = tk.Label(root, text="", justify="center")
    factorLabel.grid(row=6, column=1, padx=10, pady=10)



    # Run the application
    root.mainloop()

def calculate():
    # Loops while a, b, or c is a non-integer
    try:
        a = aEntry.get()
        b = bEntry.get()
        c = cEntry.get()

        a = int(a)
        b = int(b)
        c = int(c)

        messagebox.showwarning("Non-exact values", "Warning: these values may not be exact.")

        equationLabel.configure(text=f"{a}x^2 + {b}x + {c} = 0")

        # calculates the zero using the quadratic formula
        x1 = (-b + (((b**2) - 4*a*c))**(1/2)) / (2 * a)
        x2 = (-b - (((b**2) - 4*a*c))**(1/2)) / (2 * a)
        
        xLabel.configure(text=f"x = {x1}, {x2}".replace("j", "i"), wraplength=200)
        
        factorLabel.configure(text=f"In factored form: (x{x1:+g})*(x{x2:+g})".replace("j", "i"))
    except ValueError:
        messagebox.showerror("Invalid value", "One or more values were not entered correctly. Please enter integers for 'a', 'b' and 'c'.")
    
create_gui()



print()
print(f"{a}x^2 + {b}x + {c} = 0") 
print()

# calculates the zero using the quadratic formula
x1 = (-b + (((b**2) - 4*a*c))**(1/2)) / (2 * a)
x2 = (-b - (((b**2) - 4*a*c))**(1/2)) / (2 * a)

print("x1:", x1)
print("x2:", x2)

print("Warning: these values may not be exact.")
print()

print(f"In factored form: (x{x1:+g})*(x{x2:+g})".replace("j", "i"))





