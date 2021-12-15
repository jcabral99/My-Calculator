from app.controllers.controller import ControllerBase
from calculator.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value_a'] == '' or request.form['value_b'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('You successfully calculated')

            # get the values out of the form
            value_a = request.form['value_a']
            value_b = request.form['value_b']
            operation = request.form['operation']
            # this will call the correct operation
            getattr(Calculator, operation)(int(value_a), int(value_b))
            result = str(Calculator.get_result_of_last_calculation_added_to_history())
            return render_template('result.html', value_a=value_a, value_b=value_b, operation=operation, result=result)
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator.html')