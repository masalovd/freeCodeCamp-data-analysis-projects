import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)
    arr_flattened = np.array(list)
    metrics = {
        'mean': 'mean',
        'variance': 'var',
        'standard deviation': 'std',
        'max': 'max',
        'min': 'min',
        'sum': 'sum'
    }

    calculations = dict()

    for metric, method in metrics.items():
        calculations[metric] = [
            getattr(matrix, method)(axis=0).tolist(),
            getattr(matrix, method)(axis=1).tolist(),
            getattr(arr_flattened, method)().tolist(),
        ]

    return calculations
