'''
Please note that the below solution will cause a time-limit exceed error
It was the initial solution that I came up with
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        new_set = set()

        for curr_cur in range(len(nums)):
            for one_step_right in range(len(nums)):
                for two_step_right in range(len(nums)):
                    if curr_cur == one_step_right or curr_cur == two_step_right or one_step_right == two_step_right:
                        continue
                    if nums[curr_cur] + nums[one_step_right] + nums[two_step_right] == 0:
                        new_set.add(tuple(sorted((nums[curr_cur], nums[one_step_right], nums[two_step_right]))))

        result = [list(t) for t in new_set]
        return result