num1 = int(input("digite um número: "))

if(num1 > 10 ):
    print("O valor é maior que 10!")
    if(num1 <= 15):
        print("O valor é maior que 10 porém menor que 15")
    else:
        if(num1 <= 50):
            print("O valor é maior que 10 e menor que 50!")
        else:
            print("O valor é maior que 50!")
else:
    if(num1 > 5 ):
        print("O número é maior que 10 más menor que 5")
        if(num1 == 7 ):
            print("o numero é igual a 7")
    else:
        print("O valor é menor que 5")