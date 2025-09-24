def compute(a, b, op):
    """Compute a basic arithmetic operation.

    Accepts a and b as strings or numbers. op is one of: 'add','sub','mul','div'.
    Raises ValueError on invalid input or operations (including division by zero).
    """
    try:
        x = float(a)
        y = float(b)
    except Exception:
        raise ValueError("Please enter valid numbers for both inputs.")

    if op == "add":
        return x + y
    if op == "sub":
        return x - y
    if op == "mul":
        return x * y
    if op == "div":
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        return x / y

    raise ValueError("Unknown operation")
