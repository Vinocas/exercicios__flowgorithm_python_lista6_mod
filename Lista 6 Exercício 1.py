def par(n):
    if n % 2 == 0:
        epar = True
    else:
        epar = False
    return epar

# Main
n = int(input('Digite o número: '))
if par(n):
    print(f"{n} é par")
else:
    print(f"{n} é impar")

input()