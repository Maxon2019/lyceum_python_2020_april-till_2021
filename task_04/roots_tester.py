
from task_04.find_quadratic_equation_roots import find_quadratic_equation_roots


def test_two_roots():
    a, b, c = 1, 2, -3
    expected = (1, -3)
    actual = find_quadratic_equation_roots(a, b, c)

    assert len(actual) == 2
    assert sorted(expected) == sorted(actual)


def test_one_root():
    a, b, c = 3, -6, 9
    expected = (3)
    actual = find_quadratic_equation_roots(a, b, c)

    assert sorted(expected) == sorted(actual)


def ne_groot():
    a, b, c = 5, 3, 7
    expected = None
    actual = find_quadratic_equation_roots(a, b, c)

    assert sorted(actual) == sorted(expected)
