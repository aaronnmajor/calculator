#!/usr/bin/env python3
"""
GUI Calculator Application using tkinter
A simple calculator with basic arithmetic operations.
"""

import tkinter as tk
from tkinter import messagebox
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Variables to store the current calculation
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.should_reset = False
        
        # Create the display
        self.create_display()
        
        # Create the buttons
        self.create_buttons()
    
    def create_display(self):
        """Create the calculator display."""
        display_frame = tk.Frame(self.root, bg="black")
        display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))
        
        # Main display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 24, "bold"),
            bg="black",
            fg="white",
            anchor="e",
            padx=10,
            pady=10
        )
        self.display.pack(fill=tk.BOTH, expand=True)
        
        # Secondary display for showing the operation
        self.operation_var = tk.StringVar()
        self.operation_var.set("")
        
        self.operation_display = tk.Label(
            display_frame,
            textvariable=self.operation_var,
            font=("Arial", 12),
            bg="black",
            fg="gray",
            anchor="e",
            padx=10
        )
        self.operation_display.pack(fill=tk.X)
    
    def create_buttons(self):
        """Create all calculator buttons."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Button configuration
        button_config = {
            "font": ("Arial", 14, "bold"),
            "width": 8,
            "height": 2
        }
        
        # Row 1: Clear and operations
        tk.Button(
            button_frame, text="C", bg="#ff4444", fg="white",
            command=self.clear_all, **button_config
        ).grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="CE", bg="#ff6666", fg="white",
            command=self.clear_entry, **button_config
        ).grid(row=0, column=1, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="⌫", bg="#ff6666", fg="white",
            command=self.backspace, **button_config
        ).grid(row=0, column=2, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="÷", bg="#4444ff", fg="white",
            command=lambda: self.operation_clicked("/"), **button_config
        ).grid(row=0, column=3, padx=2, pady=2, sticky="nsew")
        
        # Row 2: Numbers 7, 8, 9 and multiply
        tk.Button(
            button_frame, text="7", bg="#666666", fg="white",
            command=lambda: self.number_clicked("7"), **button_config
        ).grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="8", bg="#666666", fg="white",
            command=lambda: self.number_clicked("8"), **button_config
        ).grid(row=1, column=1, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="9", bg="#666666", fg="white",
            command=lambda: self.number_clicked("9"), **button_config
        ).grid(row=1, column=2, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="×", bg="#4444ff", fg="white",
            command=lambda: self.operation_clicked("*"), **button_config
        ).grid(row=1, column=3, padx=2, pady=2, sticky="nsew")
        
        # Row 3: Numbers 4, 5, 6 and subtract
        tk.Button(
            button_frame, text="4", bg="#666666", fg="white",
            command=lambda: self.number_clicked("4"), **button_config
        ).grid(row=2, column=0, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="5", bg="#666666", fg="white",
            command=lambda: self.number_clicked("5"), **button_config
        ).grid(row=2, column=1, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="6", bg="#666666", fg="white",
            command=lambda: self.number_clicked("6"), **button_config
        ).grid(row=2, column=2, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="−", bg="#4444ff", fg="white",
            command=lambda: self.operation_clicked("-"), **button_config
        ).grid(row=2, column=3, padx=2, pady=2, sticky="nsew")
        
        # Row 4: Numbers 1, 2, 3 and add
        tk.Button(
            button_frame, text="1", bg="#666666", fg="white",
            command=lambda: self.number_clicked("1"), **button_config
        ).grid(row=3, column=0, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="2", bg="#666666", fg="white",
            command=lambda: self.number_clicked("2"), **button_config
        ).grid(row=3, column=1, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="3", bg="#666666", fg="white",
            command=lambda: self.number_clicked("3"), **button_config
        ).grid(row=3, column=2, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="+", bg="#4444ff", fg="white",
            command=lambda: self.operation_clicked("+"), **button_config
        ).grid(row=3, column=3, padx=2, pady=2, sticky="nsew")
        
        # Row 5: 0, decimal point and equals
        tk.Button(
            button_frame, text="0", bg="#666666", fg="white",
            command=lambda: self.number_clicked("0"), **button_config
        ).grid(row=4, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text=".", bg="#666666", fg="white",
            command=self.decimal_clicked, **button_config
        ).grid(row=4, column=2, padx=2, pady=2, sticky="nsew")
        
        tk.Button(
            button_frame, text="=", bg="#44aa44", fg="white",
            command=self.equals_clicked, **button_config
        ).grid(row=4, column=3, padx=2, pady=2, sticky="nsew")
        
        # Configure grid weights for responsive layout
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def number_clicked(self, number):
        """Handle number button clicks."""
        if self.should_reset:
            self.current = number
            self.should_reset = False
        else:
            if self.current == "0":
                self.current = number
            else:
                self.current += number
        
        self.display_var.set(self.current)
    
    def decimal_clicked(self):
        """Handle decimal point button click."""
        if self.should_reset:
            self.current = "0."
            self.should_reset = False
        elif "." not in self.current:
            self.current += "."
        
        self.display_var.set(self.current)
    
    def operation_clicked(self, op):
        """Handle operation button clicks."""
        if self.operator and not self.should_reset:
            self.equals_clicked()
        
        self.previous = self.current
        self.operator = op
        self.should_reset = True
        
        # Update operation display
        op_symbol = op
        if op == "*":
            op_symbol = "×"
        elif op == "/":
            op_symbol = "÷"
        elif op == "-":
            op_symbol = "−"
        
        self.operation_var.set(f"{self.previous} {op_symbol}")
    
    def equals_clicked(self):
        """Handle equals button click."""
        if self.operator and self.previous:
            try:
                if self.operator == "+":
                    result = float(self.previous) + float(self.current)
                elif self.operator == "-":
                    result = float(self.previous) - float(self.current)
                elif self.operator == "*":
                    result = float(self.previous) * float(self.current)
                elif self.operator == "/":
                    if float(self.current) == 0:
                        messagebox.showerror("Error", "Cannot divide by zero!")
                        return
                    result = float(self.previous) / float(self.current)
                
                # Format result to avoid unnecessary decimal places
                if result == int(result):
                    self.current = str(int(result))
                else:
                    self.current = f"{result:.10g}"  # Use general format to avoid scientific notation for most numbers
                
                self.display_var.set(self.current)
                self.operation_var.set("")
                
                self.operator = ""
                self.previous = ""
                self.should_reset = True
                
            except Exception as e:
                messagebox.showerror("Error", f"Calculation error: {str(e)}")
                self.clear_all()
    
    def clear_all(self):
        """Clear everything."""
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.should_reset = False
        self.display_var.set("0")
        self.operation_var.set("")
    
    def clear_entry(self):
        """Clear current entry."""
        self.current = "0"
        self.display_var.set("0")
    
    def backspace(self):
        """Remove last digit."""
        if len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"
        self.display_var.set(self.current)


def main():
    """Main function to run the calculator."""
    root = tk.Tk()
    calculator = Calculator(root)
    
    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", root.quit)
    
    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()