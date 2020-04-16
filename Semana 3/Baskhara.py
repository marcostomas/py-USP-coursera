import math

valorA = int(input("Digite o valor de A"))
valorB = int(input("Digite o valor de B"))
valorC = int(input("Digite o valor de C"))


delta = (valorB ** 2) - (4 * ( valorA ) * ( valorC ))

if delta < 0:
    print("Não existem raízes reais para esse número")

baskharaP = (( -valorB ) + math.sqrt(delta)) / (2 * valorA)
baskharaN = (( -valorB ) - math.sqrt(delta)) / (2 * valorA)

if delta == 0:
    print("A raiz real de de Baskhara é:",  baskharaP)

if delta > 0:
    print("As raízes reais de Baskhara são:", baskharaP, baskharaN)