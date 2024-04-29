import collections
import heapq
from typing import List


class Solution:
    # Time complexity N(log K)
    # Space complexity O(k) + O(k) => O(k)
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        heap_dict = collections.defaultdict(int)

        res = []

        for i in range(k):
            # в Python heap - это по умолчанию MinHeap, поэтому добавляем отрицательные значения
            heapq.heappush(max_heap, -nums[i])
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if k % 2 == 1:
            median = -max_heap[0]
            res.append(median)
        else:
            median = (-max_heap[0] + min_heap[0]) / 2
            res.append(median)

        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            heap_dict[prev_num] += 1

            balance = -1 if prev_num <= median else 1
            if nums[i] <= median:
                balance += 1
                heapq.heappush(max_heap, -nums[i])
            else:
                balance -= 1
                heapq.heappush(min_heap, nums[i])

            if balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            elif balance > 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

            while max_heap and heap_dict[-max_heap[0]] > 0:
                heap_dict[-max_heap[0]] -= 1
                heapq.heappop(max_heap)

            while min_heap and heap_dict[min_heap[0]] > 0:
                heap_dict[min_heap[0]] -= 1
                heapq.heappop(min_heap)

            if k % 2 == 1:
                median = -max_heap[0]
                res.append(median)
            else:
                median = (-max_heap[0] + min_heap[0]) / 2
                res.append(median)

        return res
