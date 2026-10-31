class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        q = {}
        res = 0
        #  window lenght - most repeatet characher
        l = 0

        maxf = 0

        for r in range(len(s)):
            q[s[r]] = 1 + q.get(s[r], 0)
            maxf = max(maxf, q[s[r]])
            # tweak

            if (r - l + 1) - maxf > k:
                q[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res