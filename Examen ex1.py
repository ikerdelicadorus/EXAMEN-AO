def llegir_llista_enters():
    llista = []
    while True:
        entrada = input("Introdueix un número (o '.' per acabar): ")
        if entrada == ".":
            break
        try:
            numero = int(entrada)
            llista.append(numero)
        except ValueError:
            print("Si us plau, introdueix un número vàlid.")
    return llista

# Provar la funció
llista_enters = llegir_llista_enters()
print(f"Llista de nombres llegida: {llista_enters}")



def senars_llista(llista):
    return [num for num in llista if num % 2 != 0]

# Provar la funció
llista_prova = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
llista_senars = senars_llista(llista_prova)
print(f"Llista original: {llista_prova}")
print(f"Llista de números senars: {llista_senars}")



def sumar_parells_llista(llista):
    return sum(num for num in llista if num % 2 == 0)

# Provar la funció
llista_prova = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_parells = sumar_parells_llista(llista_prova)
print(f"Llista original: {llista_prova}")
print(f"Suma dels números parells: {suma_parells}")



def cercar_numero_llista(llista, numero):
    try:
        return llista.index(numero)
    except ValueError:
        return -1

# Provar la funció
llista_prova = [10, 20, 30, 40, 50]
numero = 30
posicio = cercar_numero_llista(llista_prova, numero)
print(f"La posició del número {numero} dins la llista és: {posicio}")

numero = 60
posicio = cercar_numero_llista(llista_prova, numero)
print(f"La posició del número {numero} dins la llista és: {posicio}")



def llegir_llista_paraules():
    llista = []
    while True:
        paraula = input("Introdueix una paraula (o '.' per acabar): ")
        if paraula == ".":
            break
        llista.append(paraula)
    return llista

# Provar la funció
llista_paraules = llegir_llista_paraules()
print(f"Llista de paraules llegida: {llista_paraules}")



def crear_paraula_llista(llista):
    paraula = ''.join(paraula[0] for paraula in llista if paraula)
    return paraula

# Provar la funció
llista_prova = ["gato", "perro", "caballo", "vaca", "oveja", "gallina"]
paraula_resultat = crear_paraula_llista(llista_prova)
print(f"Llista de paraules: {llista_prova}")
print(f"Paraula formada per les inicials: {paraula_resultat}")



import random

def crear_llista_num_aleatoris():
    llista_aleatoria = [random.randint(1, 100) for _ in range(5)]
    return llista_aleatoria

# Provar la funció
llista_prova = crear_llista_num_aleatoris()
print(f"Llista de números aleatoris: {llista_prova}")



def comparar_llista(llista1, llista2):
    resultat = []
    for i in range(len(llista2)):
        if llista2[i] not in llista1:
            resultat.append(0)
        elif llista2[i] == llista1[i]:
            resultat.append(2)
        else:
            resultat.append(1)
    return resultat

# Provar la funció
llista1 = [10, 20, 30, 40, 50]
llista2 = [50, 20, 10, 40, 60]
resultat = comparar_llista(llista1, llista2)
print(f"Llista 1: {llista1}")
print(f"Llista 2: {llista2}")
print(f"Resultat de la comparació: {resultat}")



def majors_edat(edat1, edat2):
    resultat = {}
    
    if edat1 >= 18:
        resultat['edat1'] = 'major d’edat'
    else:
        resultat['edat1'] = 'menor d’edat'
    
    if edat2 >= 18:
        resultat['edat2'] = 'major d’edat'
    else:
        resultat['edat2'] = 'menor d’edat'
    
    return resultat

# Provar la funció
edat1 = 20
edat2 = 16
resultat = majors_edat(edat1, edat2)
print(f"L'edat1 ({edat1}) és: {resultat['edat1']}")
print(f"L'edat2 ({edat2}) és: {resultat['edat2']}")



