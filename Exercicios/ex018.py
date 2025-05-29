from math import sin, cos, tan, radians

angulo = float(input("Digite um angulo: "))
print(f'O seno do angulo {angulo} é {sin(radians(angulo)):.2f}.')
print(f'O cosseno do angulo {angulo} é {cos(radians(angulo)):.2f}.')
print(f'A tangente do angulo {angulo} é {tan(radians(angulo)):.2f}.')
