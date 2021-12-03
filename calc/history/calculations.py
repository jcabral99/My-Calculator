"""Calculation history Class"""
class Calculations:
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        Calculations.history.clear()
        return True
    @staticmethod
    def get_last_calculation():
        return Calculations.history[-1]
