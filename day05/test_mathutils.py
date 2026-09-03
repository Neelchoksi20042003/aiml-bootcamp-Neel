from mathutils import average, biggest, is_prime


def test_average_basic():
    assert average([2, 4, 6]) == 4.0


def test_average_empty():
    assert average([]) == 0.0


def test_biggest_basic():
    assert biggest([10, 50, 20]) == 50


def test_biggest_empty():
    assert biggest([]) is None


def test_is_prime_two():
    assert is_prime(2) is True


def test_is_prime_composite():
    assert is_prime(9) is False


def test_is_prime_zero():
    assert is_prime(0) is False


def test_is_prime_one():
    assert is_prime(1) is False


def test_is_prime_negative():
    assert is_prime(-5) is False
