#!/usr/bin/env python3
"""
Test script for the calculator logic without GUI display.
"""

class MockCalculator:
    """Mock calculator for testing logic without GUI."""
    
    def __init__(self):
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.should_reset = False
    
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
    
    def operation_clicked(self, op):
        """Handle operation button clicks."""
        if self.operator and not self.should_reset:
            self.equals_clicked()
        
        self.previous = self.current
        self.operator = op
        self.should_reset = True
    
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
                        raise ValueError("Cannot divide by zero!")
                    result = float(self.previous) / float(self.current)
                
                # Format result to avoid unnecessary decimal places
                if result == int(result):
                    self.current = str(int(result))
                else:
                    self.current = f"{result:.10g}"
                
                self.operator = ""
                self.previous = ""
                self.should_reset = True
                
            except Exception as e:
                print(f"Error: {e}")
                self.clear_all()
    
    def clear_all(self):
        """Clear everything."""
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.should_reset = False


def test_calculator():
    """Test basic calculator operations."""
    print("Testing Calculator Logic...")
    
    calc = MockCalculator()
    
    # Test 1: Basic addition (5 + 3 = 8)
    calc.number_clicked('5')
    calc.operation_clicked('+')
    calc.number_clicked('3')
    calc.equals_clicked()
    assert calc.current == "8", f"Expected 8, got {calc.current}"
    print("✓ Addition test passed: 5 + 3 = 8")
    
    # Test 2: Basic subtraction (10 - 4 = 6)
    calc.clear_all()
    calc.number_clicked('1')
    calc.number_clicked('0')
    calc.operation_clicked('-')
    calc.number_clicked('4')
    calc.equals_clicked()
    assert calc.current == "6", f"Expected 6, got {calc.current}"
    print("✓ Subtraction test passed: 10 - 4 = 6")
    
    # Test 3: Basic multiplication (7 * 8 = 56)
    calc.clear_all()
    calc.number_clicked('7')
    calc.operation_clicked('*')
    calc.number_clicked('8')
    calc.equals_clicked()
    assert calc.current == "56", f"Expected 56, got {calc.current}"
    print("✓ Multiplication test passed: 7 * 8 = 56")
    
    # Test 4: Basic division (15 / 3 = 5)
    calc.clear_all()
    calc.number_clicked('1')
    calc.number_clicked('5')
    calc.operation_clicked('/')
    calc.number_clicked('3')
    calc.equals_clicked()
    assert calc.current == "5", f"Expected 5, got {calc.current}"
    print("✓ Division test passed: 15 / 3 = 5")
    
    # Test 5: Decimal operations (2.5 + 1.5 = 4)
    calc.clear_all()
    calc.number_clicked('2')
    calc.number_clicked('.')
    calc.number_clicked('5')
    calc.operation_clicked('+')
    calc.number_clicked('1')
    calc.number_clicked('.')
    calc.number_clicked('5')
    calc.equals_clicked()
    assert calc.current == "4", f"Expected 4, got {calc.current}"
    print("✓ Decimal test passed: 2.5 + 1.5 = 4")
    
    print("\nAll calculator logic tests passed! ✓")


if __name__ == "__main__":
    test_calculator()