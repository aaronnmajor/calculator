#!/usr/bin/env python3
"""
Simple launcher script for the GUI Calculator.
This provides an alternative way to run the calculator.
"""

from calculator import main

if __name__ == "__main__":
    print("Starting GUI Calculator...")
    try:
        main()
    except KeyboardInterrupt:
        print("\nCalculator closed by user.")
    except Exception as e:
        print(f"Error starting calculator: {e}")
        print("Make sure tkinter is installed on your system.")
        print("On Ubuntu/Debian: sudo apt-get install python3-tk")