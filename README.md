# M450 LU09.A01 - Code mit Linter verbessern

Vergleichen Sie zu zweit die Linter **pylint** und **ruff**: konfigurieren,
Code analysieren, Meldungen beurteilen.

Wiki: <https://wiki.bzz.ch/modul/m450/learningunits/lu09/aufgaben/linter>

## Ausgangslage

Das Repository enthält eine kleine Klassenhierarchie (`Person`, `Employee`,
`Customer`, `RegularCustomer`) mit den passenden Unittests. Der Code
funktioniert, hält sich aber nicht überall an die
[BZZ Codingstandards](https://wiki.bzz.ch/howto/codingstandards/start).

## Auftrag

1. **Vorbereitung:** Person A arbeitet mit pylint, Person B mit ruff
   (Dreiergruppe: Person C mit flake8). Installieren Sie Ihren Linter:
   `pip install pylint` bzw. `pip install ruff`.
2. **Konfigurieren:** Erstellen Sie eine Konfigurationsdatei
   (`pyproject.toml`, `.pylintrc` oder `ruff.toml`), die möglichst genau den
   Codingstandards entspricht. Mindestens: Zeilen bis 120 Zeichen,
   Docstrings für Klassen und Methoden, `snake_case` bzw. `PascalCase`.
3. **Analysieren und beurteilen:** Wie viele Meldungen? Welche Arten? Welche
   sind *false positive*? Suchen Sie zwei Mängel, die Ihr Linter **nicht**
   meldet.
4. **Vergleichen:** Füllen Sie zu zweit die Vergleichstabelle im Wiki aus.
   Jede Person lädt sie als eine Seite PDF selbst in Moodle hoch.
5. **Wer fertig ist:** Korrigieren Sie alle echten Meldungen im Code. Die
   Unittests müssen weiterhin bestehen.

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
