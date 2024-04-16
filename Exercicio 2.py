print('Cardapio')
l=int(input('Digite o codigo do lanche:'))
q=int(input('Qual a quantidade?'))
if l == 100:
    print('O cachorro-quente vai sair por R${:.2f}'.format(1.20 * q))
elif l == 101:
    print('O Bauru simples vai sair por R${:.2f}'.format(1.30 * q))
elif l == 102:
    print('O Bauru com o ovo vai sair por R${:.2f}'.format(1.50 * q))
elif l == 103:
    print('O Hamburguer vai sair por R${:.2f}'.format(1.20 * q))
elif l == 104:
    print('O Cheeseburguer vai sair por R${:.2f}'.format(1.70 * q))
elif l == 105:
    print('O suco vai sair por R${:.2f}'.format(2.20 * q))
elif l == 106:
    print('O Refrigerante vai sair por R${:.2f}'.format(1.00 * q))
else:
    print('Codigo invalido!')
