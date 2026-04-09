class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = []
        for index in range(len(nums)):
            left = 0
            right = len(nums) -1
            while left < right:
                if left == index:
                    left += 1
                elif right == index:
                    right -= 1
                else:
                    sum_elements = nums[index] + nums[left] + nums[right]
                    if sum_elements == 0:
                        temp_arr = [nums[index], nums[left], nums[right]]
                        temp_arr.sort()
                        if temp_arr not in output:
                            output.append(temp_arr)

                        left += 1
                    elif sum_elements < 0:
                        left += 1
                    else: 
                        right -= 1

        return output