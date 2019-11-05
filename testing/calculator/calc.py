from math import sqrt


def add(a: int, b: int) -> int:
    """Adds two integers.

    Args:
        a: an integer.
        b: an integer.
    Returns:
        The sum of the two integers.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtracts two integers.

    Args:
        a: an integer.
        b: an integer.
    Returns:
        The difference of the two integers.
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """Multiplies two integers.

    Args:
        a: an integer.
        b: an integer.
    Returns:
        The product of the two integers.
    """
    return a * b


def normal_division(a: int, b: int) -> int:
    """Divides two integers.

    Args:
        a: an integer.
        b: an integer.
    Returns:
        The quotient of the two integers.
    """
    return a / b


def integer_division(a: int, b: int) -> int:
    """Divides two integers using integer division.

    Args:
        a: an integer.
        b: an integer.
    Returns:
        The quotient of the two integers.
    """
    return a // b


def modulus(a: int, b: int) -> int:
    """Modulus's two integers.

    Args:
        a: an integer.
        b: an integer.
    Returns:
        The remainder of the quotient.
    """
    return a % b


def quadratic_formula(a: int, b: int, c: int) -> int:
    """Solves the quadratic formula.

    Args:
        a: an integer.
        b: an integer.
        c: an integer.
    Returns:
        The solution to the quadratic formula.
    """
    return (-1 * b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    return (-1 * b - sqrt(b**2 - 4 * a * c)) / (2 * a)