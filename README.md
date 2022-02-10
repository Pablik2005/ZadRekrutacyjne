Instrukcja
-Aplikacje startujemy z pliku run.py (niezbędny będzie pakiet flask)

-Listę dostępnych pól na które dana figura może się poruszyć w zalewności od aktualnej pozycji uzyskujemy przez wykonanie następującego zapytania 
http://localhost:5000/api/v1/figura/aktualna_pozycja
figura: [bishop, king, knight, pawn, queen, rook]
aktualna_pozycja: w zakresie od A do H i od 1 do 8 np. A1, B4 

-Informacje czy figura na danej pozycji może wykonać ruch na docelową uzyskujemy poprzez wykonanie następującego zapytania
http://localhost:5000/api/v1/figura/aktualna_pozycja/docelowa_pozycja
aktualna_pozycja: posiada taki sam zakres jak aktualna_pozycja
