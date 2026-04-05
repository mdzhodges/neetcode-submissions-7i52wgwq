import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        current_product = 1
        for i in range(n):
            prefix[i] = current_product
            current_product *= nums[i]

        n = len(nums)
        result = [1] * n 
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product*prefix[i]
            suffix_product *= nums[i]

        return result