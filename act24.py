def factorial(n):
    if n==0 or n== 1:
        return 1
    else:
        return n* factorial(n-1)
def suma_naturales(n):
    if n==1:
        return 1
    else:
        return n + suma_naturales(n-1)
def fibonacci(n):
    if  n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
def contar_letras():
    pass
while True:
    print("MENU")
    print("1. Calcular factorial")
    print("2. Sumar números naturales")
    print("3. Calcular número de Fibonacci")
    print("4. Contar una letra en una palabra")
    print("5. Invertir una cadena de texto")
    print("6. Calcular la potencia de un número")
    print("7. Salir del programa")
    opcion= input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
            n= int(input("Ingrese un numero: "))
            if n<0:
                print("Solamente numeros positivos")
            else:
                print(f"El factorial de {n} es: {factorial(n)}")
        case "2":
            n=int(input("Ingrese un numero: "))
            if n<0:
                print("Solamente numeros positivos")
            print(suma_naturales(n))
        case "3":
            n = int(input("Ingrese un numero: "))
            if n < 0:
                print("Solamente numeros positivos")
            else:
                print(fibonacci(n))
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion invalida. Ingrese una opcion valida")
