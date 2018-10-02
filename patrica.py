numero1 = input("Digite um numero: ")
numero1 = int(numero1)

numero2 = input("Digite um segundo numero: ")
numero2 = int(numero2)

if(numero1 == numero2): #operador de igualdade
    print("O numero %d é igual a %d. " %(numero1, numero2))
if(numero1 != numero2): #operador de diferença
    print("o numero %d é diferente de %d " %(numero1, numero2))
if(numero1 < numero2): #operador menor que
    print("o numero %d é menor que %d " % (numero1, numero2))
if(numero1 > numero1): #operador maior que
    print("o numero %d é maior que %d " % (numero1, numero2))
if(numero1 >= numero2): #operador maior ou igual
    print("o numero %d é maior ou igual que %d " % (numero1, numero2))
if(numero1 <= numero2): #operador menor ou igual
    print("o numero %d é menor ou igual que %d " % (numero1, numero2))