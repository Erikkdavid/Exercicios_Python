print('Nota da prova')
n=int(input('Digite a nota:'))
if n >= 86:
    print('A')
elif n <= 85 and n >= 61:
    print('B')
elif n <= 60 and n >= 36:
    print('C')
elif n <= 35 and n >= 1:
    print('D')
else:
    print('E')
