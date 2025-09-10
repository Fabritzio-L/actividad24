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
    if  n<2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
def contar_letras(palabra,letra,i=0):
    if i==len(palabra):
        return 0
    elif palabra[i] == letra:
        return  1+ contar_letras(palabra,letra,i+1)
    else:
        return contar_letras(palabra,letra,i+1)
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
                print(f"El número de fibonacci es {fibonacci(n)}")
        case "4":
            palabra= input("Ingrese una palabra: ")
            letra= input("Ingrese la letra a contar: ")
            print(f"La letra {letra} en {palabra} aparece {contar_letras(palabra,letra)} veces")
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion invalida. Ingrese una opcion valida")
