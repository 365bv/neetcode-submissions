class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False

        need = Counter(s1)

        def add (ch: str, delta: int = 1):
            need[ch] += delta
            if need[ch] == 0: del need[ch]

        for i in range(n2):
            add(s2[i], -1)
            if i >= n1: add(s2[i-n1], 1)
            if not need: return True

        return False