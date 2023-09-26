from customer import Customer
from employee import Employee

class RegularCustomer(Customer):
   '''
    Beschreibt einen Stammkunden mit seinem Kundenkontakt und dem Rabatt, den er bekommt.
    Dazu muss bei der Erzeugung des Objekts die Referenz auf ein Mitarbeiter-Objekt geliefert werden.

    Die Attribute sind über getter/setter zugreifbar.
    Für die Ausgabe am Stdout wird die Methode print() verwendet. Dabei wird aber immer auch
    die Ausgabe der Oberklasse Customer ausgeführt.
   '''

   def __init__(self, name, age, client_advisor):
      '''
      Initlaisiert ein Kunden-Objekt mit einer einseitigen Beziehung zu Mitarbeiter
      :param name: Name des Kunden
      :param age: Alter des Kunden
      :param client_advisor: Referenz zum Kundenbetreuer
      '''
      super().__init__(name, age, client_advisor)

   @property
   def discount(self):
      '''
      Liefert den Rabatt des Stammkunden
      :return: Rabatt des Stammkunden
      '''
      return self._discount

   @discount.setter
   def discount(self, discount):
      '''
      Legt den rabatt des Stammkunden fest.
      :param discount: Rabatt des Stammkunden
      '''
      self._discount = discount


   def print(self):
      '''
      Gibt alle Information einer Mitarbeiterin am Stdout aus.
      Dazu muss die entsprechende Methode der Oberklasse auch aufgerufen werden.
      '''
      super().print()
      print(f'\t\tStammkunde mit {self._discount}% Rabatt')


#Test
if __name__ == '__main__':
   e = Employee('Max', 2000, '455.45.T', '099-345-332-123')
   r = RegularCustomer('Pia', 1980, e)
   r.address  = 'Oberdorf'
   r.discount = 2.4
   r.print()