def menu():
    print("Opcions disponibles:")
    print("1. Mostrar dígits parells d'un número")
    print("2. Eliminar primer i últim element d'una llista")
    print("3. Comprovar si una llista està ordenada")
    print("4. Comprovar si una llista té duplicats")
    print("5. Crear llista de 20 elements aleatoris i comprovar duplicats")
    print("6. Eliminar elements duplicats d'una llista")
    print("7. Crear llista a partir d'un fitxer")
    print("8. Cercar índex d'una paraula en una llista ordenada")
    print("9. Mostrar números de 1 a 10 en ordre invers")
    print("10. Mostrar números parells i senars fins a 100")
    print("11. Sumar números entre dos números donats")
    print("12. Imprimir un patró d'estrelles")
    print("13. Mostrar paraules en posicions parells d'una llista")
    print("14. Mostrar patró de números")
    print("15. Mostrar números primers entre 1 i 100")
    print("16. Realitzar operacions amb la calculadora")
    print("17. Llegir llista de nombres fins a '.'")
    print("18. Mostrar números senars d'una llista")
    print("19. Sumar números parells d'una llista")
    print("20. Cercar número dins una llista")
    print("21. Llegir llista de paraules fins a '.'")
    print("22. Crear paraula amb inicials de paraules d'una llista")
    print("23. Crear llista de 5 números aleatoris")
    print("24. Comparar dues llistes de 5 elements")
    print("25. Comprovar si edats són majors d'edat")

    while True:
        try:
            opcio = int(input("Selecciona una opció (1-25): "))
            if 1 <= opcio <= 25:
                return opcio
            else:
                print("Opció no vàlida, si us plau tria un número entre 1 i 25.")
        except ValueError:
            print("Entrada no vàlida, si us plau introdueix un número.")

def main():
    opcio = menu()

    if opcio == 1:
        numero = int(input("Introdueix un número: "))
        print(digits_parells(numero))
    elif opcio == 2:
        llista = [int(x) for x in input("Introdueix els elements de la llista separats per espais: ").split()]
        print(eliminarcapicua(llista))
    elif opcio == 3:
        llista = [int(x) for x in input("Introdueix els elements de la llista separats per espais: ").split()]
        print(esta_ordenada(llista))
    elif opcio == 4:
        llista = [int(x) for x in input("Introdueix els elements de la llista separats per espais: ").split()]
        print(hi_ha_duplicats(llista))
    elif opcio == 5:
        llista = llista_20_elements()
        print(f"Llista generada: {llista}")
        print(f"Hi ha duplicats? {hi_ha_duplicats(llista)}")
    elif opcio == 6:
        llista = [int(x) for x in input("Introdueix els elements de la llista separats per espais: ").split()]
        print(elimina_duplicats(llista))
    elif opcio == 7:
        nom_fitxer = input("Introdueix el nom del fitxer: ")
        print(crear_llista_fitxer(nom_fitxer))
    elif opcio == 8:
        llista = input("Introdueix els elements de la llista ordenada separats per espais: ").split()
        paraula = input("Introdueix la paraula a cercar: ")
        print(index_paraula(llista, paraula))
    elif opcio == 9:
        imprimir_invers()
    elif opcio == 10:
        print("Números parells fins a 100:")
        mostrar_parells()
        print("Números senars fins a 100:")
        mostrar_senars()
    elif opcio == 11:
        a = int(input("Introdueix el primer número: "))
        b = int(input("Introdueix el segon número: "))
        print(suma_interval(a, b))
    elif opcio == 12:
        imprimir_patron()
    elif opcio == 13:
        llista = input("Introdueix les paraules de la llista separades per espais: ").split()
        print(elements_parells(llista))
    elif opcio == 14:
        imprimir_patron_numeros()
    elif opcio == 15:
        print("Números primers entre 1 i 100:")
        print(primers_fins_a_100())
    elif opcio == 16:
        calculadora()
    elif opcio == 17:
        print(llegir_llista_enters())
    elif opcio == 18:
        llista = [int(x) for x in input("Introdueix els elements de la llista separats per espais: ").split()]
        print(senars_llista(llista))
    elif opcio == 19:
        llista = [int(x) for x in input("Introdueix els elements de la llista separats per espais: ").split()]
        print(sumar_parells_llista(llista))
    elif opcio == 20:
        llista = [int(x) for x in input("Introdueix els elements de la llista separats per espais: ").split()]
        numero = int(input("Introdueix el número a cercar: "))
        print(cercar_numero_llista(llista, numero))
    elif opcio == 21:
        print(llegir_llista_paraules())
    elif opcio == 22:
        llista = input("Introdueix les paraules de la llista separades per espais: ").split()
        print(crear_paraula_llista(llista))
    elif opcio == 23:
        print(crear_llista_num_aleatoris())
    elif opcio == 24:
        llista1 = [int(x) for x in input("Introdueix els elements de la primera llista separats per espais: ").split()]
        llista2 = [int(x) for x in input("Introdueix els elements de la segona llista separats per espais: ").split()]
        print(comparar_llista(llista1, llista2))
    elif opcio == 25:
        edat1 = int(input("Introdueix la primera edat: "))
        edat2 = int(input("Introdueix la segona edat: "))
        print(majors_edat(edat1, edat2))

if __name__ == "__main__":
    main()
