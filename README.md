# Podstawy Sztucznej Inteligencji - Projekt - Porównanie algortymów przeszukiwania BFS, DFS, IDFS dla problemu znalezienia drogi w wygenerowanym labiryncie.
Projekt wykonany w ramach przedmiotu PSZT (Podstawy Sztucznej Inteligencji) w semestrze 2020Z (5 semestr), na kierunku Informatyka, specjalizacji Inżynieria Systemów Informacyjnych (ISI) na Wydziale Elektroniki i Technik Informacyjnych (EiTI) Politechniki Warszawskiej.

**Prowadzący projekt**: mgr inż. Mikołaj Markiewicz
**Ocena**: 15/15

### Autorzy
Lukasz Pokorzyński, nr 300251  
l.pokorzynski@stud.elka.pw.edu.pl  
Adam Steciuk, nr 300263  
adam.steciuk.stud@pw.edu.pl  

### Treść zadania
Napisać program porównujący działanie algorytmów przeszukiwania BFS, DFS, IDFS dla problemu znalezienia drogi w labiryncie. Przestrzeń dyskretna - dozwolone ruchy to góra, dół, lewo, prawo. WE: plik ze strukturą labiryntu z we/wy (dla większych użyć jakiegoś generatora).
WY: znaleziona najkrótsza ścieżka i/lub mapka z zaznaczoną ścieżką

_(Reszta dostępna w [dokumentacji końcowej](https://github.com/steciuk/PSZT-maze-solver/blob/ff1782ac67b73ef74e92caec9bc91a0377cb44d2/PSZT%20-%20Labirynt.pdf))_

### Instrukcja
- Uruchamiamy ``main.py``
- Opcję w menu wybieramy wpisując odpowiednią wartość porządkową (1, 2, 3, 4 lub h) i zatwierdzając klawiszem Enter.
- Po wybraniu opcji dokonywane są następujące czynności:
  - ``(1)`` Generacja labiryntu - buduje labirynt z pliku tekstowego lub pobiera od użytkownika parametry do jego utworzenia (x, y, seed, czy ma mieć tylko jedną ścieżkę)
  - ``(2)`` Szukanie rozwiązania - jeżeli labirynt został już stworzony, szuka rozwiązań oraz wyświetla czas wykonywania i liczbę kroków (przeszukanych węzłów grafu) dla algorytmu. Jeżeli szukanie ścieżki następuje po losowaniu startu i celu, wtedy program pyta ile takich losowych przeszukań ma przeprowadzić i wyświetla dodatkowo średnią z czasów wykonywania.
  - ``(3)`` Zapis do pliku .txt - zapisuje labirynt do pliku tekstowego jako mapa numeryczna z wartościami 0-3
  - ``(4)`` Wyjście - wyłącza działanie programu
  - ``(h)`` Pomoc - wyświetla opis opcji ”w pigułce”

