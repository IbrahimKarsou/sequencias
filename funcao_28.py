import numpy as np

print('digite um angulo')
n = (float(input()) * 3.141593) / 180


def fatorial(y):
    count = 1
    resultado = 1.0
    while count <= y:
        resultado *= count
        count += 1
    return resultado


def sequencia(x):
    seq = f'cos {x} = '
    for i in range(0, 6):
        seq = seq + f'{((-1)**i/fatorial(2*i))*(x**(2*i))} +'
    print(seq)


sequencia(n)
