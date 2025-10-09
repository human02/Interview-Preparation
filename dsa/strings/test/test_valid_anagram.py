# test_valid_anagram.py
import pytest
from dsa.strings.valid_anagram import Solution


@pytest.fixture
def solution():
    """Fixture to provide a Solution instance to all tests"""
    return Solution()


def test_valid_anagram_basic_true(solution):
    assert solution.isAnagram("racecar", "carrace") == True


def test_valid_anagram_basic_false(solution):
    assert solution.isAnagram("jar", "jam") == False


def test_valid_anagram_with_spaces(solution):
    assert solution.isAnagram("a b c", "c b a") == True
    assert solution.isAnagram("a b c", "abc") == False


def test_valid_anagram_with_uppercase(solution):
    assert solution.isAnagram("Abc", "bAc") == True
    assert solution.isAnagram("Abc", "bac") == False


def test_valid_anagram_with_special_chars(solution):
    assert solution.isAnagram("!@#", "#@!") == True
    assert solution.isAnagram("!@#", "!@") == False


def test_valid_anagram_empty_strings(solution):
    assert solution.isAnagram("", "") == True


def test_valid_anagram_unicode(solution):
    assert solution.isAnagram("你好", "好你") == True
    assert solution.isAnagram("你好", "你你") == False


def test_valid_anagram_numbers(solution):
    assert solution.isAnagram("123", "321") == True
    assert solution.isAnagram("123", "12") == False
