n = int(input("Digite o valor de n: "))

if n % 2 != 0:
    i = 0 
    k = 1
    while i < n:
        print (k)
        k = k + 2
        # n = n + 2
        i += 1
else:
    z = 0
    a = 1
    while z < n:
        print(a)
        a = a + 2
        z += 1