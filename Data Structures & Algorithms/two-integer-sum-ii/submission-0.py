class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}

        for i,n in enumerate(numbers):
            if target - n in hash_map:
                return [min(i+1, hash_map[target - n]+1), max(i+1, hash_map[target - n]+1)]
            else:
                hash_map[n] = i