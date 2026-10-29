class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or target < nums[0] or target > nums[len(nums)-1]:
            return -1
        else:
            left = 0
            right = len(nums)-1

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1