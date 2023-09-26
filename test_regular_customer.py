import pytest
from employee import Employee
from regular_customer import RegularCustomer

class TestRegularCustomer:

    @pytest.fixture
    def employee(self):
        return Employee('Robin', 50, '155-44', '011 111 11 11')

    @pytest.fixture
    def customer(self, employee):
        return RegularCustomer('Carla', 30, employee)

    def test_regular_customer_initialisation(self, customer, employee):
        assert customer.name == 'Carla'
        assert customer.age == 30
        assert customer.client_advisor == employee

    def test_get_set_discount(self, customer):
        customer.discount = 3.3
        assert customer.discount == 3.3

    def test_regular_customer_print(self, customer, capsys):
        customer.address = 'Neustadt'
        customer.discount = 5.1
        customer.print()
        captured = capsys.readouterr()
        assert captured.out == 'Person: Carla\n\tAlter: 30\n\tAdresse: Neustadt\n\t\tKundenberater: Robin\t011 111 11 11\n\t\tStammkunde mit 5.1% Rabatt\n'

