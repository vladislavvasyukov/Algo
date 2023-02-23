class Solution:
    @staticmethod
    def factorial(num):
        result = 1
        for i in range(1, num+1):
            result *= i
        return result

    def fun(self, nums, n, kth):
        count = n
        fact = self.factorial(count)
        result = []
        while nums:
            fact = fact // count
            i, kth = divmod(kth, fact)
            result.append(nums[i])
            nums = nums[:i] + nums[i+1:]
            count -= 1

        return result

    def get_kth_permutation(self, n, kth):
        nums = []
        for i in range(n):
            nums.append(str(i+1))
        return self.fun(nums, n, kth-1)


print(Solution().get_kth_permutation(3,4))
