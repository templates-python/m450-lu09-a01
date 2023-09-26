import pytest

from person import Person

class TestPerson:

    @pytest.fixture
    def person(self):
        return Person('Max', 33)


    def test_person_initialisation(self, person):
        assert person.name == 'Max'
        assert person.age == 33

    def test_set_get_address(self, person):
        person.address = 'Dorf'
        assert person.address == 'Dorf'

    def test_person_print(self, person, capsys):
        person.address = 'Testadresse'
        person.print()
        captured = capsys.readouterr()
        assert captured.out == 'Person: Max\n\tAlter: 33\n\tAdresse: Testadresse\n'

