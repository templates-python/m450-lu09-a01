# M450 LU09.A01 - Code mit Linter verbessern

Nutze ein Linter-Programm, um Schwächen im Sourcecode zu entdecken und zu
verbessern.

Wiki: <https://wiki.bzz.ch/modul/m450/learningunits/lu09/aufgaben/linter>

## Ausgangslage

Das Repository enthält eine kleine Klassenhierarchie (`Person`, `Employee`,
`Customer`, `RegularCustomer`) mit den passenden Unittests. Der Code
funktioniert, hält sich aber nicht überall an die
[Coding Standards](https://wiki.bzz.ch/howto/codingstandards/start).

## Auftrag

1. Wähle einen Linter aus und passe seine Konfiguration so an, dass sie
   möglichst genau den Coding Standards entspricht. Dokumentiere deine
   Einstellungen.
2. Analysiere den Sourcecode mit deinem Linter: Wie viele Fehler bzw. «code
   smells» wurden entdeckt? Welche Arten von Fehlern? Wie viele davon sind gar
   keine Fehler (false positive)?
3. Verbessere den Code anhand der Meldungen. Die Unittests müssen dabei
   weiterhin bestehen.
4. Tragt die Ergebnisse als Gruppe zusammen und ladet den Vergleich als PDF in
   Moodle hoch (siehe Wiki).

## Lokal testen

```bash
pip install -r requirements.txt
pytest
python _run_pylint.py
```

## Bewertung

| Teil | Punkte |
| --- | --- |
| Unittests (12 Testfälle, müssen nach dem Verbessern weiterhin bestehen) | 12 |
| Linting von `person.py`, `employee.py`, `customer.py`, `regular_customer.py`, `main.py` | 5 |
| **Total** | **17** |

Der Vergleich der Linter (PDF) wird in Moodle abgegeben und von Hand bewertet.

## Abgabe

Der Code wird durch den Push ins GitHub-Repository abgegeben. Jeder Push wird
automatisch bewertet.
