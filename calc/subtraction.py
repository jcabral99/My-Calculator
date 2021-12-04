"""this is the addition calculation that is being inherits the value A and value B from the calculation class"""

from calc.calculation import Calculation

class Subtraction(Calculation):
    """The addition class has one method to get the result of the calculation A and B come from
    the calulation parent"""
    def getresult(self):
        return self.value_a - self.value_b
