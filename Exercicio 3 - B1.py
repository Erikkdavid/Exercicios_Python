#triangulo
l1=int(input('Primeiro lado:'))
l2=int(input('Segundo lado:'))
l3=int(input('Terceirp numero:'))
if l1 == l2 and l1 == l3:
    print('O triangulo e Equilatero')
elif l1 == l2 and l1 > l3 or l1 == l3 and l1 > l2 or l3 == l2 and l3 > l1:
    print('O triangulo e Isosceles')
else:
    print('O triangulo e Escaleno')
