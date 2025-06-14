def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return numerator / denominator

    except ValueError:
        print("Error: Please enter numeic value only ")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
