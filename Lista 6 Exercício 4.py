def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        bissexto = True
    else:
        bissexto = False
    return bissexto

print('Insira um ano')

ano = int(input())

if bissexto(ano):
    print('O ano inserido é bissexto!')

else:
    print('O ano inserido não é bissexto!')

input()