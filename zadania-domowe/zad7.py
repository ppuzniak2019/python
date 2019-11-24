#Proszę otworzyć plik i zapisać do niego dowolne dane, a następnie bez zamykania go spróbować odczytać jego zawartość.

#Tworzenie pliku:
plik_tekstowy = open('plik.txt', 'w')
plik_tekstowy.write("Testuje pisanie plików!")
plik_tekstowy.close()

#Otwieranie pliku:
plik_tekstowy = open('plik.txt', 'r')
print(plik_tekstowy.read())
plik_tekstowy.close()

#Edytowanie i otwieranie bez zapisania:
plik_tekstowy = open('plik.txt', 'w')
plik_tekstowy.write("Testuje pisanie plików! I coś nowego dopisuje!")
'''
#print(plik_tekstowy.read()) # NIESTETY WYSKAKUJE BŁĄD
'''
plik_tekstowy.close()

