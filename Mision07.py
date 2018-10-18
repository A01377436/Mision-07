##Autor: David Alejandro Nicolás Palos
##Descripción: Uso de ciclos while para calcular divisiones y numeros mayores dados


##Encuentra el numero mayor de una serie de números dados
def encontrarMayor():
    mayor = -1
    print("")
    numero = int(input("Teclea un número [-1 para salir]: "))
    while numero != -1:
        if numero > mayor:
            mayor = numero
            numero = int(input("Teclea un número [-1 para salir]: "))
        else:
            numero = int(input("Teclea un número [-1 para salir]: "))
    if numero == -1 and mayor != -1:
        print("El mayor es:", mayor)
    if numero == -1 and mayor == -1:
        print("No hay valor mayor")


##Encuentra el resultado de la division a base de restas
def dividir(dividendo,divisor):

    if divisor != 0:
        cociente = 0
        residuo = 0
        while dividendo >= divisor :
            dividendo = dividendo-divisor
            cociente = cociente + 1
            residuo = dividendo
        print(cociente,", sobra",residuo)


##Funcion main
def main():
        print("""Misión 07. Ciclos While
Autor: David Alejandro Nicolás Palos
Matrícula: A01377436
1.Calcular Divisiones
2.Encontrar el mayor
3.Salir""")
        opcion = int(input("Teclea tu opción:",))
        while opcion != 3:
            if opcion == 1:
                print("")
                print("Calculando divisiones")
                dividendo = int(input("Dividendo: "))
                divisor = int(input("Divisor: "))
                print(dividendo,"/",divisor,"="," ",end='')
                dividir(dividendo,divisor)
            elif opcion ==2:
                encontrarMayor()
            else:
                print("ERROR, teclea 1,2 o 3")
            print("""
Misión 07. Ciclos While
Autor: David Alejandro Nicolás Palos
Matrícula: A01377436
1. Calcular Divisiones
2. Encontrar el mayor
3. Salir""")
            opcion = int(input("Teclea tu opción:",))
        print("")
        print("Gracias por usar este programa, regresa pronto.")


main()