from person import Person

class Employee(Person):
    '''
    Beschreibt eine Mitarbeiterin mit den für eine Firma typischen Merkmalen wie
    - Personal-Nummer
    - Lohn
    - Telefon-Nummer

    Die Attribute sind über getter/setter zugreifbar.
    Für die Ausgabe am Stdout wird die Methode print() verwendet. Dabei wird aber immer auch
    die Ausgabe der Oberklasse Person ausgeführt.
    '''

    def __init__(self, name, age, pers_nr, phone):
        '''
        Initlalisiert ein Mitarbeiter-Objekt.
        :param name: Name der Mitarbeiterin
        :param age: Alter der Mitarbeiterin
        :param pers_nr: Personal-Nummer der Mitarbeiterin
        :param phone: Telefon-Nummer der Mitarbeiterin
        '''
        super().__init__(name, age)
        self._pers_nr = pers_nr
        self._phone   = phone

    @property
    def pers_nr(self):
        '''
        Liefert die Personal-Nummer der Mitarbeiterin
        :return: Personal-Nummer der Mitarbeiterin
        '''
        return self._pers_nr

    @pers_nr. setter
    def pers_nr(self, pers_nr):
        '''
        Legt die Personalnummer der Mitarbeiterin fest.
        :param pers_nr: Personalnummer der Mitarbeiterin
        '''
        self._pers_nr = pers_nr

    @property
    def phone(self):
        '''
        Liefert die Telefon-Nummer der Mitarbeiterin
        :return: Telefo-Nummer der Mitarbeiterin
        '''
        return self._phone

    @phone.setter
    def phone(self, phone):
        '''
        Legt die Telefonnummer der Mitarbeiterin fest.
        :param phone: Telefonnummer der Mitarbeiterin
        '''
        self._phone = phone

    @property
    def salary(self):
        '''
        Liefert den Lohn der Mitarbeiterin
        :return: Lohn der Mitarbeiterin
        '''
        return self._salary

    @salary.setter
    def salary(self, salary):
        '''
        Legt den Lohn der Mitarbeiterin fest.
        :param salary: Lohn der Mitarbeiterin
        '''
        self._salary = salary

    def print(self):
        '''
        Gibt alle Information einer Mitarbeiterin am Stdout aus.
        Dazu muss die entsprechende Methode der Oberklasse auch aufgerufen werden.
        '''
        super().print()
        print(f'\t\tPersonalnummer: {self._pers_nr}\n\t\tTelefon: {self._phone}\n\t\tLohn: {self._salary}')

#Test
if __name__ == "__main__":
    m = Employee('Max', 2000, '723-123', '01 03 04 05')
    m.address = 'Weltdorf'
    m.salary = 6000.00
    m.print()