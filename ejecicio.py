import itertools  

alfabeto = ['0', '1']
longitud_max = 3

L = set()

for i in range(1, longitud_max + 1):
    for combinacion in itertools.product(alfabeto, repeat=i):
        L.add(''.join(combinacion))

print("Lenguaje L con todas las combinaciones de hasta 3 símbolos:")
print(L)
