#Paweł Puźniak, Niestaconarne Rok II - L2 (MITI) - UP Kraków 2019
# Wykorzystując pętle, break i else proszę napisać program, w którym użytkownik w przeciągu skończonej liczby prób ma
# odgadnąć ustawione wcześniej słowo. W przypadku, kiedy mu się uda program ma wypisać gratulacje, a jeśli skończy
# się liczba prób to poinformować o przegranej.

print("Witaj w programie! Wpisz liczbę prób do odgadnięcia:")
liczbaProb = input()
print("Okej, twoja liczba prób to: " + liczbaProb)

haslo = "python"

odliczanie = 0
podliczenie = int(liczbaProb)
odpowiedz = 0
while odliczanie < int(liczbaProb) and odpowiedz != haslo:
    odpowiedz = input("Zgadnij hasło!")
    odliczanie += 1
    podliczenie -= 1
    if odpowiedz.lower() == haslo:
        print("Gratulacje! Odgadłeś!")
        break
    print("To nie to hasło, próbuj ponownie! Zostały Ci " + str(podliczenie) + " podejścia!")
else:
    print("Ups, skończyły się podejścia - spróbuj innym razem!")
koniec = input()
if koniec == True:
    sys.exit()