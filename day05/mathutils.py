"""Provide basic mathematical utility functions."""

# from typing import Optional


def average(nums: list[int | float]) -> float:
    """Return the mean of a list of numbers.

    Args:
        nums: A list of integers or floats. May be empty.

    Returns:
        The mean as a float, or 0.0 if the list is empty.
    """
    if not nums:
        return 0.0

    return sum(nums) / len(nums)


def biggest(nums: list[int]) -> int | None:
    """Return the largest number from a list.

    Args:
        nums: A list of integers. May be empty.

    Returns:
        The largest integer, or None if the list is empty.
    """
    if not nums:
        return None

    return max(nums)


def is_prime(n: int) -> bool:
    """Check whether a number is prime.

    Args:
        n: The integer to check.

    Returns:
        True if the number is prime, otherwise False.
        Numbers less than 2 are not prime.
    """
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
