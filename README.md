# predykcja API (Flask + Docker)

aplikacja API, która przyjmuje dwie liczby `x` i `y`, sumuje je, i na podstawie prostej reguły zwraca predykcję:

- Jeśli `x + y > 5.8` → predykcja = 1
- W przeciwnym razie → predykcja = 0

---

## Endpoint

http://localhost:5000/api/v1.0/predict?x=3&y=3
