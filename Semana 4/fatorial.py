n = int(input("Digite um valor para n fatorial: "))

fatorial = n

while n > 1:
    n -= 1
    fatorial = fatorial * n

if n == 0:
    fatorial = 1

print(fatorial)