# proszę na dowolnej funkcji przetestować parametry pozycyjne, z nazwami, *args i **kwargs. Sprawdzić w jakiej kolejności
# mogą być ustawiane. Czy można bez błędu wywołać poniższą funkcję bez wprowadzania w niej zmian.

# -------------------- Funkcja która obsługuje *args

def funkcjaTestowa(*argv):
    for arg in argv:
        print(arg)


funkcjaTestowa('Hello', 'World', 'Testuje', 'Wszystkie Parametry', 'Funkcji')

# -------------------- Funkcja która obsługuje nazwy i *kwargs

def drukaFunkcjaTestiwa(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


drukaFunkcjaTestiwa("Cześć", pierwszy='111', drugi='222', trzeci='333')

# -------------------- Funkcja która łączy nazwy, *args i *kwargs

def trzeciaFunkcjaTesowa(arg1, arg2, *inne, **pozostale):
    print(arg1 + arg2)
    for arg in inne:
        print(arg)
    for key, value in pozostale.items():
        print("%s == %s" % (key, value))

trzeciaFunkcjaTesowa("Pierwszy", "Drugi", "test", "test2", "test3", testuje=111, testuje2=222)

# -------------------- Funkcja działa z poniższym wykonaniem

def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)

person_print("Paweł", "Puźniak", "dupa", "można wywołać", "kiedy zrobimy taki myk: ", age="12")
