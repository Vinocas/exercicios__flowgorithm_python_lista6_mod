def nota(n):
    if n >= 6:
        nota = True
    else:
        nota = False
    return nota

# Main
print('Digite a nota, de 0 a 10: ')

n = int(input())

while n > 10 or n < 0:
    print('O valor da nota não pode ser menor que 0 ou maior que 10! Digite novamente o valor da nota: ')
    n = int(input())

if nota(n):
    print('A nota inserida é maior que 6. APROVADO')

else:
    print('A nota inserida é menor que 6. REPROVADO')

input()