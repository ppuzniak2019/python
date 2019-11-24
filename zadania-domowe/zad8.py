#Za pomocą with open( ) proszę odczytać zawartość jednego pliku i zapisać w drugim. Proszę uwzględnić obsługę wyjątków.

#Najpierw tworzymy plik 1 i coś w nim zapisujemy:
plik_tekstowy = open('plik1.txt', 'w')
plik_tekstowy.write("Testujemy kopiowanie plików")
plik_tekstowy.close()

#Za pomocą with otwieramy pliki i przenosimy dane.
try:
    with open("plik1.txt") as p1:
        tekst = p1.readlines()
        with open("plik2.txt", "w") as p2:
            p2.writelines(tekst)
except (IOError) as e:
    print(e)


