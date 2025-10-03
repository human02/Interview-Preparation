"""
Find the Fastest 3 Horses

You have 25 horses and a race track that can accommodate only 5 horses at a time. Each horse has a consistent speed, but you don't have a stopwatch to measure their actual speeds. You can only determine the relative order of horses within each race.
Your task: Write a function that finds the top 3 fastest horses using the minimum number of races.
"""

import random


def race(horses):
    """Race horses and return sorted by speed (fastest first)"""
    return sorted(horses, key=lambda x: x[1], reverse=True)


def find_top_3():
    """Find top 3 fastest horses from 25 horses in 7 races"""

    # Create 25 horses with random speeds: (id, speed)
    horses = [(i, random.randint(100, 350)) for i in range(1, 26)]

    # STEP 1: Race 5 groups of 5 horses (Races 1-5)
    groups = []
    for i in range(5):
        group = horses[i * 5 : (i + 1) * 5]
        result = race(group)
        groups.append(result)
    print(groups)

    # STEP 2: Race group winners (Race 6)
    winners = [group[0] for group in groups]
    winners_result = race(winners)
    fastest = winners_result[0]

    # STEP 3: Select candidates for 2nd and 3rd
    group_A = groups[winners.index(winners_result[0])]
    group_B = groups[winners.index(winners_result[1])]
    group_C = groups[winners.index(winners_result[2])]

    candidates = [group_A[1], group_A[2], group_B[0], group_B[1], group_C[0]]

    # STEP 4: Race candidates (Race 7)
    final_result = race(candidates)

    # Top 3 horses
    top_3 = [fastest, final_result[0], final_result[1]]

    # Display results
    print("\nTop 3 Horses (found in 7 races):")
    for i, (id, speed) in enumerate(top_3, 1):
        print(f"  {i}. Horse {id} - Speed {speed}")

    # Verify correctness
    actual_top_3 = race(horses)[:3]
    found_ids = sorted([h[0] for h in top_3])
    actual_ids = sorted([h[0] for h in actual_top_3])

    if found_ids == actual_ids:
        print("\n✓ Correct top 3 found!")
    else:
        print("\n✗ Error in algorithm")


# Run the simulation
find_top_3()
