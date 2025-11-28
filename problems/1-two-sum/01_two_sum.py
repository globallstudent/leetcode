from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        d = {}

        for i, j in enumerate(nums):
            diff = target - j
            if diff in d:
                result = [d[diff], i]
            else:
                d[j] = i

        return result


target = 9
nums = [2, 7, 11, 15]

solution = Solution()

print(solution.twoSum(nums=nums, target=target))
