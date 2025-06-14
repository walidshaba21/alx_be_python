def safe_divide(numerator, denominator):
    numerator =  int(numerator)
    denominator = int(denominator)
    if denominator == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    return numerator / denominator

