def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Try performing the division
        result = num / den
        return f"The result of dividing {num} by {den} is {result}"

    except ValueError:
        return "Error: Please provide numeric values."

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."