print("Szybkie mnożenie dużych liczb\n\n")

val1 = input("Podaj wartość pierszą:")
val2 = input("Podaj wartość drugą:")

val1_check = 100 - int(val1)
val2_check = 100 - int(val2)

sum1 = val1_check + val2_check

result1 = 100 - sum1
result2 = val1_check * val2_check

wynik = result1 + result2
print("Wynik to: " + str(wynik))
wynikSprawdzajacy = int(val1) * int(val2)
print("Wynik sprawdzający: " + str(wynikSprawdzajacy))
if wynik == wynikSprawdzajacy:
    print("Ok")
else:
    print("Ops, jest błąd!")
