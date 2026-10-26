"""Python Programs Collection: factorial, Fibonacci and structure-to-dictionary."""


def factorial(n):
    """Return n! using a loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


def factorial_recursive(n):
    """Return n! using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci(count):
    """Return the first `count` numbers of the Fibonacci series."""
    if count < 0:
        raise ValueError("Count cannot be negative.")
    series = []
    first, second = 0, 1
    for _ in range(count):
        series.append(first)
        first, second = second, first + second
    return series


def pairs_to_dict(pairs):
    """Convert a list of (key, value) pairs into a dictionary."""
    result = {}
    for key, value in pairs:
        result[key] = value
    return result


def lists_to_dict(keys, values):
    """Convert a list of keys and a list of values into a dictionary."""
    if len(keys) != len(values):
        raise ValueError("keys and values must have the same length.")
    return dict(zip(keys, values))


class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course


def object_to_dict(obj):
    """Convert an object's attributes into a dictionary."""
    return dict(vars(obj))


if __name__ == "__main__":
    print("Factorial of 5 (loop):", factorial(5))
    print("Factorial of 5 (recursive):", factorial_recursive(5))
    print("First 10 Fibonacci numbers:", fibonacci(10))
    print("Pairs to dict:", pairs_to_dict([("a", 1), ("b", 2)]))
    print("Lists to dict:", lists_to_dict(["x", "y"], [10, 20]))
    print("Object to dict:", object_to_dict(Student("Asha", 7, "CSE")))
