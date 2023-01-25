"""

"""

#  non stack solution
# O(n) time | O(n) space


def sunsetViews(buildings, direction):
    buildingWithView = []
    startIdx = 0 if direction == "WEST" else len(buildings) - 1
    step = 1 if direction == "WEST" else -1

    idx = startIdx
    runningMaxHeight = 0

    # east stop condition and west stop condition
    while idx >= 0 and idx < len(buildings):
        buildingHeight = buildings[idx]
        if buildingHeight > runningMaxHeight:
            buildingWithView.append(idx)
            runningMaxHeight = buildingHeight
        # runningMaxHeight = max(runningMaxHeight, buildingHeight) - also correct but remove above line
        idx += step

    # As in East case we run from end to start, thus index and added in descending order.
    if direction == "EAST":
        return buildingWithView[::-1]

    return buildingWithView
