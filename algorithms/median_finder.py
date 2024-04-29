import heapq

class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))
        else:
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(3)
    mf.addNum(5)
    mf.addNum(-1)
    mf.addNum(2)
    m = mf.findMedian()
    print(m)