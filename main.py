from person import Person
from employee import Employee
from customer import Customer
from regular_customer import RegularCustomer

if __name__ == "__main__":
    # eine allgemeine Person erstellen
    p = Person("Max", 25)
    p.adress = "Musterdorf"
    p.print()
    print("--------------------------------------------")
    # Einen Mitarbeiter erstellen
    e = Employee("Joel", 35, "723-123", "01 03 04 05")
    e.adress = "Weltdorf"
    e.salary = 6000.00
    e.print()
    print("--------------------------------------------")
    # einen Kunden erstellen
    c = Customer("Moritz", 45, e)
    c.adress = "Oberdorf"
    c.print()
    print("--------------------------------------------")
    # eine Stammkundin erstellen
    r = RegularCustomer("Pia", 25, e)
    r.adress = "Oberdorf"
    r.discount = 2.4
    r.print()
    print("--------------------------------------------")