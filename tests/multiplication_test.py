"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (2.0,2.0)
    multiplication = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiplication.get_result() == 4.0
