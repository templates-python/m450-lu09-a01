from person import Person
from employee import Employee

class Customer(Person):
    '''
    Beschreibt einen Kunden mit seinem Kundenkontakt.
    Dazu muss bei der Erzeugung des Objekts die Referenz auf ein Mitarbeiter-Objekt geliefert werden.

    Die Attribute sind über getter/setter zugreifbar.
    Für die Ausgabe am Stdout wird die Methode print() verwendet. Dabei wird aber immer auch
    die Ausgabe der Oberklasse Person ausgeführt.
    '''

    def __init__(self, name, age, client_advisor):
        '''
        Initlaisiert ein Kunden-Objekt mit einer einseitigen Beziehung zu Mitarbeiter
        :param name: Name des Kunden
        :param age: Alter des Kunden
        :param client_advisor: Referenz zum Kundenbetreuer
        '''
        super().__init__(name, age)
        self._client_advisor = client_advisor

    @property
    def client_advisor(self):
        '''
        Liefert die Referenz zum Kundenberater
        :return: Referenz des Kundenberaters
        '''
        return self._client_advisor

    @client_advisor.setter
    def client_advisor(self, client_advisor):
        '''
        Sett die Referenz zum Kundenberater
        :param client_advisor: Referenzauf Kundenberater
        '''
        self._client_advisor = client_advisor

    def print(self):
        '''
        Gibt alle Information einer Mitarbeiterin am Stdout aus.
        Dazu muss die entsprechende Methode der Oberklasse auch aufgerufen werden.
        '''
        super().print()
        print(f'\t\tKundenberater: {self._client_advisor.name}\t{self._client_advisor.phone}')

#Test
if __name__ == '__main__':
    e = Employee('Max', 44, '455.45.T', '099-345-332-123')
    c = Customer('Pia', 30, e)
    c.address = 'Oberdorf'
    c.print()
