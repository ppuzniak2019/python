#Paweł Puźniak, Niestaconarne Rok II - L2 (MITI) - UP Kraków 2019
# Proszę posortować podaną listę po drugim elemencie każdej listy, a w przypadku, kiedy są równe to po trzecim elemencie:
# list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]


lista = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
print("Lista przed sortowaniem:")
print (lista)

def sortowanie_po_3(list_element):
    return list_element[2]
def sortowanie_po_2(list_element):
    return list_element[1]

lista.sort(key=sortowanie_po_3) #najpierw sortujemy całość po 3 elemencie, przyda się jeżeli drugie byłyby równe
lista.sort(key=sortowanie_po_2) #i teraz elegancko sortujemy po drugim :)

print("Lista posortowana:")
print (lista)
