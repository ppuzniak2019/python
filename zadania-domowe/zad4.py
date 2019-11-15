#Paweł Puźniak, Niestaconarne Rok II - L2 (MITI) - UP Kraków 2019
# Za pomocą list comprehension proszę stworzyć listę z pierwszych liter imion w liście
# ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa'].

lista=['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']

list_len = len(lista)

lista2 = [lista[element][:1] for element in range(list_len)]
print(lista2)