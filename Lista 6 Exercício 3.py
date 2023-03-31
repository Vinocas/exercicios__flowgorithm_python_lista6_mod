def fv(c, n, i):
    return c * (1 + i) ** n

c = float(input('Digite o capital inicial: '))
i = float(input('Digite a taxa de juros: '))
n = int(input('Digite o prazo: '))

print(f"O valor futuro do capital é: {fv(c, n, i)}")

input()