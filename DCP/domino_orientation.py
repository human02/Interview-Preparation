"""

You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL. 

"""

# O(n) time | O(n) space
def push_dominoes(dominoes):
    n = len(dominoes)

    # It stores the forces experienced at each domino
    forces = [0] * n

    # finding force for R right-side
    f = 0
    for i in range(n):
        if dominoes[i] == "R":
            f = n
        elif dominoes[i] == "L":
            f = 0
        else:
            f = max(
                f - 1, 0
            )  # (f-1) as each . will reduce the force by 1 unit, max to prevent -1 case
        forces[i] += f

    # finding force for L left-side
    f = 0
    for i in range(n - 1, -1, -1):
        if dominoes[i] == "L":
            f = n
        elif dominoes[i] == "R":
            f = 0
        else:
            f = max(
                f - 1, 0
            )  # (f-1) as each . will reduce the force by 1 unit, max to prevent -1 case
        forces[i] -= f

    # list to store the final output
    result = ""

    # last iteration to check aggregate force to tell the fall side or standing.
    for i in range(n):
        if forces[i] == 0:
            result += "."
        elif forces[i] > 0:
            result += "R"
        else:
            result += "L"
    return result


print(push_dominoes(".L.R....L"))  # LL.RRRLLL.
print(push_dominoes("..R...L.L"))  # ..RR.LLLL.
