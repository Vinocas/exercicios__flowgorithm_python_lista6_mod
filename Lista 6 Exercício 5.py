def primo(n):
    c = 0
    mult = 0
    for c in range (1, n + 1, 1):
        if n % c == 0:
            mult = mult + 1
    if mult == 2:
        primo = True
    else:
        primo = False
    
    return primo

# Main
n = int(input('Insira um número: '))
if n > 1:
    if primo(n):
        print('O número é primo!')
    else:
        print('O número não é primo!')
else:
    print('O número é primo!')

input()