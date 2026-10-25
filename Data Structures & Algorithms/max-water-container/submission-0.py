class Solution:
    def maxArea(self, height: List[int]) -> int:
        area:int  = 0

        mh = max(height)
        l, r = 0, len(height) - 1

        while l < r:
            left = height[l]
            right = height[r]

            area = max(min(left, right) * (r - l), area)

            if left < right:
                l += 1
            else:
                r -= 1

            if mh * (r - l) < area:
                break

        return area