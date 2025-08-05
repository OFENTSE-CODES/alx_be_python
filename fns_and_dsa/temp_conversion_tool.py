# temp_conversion_tool.py

# --------------------------
# Global Conversion Factors
# --------------------------

# This factor is used to convert Fahrenheit to Celsius.
# Formula: (F - 32) × (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# This factor is used to convert Celsius to Fahrenheit.
# Formula: (C × 9/5) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# --------------------------
# Conversion Functions
# --------------------------

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# --------------------------
# Main User Interaction
# --------------------------

def main():
    try:
        # Prompt for temperature input
        temp_input = input("Enter the temperature value: ").strip()
        temperature = float(temp_input)  # Validate numeric input

        # Prompt for scale (Celsius or Fahrenheit)
        scale = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Conversion logic
        if scale == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
        elif scale == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        else:
            raise ValueError("Invalid scale. Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# --------------------------
# Run the Program
# --------------------------

if __name__ == "__main__":
    main()