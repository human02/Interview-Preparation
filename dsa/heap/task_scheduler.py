"""

Task Scheduler

You are given a list of tasks represented by uppercase English letters ('A' to 'Z'),
and an integer n representing a cooldown interval between two same tasks.
Each task takes exactly 1 CPU interval to complete.

Tasks can be executed in any order, but identical tasks must be separated by at least n intervals,
during which the CPU may remain idle or execute other tasks.

Return the minimum number of CPU intervals required to complete all the tasks.

Examples:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: One valid execution order is:
A -> B -> idle -> A -> B -> idle -> A -> B
Total intervals = 8

Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible execution:
A -> B -> C -> D -> A -> B
No idle interval is needed as cooldown = 1.

Input: tasks = ["A","A","A","B","B","B"], n = 3
Output: 10

"""

from collections import Counter, deque
import heapq


# TC - O(n), SC - O(n)
class Solution:
    def find_time(self, tasks, n):
        """
        -> Finding freq of each task and storing it in a dict for O(1) lookup
        -> Counter is a dict
        """
        tasks_dict = Counter(tasks)

        """
        -> Max heap will allow us to keep track of the most freq task log(n) = log(26)
        -> This heap tells us the task available for processing
        -> Greedy Approach - Start with Max Freq Job
        -> Add value not the key to the max heap
        """
        maxHeap = [-cnt for cnt in tasks_dict.values()]
        heapq.heapify(maxHeap)  # maxHeap is now a heap O(n), heappush - O(nlogn)

        """
        -> Queue is used to store (freq,idle_time) jobs in wait before execute ready.
        -> It keeps track of jobs waiting for idle time completion
        """
        q = deque()  # [-cnt,idle_time]
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                frq = heapq.heappop(maxHeap)
                frq += 1  # Reduce count by 1
                if frq:
                    q.append([frq, n + time])
            if q and q[0][1] == time:
                # put back job to heap for processing
                heapq.heappush(maxHeap, q.popleft()[0])

        return time


if __name__ == "__main__":
    obj = Solution()
    print(obj.find_time(["A", "A", "A", "B", "B", "B"], 2))
    print(obj.find_time(["A", "A", "A", "B", "B", "B"], 1))
    print(obj.find_time(["A", "A", "A", "B", "B", "B"], 3))
