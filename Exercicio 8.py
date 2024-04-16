print('Calculadora Operador')
n1=float(input('Digite um numero:'))
op=input('Defina o operador:')
n2=float(input('Digite outro numero:'))
if op == '-':
    print('{:.0f}'.format(n1 - n2))
elif op == '+':
    print('{:.0f}'.format(n1 + n2))
elif op == '/':
    print('{:.0f}'.format(n1 / n2))
elif op == '*':
    print('{:.0f}'.format(n1 * n2))


