print('digite um angulo para descobrir o seno do mesmo')
n = float(input())


def fatorial(y):
    """faz um fatorial do numero passado como parametro"""
    count = 1
    resultado = 1.0
    while count <= y:
        resultado *= count
        count += 1
    return resultado


def sen_x(x):
    seq = f'sen{x} = '
    for i in range(0, 6):
        seq = seq + f'{x**(2*i+1)/fatorial(2*i+1)} +'
    print(seq)


sen_x(n)
