def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return numerator / denominator

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
