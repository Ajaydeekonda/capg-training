import math

def basic_operations():
    """Demonstrate basic math operations."""
    a, b = 10, 3
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulo: {a} % {b} = {a % b}")

def power_and_root():
    """Demonstrate power and root functions."""
    x = 16
    print(f"Square Root of {x}: {math.sqrt(x)}")
    print(f"{x} raised to power 3: {math.pow(x, 3)}")
    print(f"{x} raised to power 0.5: {math.pow(x, 0.5)}")  # Same as sqrt

def logarithm_operations():
    """Demonstrate logarithm functions."""
    num = 100
    print(f"Natural Log (ln) of {num}: {math.log(num)}")
    print(f"Log base 10 of {num}: {math.log10(num)}")
    print(f"Log base 2 of {num}: {math.log2(num)}")

def trigonometry():
    """Demonstrate trigonometric functions."""
    angle = math.radians(45)  # Convert degrees to radians
    print(f"sin(45°): {math.sin(angle)}")
    print(f"cos(45°): {math.cos(angle)}")
    print(f"tan(45°): {math.tan(angle)}")

def rounding_operations():
    """Demonstrate rounding functions."""
    num = 7.75
    print(f"Ceiling of {num}: {math.ceil(num)}")
    print(f"Floor of {num}: {math.floor(num)}")
    print(f"Round {num} to nearest integer: {round(num)}")

def constants():
    """Print mathematical constants."""
    print(f"Value of PI: {math.pi}")
    print(f"Value of Euler's number (e): {math.e}")
    print(f"Golden ratio (φ): {math.tau}")

# Example Usage
if __name__ == "__main__":
    print("Basic Operations:")
    basic_operations()

    print("\nPower and Root Operations:")
    power_and_root()

    print("\nLogarithm Operations:")
    logarithm_operations()

    print("\nTrigonometry:")
    trigonometry()

    print("\nRounding Operations:")
    rounding_operations()

    print("\nMathematical Constants:")
    constants()
