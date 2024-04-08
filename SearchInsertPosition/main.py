class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for number in range(len(nums)):
            if (nums[number] == target) or (nums[number] > target):
                return number
        return number+1


print(Solution().searchInsert([1,2,4,5], 6))