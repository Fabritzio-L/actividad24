def factorial(n):
    if n==0 or n== 1:
        return 1
    else:
        return n* factorial(n-1)
def suma_naturales(n):
    if n<0:
        return "Solamente numeros positivos"
    else:
        return n + suma_naturales(n-1)
def fibonacci(n):

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
            print(suma_naturales(n))