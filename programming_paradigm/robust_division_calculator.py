def safe_divide(numerator, denominator):
    """
    Performs safe division with error handling.
    Returns:
      - Result as: "The result of the division is X"
      - Error for zero division: "Error: Cannot divide by zero."
      - Error for invalid input: "Error: Please enter numeric values only."
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"