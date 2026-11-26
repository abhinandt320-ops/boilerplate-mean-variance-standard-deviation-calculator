import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(numbers).reshape(3, 3)

    operations = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum
    }

    calculations = {}

    for name, function in operations.items():
        calculations[name] = [
            function(arr, axis=0).tolist(),
            function(arr, axis=1).tolist(),
            function(arr).tolist()
        ]

    return calculations