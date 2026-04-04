class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = 1
        temp = 0
        while left  < len(nums)-1:
            temp = nums[left] + nums[right]
            if temp == target:
                return [left, right]
            
            if right == len(nums)-1:
                left+=1
                right = left+1
            else:
                right += 1


        return []