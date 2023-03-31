def raiz(a,b,c,):
    delta = (b**2)-(4*a*c)

    if delta > 0:
        x1 = (-b+(delta**0.5))/(2*a)
        x2 = -(b-(delta**0.5))/(2*a)
        raiz = "x1 = " + str(x1) + " e x2 = " + str(x2)
    else:
        raiz = "Valor de Δ é negativo, logo não existem raízes reais!"

    return raiz
    
# Main

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

print(raiz(a,b,c))

input()