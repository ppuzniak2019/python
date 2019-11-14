# Proszę sprawdzić czas potrzebny na przeszukanie poniższej listy pod kątem -1. Proszę zastosować wszystkie
# sposoby przeszukania, które przyjdą do głowy.
#    from random import randint
#    long_list = [randint(0, 3000) for element in range(1000000)]

from random import randint
import time

long_list = [randint(0, 3000) for element in range(1000000)]
poszukiwana = -1

start_time = time.time()
long_list.count(poszukiwana)
end_time = time.time() - start_time
print("Poszukiwanie 1 sposobem: " + str(end_time))

start_time = time.time()
poszukiwana in long_list
end_time = time.time() - start_time
print("Poszukiwanie 2 sposobem: " + str(end_time))



