import pytest
from asteroid_collision import Solution

sol = Solution()

@pytest.mark.parametrize(
    "asteroids, expected",
    [
        ([2, -2], []),                  # both destroy each other
        ([10, 20, -10], [10, 20]),      # small asteroid destroyed
        ([10, 2, -5], [10]),            # chain reaction
        ([5, 10, -5], [5, 10]),         # left asteroid destroyed
        ([-2, -1, 1, 2], [-2, -1, 1, 2]) # no collisions
    ]
)
def test_asteroid_collision(asteroids, expected):
    assert sol.asteroidCollision(asteroids) == expected