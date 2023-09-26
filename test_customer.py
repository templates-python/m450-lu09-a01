import pytest
from employee import Employee
from customer import Customer

class TestCustomer:

    @pytest.fixture
    def employee(self):
        return Employee('Robin', 50, '155-44', '011 111 11 11')

    @pytest.fixture
    def customer(self, employee):
        return Customer('Carla', 30, employee)

    def test_customer_initialisation(self, customer, employee):
        assert customer.name == 'Carla'
        assert customer.age == 30
        assert customer.client_advisor == employee

    def test_set_get_client_advisor(self, customer):
        customer.client_advisor = Employee('Ahmed', 40, '225.23', '+54 782 12 23 55 6')
        assert customer.client_advisor.name == 'Ahmed'

    def test_customer_print(self, customer, capsys):
        customer.address = 'Altstadt'
        customer.print()
        captured = capsys.readouterr()
        assert captured.out == 'Person: Carla\n\tAlter: 30\n\tAdresse: Altstadt\n\t\tKundenberater: Robin\t011 111 11 11\n'

