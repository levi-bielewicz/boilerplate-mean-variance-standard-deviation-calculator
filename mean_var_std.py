import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(list).reshape(3,3)
    print(a)

    dictionary = dict()
    dictionary['mean'] = [a.mean(0), a.mean(1), a.mean()]
    dictionary['variance'] = [a.var(0), a.var(1), a.var()]
    dictionary['standard deviation'] = [a.std(0), a.std(1), a.std()]
    dictionary['max'] = [a.max(0), a.max(1), a.max()]
    dictionary['min'] = [a.min(0), a.min(1), a.min()]
    dictionary['sum'] = [a.sum(0), a.sum(1), a.sum()]

    return calculate[(0, 1, 2, 3, 4, 5, 6, 7, 8)]
