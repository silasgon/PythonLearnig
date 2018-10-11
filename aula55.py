# a = 10
# b = 25
# c = 66
#
# x = int(input("Digite um número: "))
#
# #if( x == a or x == b or x == c):
# if(x in [a, b, c]):
#     print("o numero está contido!")
# else:
#     print("O numero não esta contido")

#-------------------------------------------------------------------------

cores = ["Azul", "vermelho", "amarelo", "branco"]

while True:
    cor = input("Digite o nome de uma cor ou 0 para sair: ")

    if(cor == "0"):
        break
    if cor in cores:
        print("A cor esta contida e é a cor: " + cor)
    else:
        print("A cor não esta contida")
