def safe_divide(numerator, denominator):
    """
    Safely divide numerator by denominator.
    Returns a string with the result or an error message.

    Expected outputs (exact text):
    - Normal: "The result of dividing {num} by {den} is {result}"
    - Non-numeric: "Error: Please provide numeric values."
    - Division by zero: "Error: Division by zero is not allowed."
    """
    # First, convert inputs to floats and handle non-numeric values
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please provide numeric values."

    # Perform the division in its own try/except so ZeroDivisionError is caught explicitly
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    return f"The result of dividing {num} by {den} is {result}"