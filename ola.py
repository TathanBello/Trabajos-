alfabeto = {'a', 'b'}
L = {'a', 'b', 'ab', 'ba', 'aa'}

print("Verificador de palabras en el lenguaje L")
print("Escribe 'salir' para terminar el programa.\n")

while True:
    palabra = input("Ingresa una palabra: ")

    if palabra.lower() == "salir":
        print("Programa finalizado.")
        break

    if palabra in L:
        print(f"La palabra '{palabra}' pertenece al lenguaje L.\n")
    else:
        print(f"La palabra '{palabra}' NO pertenece al lenguaje L.\n")
