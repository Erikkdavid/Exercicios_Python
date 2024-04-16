# Calculadora de Bhaskara
print('FÓRMULA DE BHASKARA')
print('Ax² + Bx + C = 0')

# Solicita os valores de a, b e c
a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

# Calcula o discriminante (delta)
delta = (b ** 2) - 4 * a * c

print("\n**************************\n")

# Verifica as condições e calcula as raízes
if a == 0:
    print("O valor de 'a' deve ser diferente de zero.")
elif delta < 0:
    print("A equação não possui raízes reais.")
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"Raiz 1 (x1): {x1}")
    print(f"Raiz 2 (x2): {x2}")
