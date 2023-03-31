def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat * i
        i = i + 1
    res = fat

    return res

def combinacao(n,p):
    res = fatorial(n)/fatorial(p)*fatorial(n-p)

    return res

def arranjo(n,p):
    res = fatorial(n)/fatorial(n-p)

    return res

# Main

n = int(input('Digite o valor de n: '))
p = int(input('Digite o valor de p: '))

print('Combinação (n,p) = ' + str(combinacao(n,p)))
print('Arranjo (n,p) = ' + str(arranjo(n,p)))

input()