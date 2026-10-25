class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
         return 0
        result = 1

        for x in (nums_set := {*nums}):
            if x-1 not in nums_set:
                y = x + 1
                while y in nums_set:
                    y += 1
                if y - x > result:
                    result = y-x
        return result