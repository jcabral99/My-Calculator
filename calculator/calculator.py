"""This is the increment function"""

from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division
# from csvmanager.read import Read
# from csvmanager.Write import Write
# import pandas as pd

class Calculator:
    """This is the Calculator class"""
    history = []
    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        return Calculator.history[0].getresult()
    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True
    @staticmethod
    def history_count():
        return len(Calculator.history)
    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        if Calculator.history[-1] != "NaN":
            return Calculator.history[-1].get_result()
        return Calculator.history[-1]

    @staticmethod
    def addition(value_a, value_b):
        """adds number to result"""
        addition = Addition.create(value_a,value_b)
        Calculator.add_calculation_to_history(addition)
        # df = Read.DataFrameFromCSVFile()
        # dict = {'Value1': value_a, 'Value2': value_b, 'Results': addition.get_result()}
        # df2 = pd.DataFrame(dict)
        # df3 = pd.concat([df,df2], ignore_index=True)
        # Write.DataFrameFromCSVFile(df3)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def subtraction(value_a, value_b):
        """"subtract number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiplication(value_a, value_b):
        """multiply two numbers and store the result"""
        multiplication = Multiplication.create(value_a,value_b)
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def division(value_a,value_b):
        """divide two numbers and store the result"""
        if value_b != 0:
            division = Division.create(value_a,value_b)
            Calculator.add_calculation_to_history(division)
            return
        else:
            Calculator.history.append("NaN")
            return Calculator.get_result_of_last_calculation_added_to_history()
