"""Testing the Calculator"""
import pprint

from calculator.calculator import Calculator

def test_calculator_add():
    """testing the add function of the calculator"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1,2) == -1

def test_calculator_multiply():
    """test multiplication of two numbers"""
    assert Calculator.multiply_numbers(1,2) == 2