L1 = {"a", "b", "ab", "ba"}
L2 = {"b", "c", "bc", "cb"}
L3 = {"a", "b", "c"}
L4 = {"ab", "ac"}
L5 = {"b", "bc", "ca", "c"}

def union_lenguajes(L, M):

    return L | M

def interseccion_lenguajes(L, M):

    return L & M

def concatenacion_lenguajes(L, M):

    resultado = set()
    for palabra1 in L:
        for palabra2 in M:
            resultado.add(palabra1 + palabra2)
    return resultado

def pertenece(palabra, lenguaje):

    return palabra in lenguaje


def ejercicios_union():
    print("=== EJERCICIOS DE UNIÓN ===")
    
    resultado1 = union_lenguajes(L1, L2)
    print(f"1. L1 ∪ L2 = {resultado1}")

    resultado2 = union_lenguajes(L1, L3)
    print(f"2. L1 ∪ L3 = {resultado2}")

    resultado3 = union_lenguajes(L2, L3)
    print(f"3. L2 ∪ L3 = {resultado3}")

    resultado4 = union_lenguajes(L4, L5)
    print(f"4. L4 ∪ L5 = {resultado4}")

    union_parcial = union_lenguajes(L1, L2)
    resultado5 = union_lenguajes(union_parcial, L3)
    print(f"5. L1 ∪ L2 ∪ L3 = {resultado5}")

    A = {"cad", "aca", "ad"}
    B = {"a", "d", "c"}
    resultado6 = union_lenguajes(A, B)
    print(f"6. A ∪ B = {resultado6}")

    A = {"10", "01", "11"}
    B = {"0", "1"}
    C = {"00", "10"}
    union_ab = union_lenguajes(A, B)
    resultado7 = union_lenguajes(union_ab, C)
    print(f"7. A ∪ B ∪ C = {resultado7}")

    union_l1_l2 = union_lenguajes(L1, L2)
    pertenece_abc = pertenece("abc", union_l1_l2)
    print(f"8. (L1 ∪ L2) = {union_l1_l2}")
    print(f"   ¿Pertenece 'abc' a (L1 ∪ L2)? {pertenece_abc}")

    union_l4_l5 = union_lenguajes(L4, L5)
    pertenece_a = pertenece("a", union_l4_l5)
    print(f"9. (L4 ∪ L5) = {union_l4_l5}")
    print(f"   ¿Pertenece 'a' a (L4 ∪ L5)? {pertenece_a}")

    resultado10 = union_lenguajes(L1, L4)
    print(f"10. Unión adicional: L1 ∪ L4 = {resultado10}")

def ejercicios_interseccion():
    print("\n=== EJERCICIOS DE INTERSECCIÓN ===")

    resultado1 = interseccion_lenguajes(L1, L2)
    print(f"1. L1 ∩ L2 = {resultado1}")

    resultado2 = interseccion_lenguajes(L1, L3)
    print(f"2. L1 ∩ L3 = {resultado2}")

    resultado3 = interseccion_lenguajes(L2, L3)
    print(f"3. L2 ∩ L3 = {resultado3}")

    resultado4 = interseccion_lenguajes(L4, L5)
    print(f"4. L4 ∩ L5 = {resultado4}")

    interseccion_parcial = interseccion_lenguajes(L1, L2)
    resultado5 = interseccion_lenguajes(interseccion_parcial, L3)
    print(f"5. L1 ∩ L2 ∩ L3 = {resultado5}")

    A = {"01", "10", "11"}
    B = {"10", "00", "1"}
    resultado6 = interseccion_lenguajes(A, B)
    print(f"6. A ∩ B = {resultado6}")

    A = {"x", "y", "z"}
    B = {"m", "n", "z"}
    resultado7 = interseccion_lenguajes(A, B)
    print(f"7. A ∩ B = {resultado7}")

    interseccion_l1_l2 = interseccion_lenguajes(L1, L2)
    pertenece_a = pertenece("a", interseccion_l1_l2)
    print(f"8. (L1 ∩ L2) = {interseccion_l1_l2}")
    print(f"   ¿Pertenece 'a' a (L1 ∩ L2)? {pertenece_a}")

    interseccion_l4_l5 = interseccion_lenguajes(L4, L5)
    pertenece_b = pertenece("b", interseccion_l4_l5)
    print(f"9. (L4 ∩ L5) = {interseccion_l4_l5}")
    print(f"   ¿Pertenece 'b' a (L4 ∩ L5)? {pertenece_b}")

    resultado10 = interseccion_lenguajes(L2, L3)
    print(f"10. Intersección adicional: L2 ∩ L3 = {resultado10}")

def ejercicios_concatenacion():

    print("\n=== EJERCICIOS DE CONCATENACIÓN ===")
    
    resultado1 = concatenacion_lenguajes(L1, L3)
    print(f"1. L1 · L3 = {resultado1}")

    resultado2 = concatenacion_lenguajes(L3, L1)
    print(f"2. L3 · L1 = {resultado2}")

    resultado3 = concatenacion_lenguajes(L4, L5)
    print(f"3. L4 · L5 = {resultado3}")

    resultado4 = concatenacion_lenguajes(L5, L4)
    print(f"4. L5 · L4 = {resultado4}")

    resultado5 = concatenacion_lenguajes(L1, L2)
    print(f"5. L1 · L2 = {resultado5}")

    A = {"a", "b"}
    B = {"a", "c"}
    resultado6 = concatenacion_lenguajes(A, B)
    print(f"6. A · B = {resultado6}")
 
    A = {"0", "1"}
    B = {"", "00"}  
    resultado7 = concatenacion_lenguajes(A, B)
    print(f"7. A · B = {resultado7}")

    concat_l1_l2 = concatenacion_lenguajes(L1, L2)
    pertenece_aba = pertenece("aba", concat_l1_l2)
    print(f"8. (L1 · L2) = {concat_l1_l2}")
    print(f"   ¿Pertenece 'aba' a (L1 · L2)? {pertenece_aba}")
 
    concat_l3_l4 = concatenacion_lenguajes(L3, L4)
    pertenece_cab = pertenece("cab", concat_l3_l4)
    print(f"9. (L3 · L4) = {concat_l3_l4}")
    print(f"   ¿Pertenece 'cab' a (L3 · L4)? {pertenece_cab}")

    resultado10 = concatenacion_lenguajes(L2, L5)
    print(f"10. Concatenación adicional: L2 · L5 = {resultado10}")

if __name__ == "__main__":
    ejercicios_union()
    ejercicios_interseccion()
    ejercicios_concatenacion()