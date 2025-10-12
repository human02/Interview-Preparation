import pytest
from dsa.arrays.next_permutation import Solution


@pytest.fixture
def solution():
    return Solution()


def test_next_permuation_None(solution):
    assert solution.find_next("") == ""


def test_next_permuation_numerical_desc(solution):
    assert solution.find_next("321") == "123"


def test_next_permuation_numerical(solution):
    assert solution.find_next("151") == "511"


def test_next_permuation_string(solution):
    assert solution.find_next("abdc") == "acbd"
