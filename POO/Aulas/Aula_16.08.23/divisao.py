lower = float(input('Num esquerda: '))
upper = float(input('Num direita: '))

def displayRange(lower, upper):
    if lower < upper:
        return 0
    else:
        return lower/upper
t = displayRange(lower, upper)
print(t)