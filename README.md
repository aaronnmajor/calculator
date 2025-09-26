# Calculator

A simple GUI calculator application built with Python and tkinter.

## Features

- Basic arithmetic operations: addition (+), subtraction (−), multiplication (×), and division (÷)
- Decimal number support
- Clear all (C) and clear entry (CE) functions
- Backspace functionality (⌫)
- Error handling for division by zero
- Clean, user-friendly interface with a dark theme

## Requirements

- Python 3.x
- tkinter (usually included with Python, but may need separate installation on some Linux distributions)

### Installing tkinter (if needed)

- **Ubuntu/Debian**: `sudo apt-get install python3-tk`
- **CentOS/RHEL**: `sudo yum install tkinter` 
- **macOS**: Included with Python
- **Windows**: Included with Python

## Usage

### Running the Calculator

```bash
python3 calculator.py
```

### Using the Calculator

1. **Numbers**: Click the number buttons (0-9) to enter numbers
2. **Decimal Point**: Click the "." button to add decimal points
3. **Operations**: Click +, −, ×, or ÷ to perform operations
4. **Equals**: Click "=" to calculate the result
5. **Clear All**: Click "C" to clear everything
6. **Clear Entry**: Click "CE" to clear only the current entry
7. **Backspace**: Click "⌫" to delete the last entered digit

### Example Calculations

- **Addition**: `5 + 3 = 8`
- **Subtraction**: `10 − 4 = 6`
- **Multiplication**: `7 × 8 = 56`
- **Division**: `15 ÷ 3 = 5`
- **Decimals**: `2.5 + 1.5 = 4`

## Testing

Run the test suite to verify the calculator logic:

```bash
python3 test_calculator.py
```

## File Structure

```
calculator/
├── calculator.py          # Main calculator application
├── test_calculator.py     # Test suite for calculator logic
├── requirements.txt       # Project dependencies and installation notes
└── README.md             # This file
```

## Development

The calculator is built using Python's built-in tkinter library for the GUI. The main `Calculator` class handles:

- GUI layout and styling
- Button click events
- Arithmetic calculations
- Error handling
- Display updates

## License

This project is open source and available under the MIT License.