import pytest
from dsa.trees.bt.height_bt import Solution

# test_height_bt.py


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@pytest.fixture
def solution():
    return Solution()


def test_height_empty_tree(solution):
    assert solution.find_height(None) == 0


def test_height_single_node(solution):
    root = TreeNode(1)
    assert solution.find_height(root) == 1


def test_height_left_skewed(solution):
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert solution.find_height(root) == 3


def test_height_right_skewed(solution):
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert solution.find_height(root) == 3


def test_height_balanced_tree(solution):
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert solution.find_height(root) == 3


def test_height_unbalanced_tree(solution):
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6)), None), TreeNode(3))
    assert solution.find_height(root) == 4
