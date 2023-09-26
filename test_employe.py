import pytest
from employee import Employee

class TestEmployee:

    @pytest.fixture
    def employee(self):
        return Employee('Mia', 22, '722.56-8', '099 999 99 99')

    def test_employee_initialisation(self, employee):
        assert employee.name == 'Mia'
        assert employee.age == 22
        assert employee.pers_nr == '722.56-8'
        assert employee.phone == '099 999 99 99'

    def test_set_get_salary(self, employee):
        employee.salary = 2000
        assert employee.salary == 2000

    def test_employee_print(self, employee, capsys):
        employee.address = 'Musterdorf'
        employee.salary = 5000
        employee.print()
        captured = capsys.readouterr()
        assert captured.out == 'Person: Mia\n\tAlter: 22\n\tAdresse: Musterdorf\n\t\tPersonalnummer: 722.56-8\n\t\tTelefon: 099 999 99 99\n\t\tLohn: 5000\n'
