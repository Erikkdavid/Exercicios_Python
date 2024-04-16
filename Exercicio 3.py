print('Raiz positiva')
r=int(input('Digite um numero:'))
if r >= 0:
    print('a raiz de {} vai ser {:.1f}'.format(r, r **(1/2)))
else:
    print('Número Invalido!')
