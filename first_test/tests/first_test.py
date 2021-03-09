import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 0.1, 10) == 1
    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 0.1, 10) == 1.0

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 73, 20) == 3.65
    def test_division_calculation_failed(self):
        assert self.calc.division(self, 73, 20) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 2.6, 2) == 0.6
    def test_subtraction_calculation_failed(self):
        assert self.calc.subtraction(self, 2.6, 2) == 0.6000000000000001

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 0.2, 0.1) == 0.3
    def test_adding_calculation_failed(self):
        assert self.calc.adding(self, 0.2, 0.1) == 0.30000000000000004
