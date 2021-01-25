import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 5, 5) == 25
    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 5, 5) == 10

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 5, 5) == 1
    def test_division_calculation_failed(self):
        assert self.calc.division(self, 5, 5) == 0

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 5, 5) == 0
    def test_subtraction_calculation_failed(self):
        assert self.calc.subtraction(self, 5, 5) == 1

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 5) == 10
    def test_adding_calculation_failed(self):
        assert self.calc.adding(self, 5, 5) == 25