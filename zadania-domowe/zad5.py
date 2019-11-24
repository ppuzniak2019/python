#Proszę tak skopiować poniższy słownik, żeby di['four'][0] = 'cztery' nie powodowało zmiany w kopii.
import copy

di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
di2 = di.copy()             #pierwszy sposób kopiowania
di3 = copy.deepcopy(di)     #drugi sposób kopiowania - WŁAŚCIWY ABY NIE POWODOWAŁO ZMIANY

print(di)
print(di2)
print(di3)

di['four'][0] = 'cztery'    #wykonujemy działanie

print(di)                   #{'one': [1], 'two': [2], 'three': [3], 'four': ['cztery']}
print(di2)                  #{'one': [1], 'two': [2], 'three': [3], 'four': ['cztery']}
print(di3)                  #{'one': [1], 'two': [2], 'three': [3], 'four': [4]}