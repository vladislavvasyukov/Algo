import heapq
from collections import defaultdict
from typing import List


class Solution:
    def __init(self, k):
        self.k = k
        self.lo = []  # max heap
        self.hi = []  # min heap
        self.ans = []

    def _add_to_result(self):
        if self.k % 2:
            self.ans.append(self.hi[0])
        else:
            self.ans.append((self.hi[0] - self.lo[0]) / 2)

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        self.__init(k)
        if not nums or not k:
            return self.ans

        for i in range(k):
            if len(self.lo) == len(self.hi):
                heapq.heappush(self.hi, -heapq.heappushpop(self.lo, -nums[i]))
            else:
                heapq.heappush(self.lo, -heapq.heappushpop(self.hi, nums[i]))

        self._add_to_result()
        to_remove = defaultdict(int)
        for i in range(k, len(nums)):
            heapq.heappush(self.lo, -heapq.heappushpop(self.hi, nums[i]))
            out_num = nums[i-k]
            if out_num > -self.lo[0]:
                heapq.heappush(self.hi, -heapq.heappop(self.lo))

            to_remove[out_num] += 1
            while self.lo and to_remove[-self.lo[0]]:
                to_remove[-self.lo[0]] -= 1
                heapq.heappop(self.lo)

            while to_remove[self.hi[0]]:
                to_remove[self.hi[0]] -= 1
                heapq.heappop(self.hi)

            self._add_to_result()

        return self.ans

if __name__ == '__main__':
    # [1, -1, -1, 3, 5, 6]
    print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    # [2, 3, 3, 3, 2, 3, 2]
    print(Solution().medianSlidingWindow([1,2,3,4,2,3,1,4,2], 3))
