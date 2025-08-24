# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def _parse_temperature_or_raise(text):
    """Parse a temperature string to float or raise the required ValueError."""
    try:
        return float(text)
    except Exception:
        # EXACT message per spec
        raise ValueError("Invalid temperature. Please enter a numeric value.")


def main():
    temp_input = input("Enter the temperature to convert: ").strip()
    temperature = _parse_temperature_or_raise(temp_input)

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    else:
        # Unit validation (not part of the ValueError check, but helpful)
        print("Invalid unit. Please enter C or F.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        # Keep CLI friendly output while still having an actual ValueError in code
        print(e)