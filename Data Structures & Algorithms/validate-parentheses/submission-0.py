class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) < 2:
            return False
        tp = deque(s[0])
        for i in range(1, len(s)):
            tp.append(s[i])
            if len(tp) < 2:
                continue
            if (tp[-1] == ")" and tp[-2] == "(") or (tp[-1] == "}" and tp[-2] == "{") or (tp[-1] == "]" and tp[-2] == "["):
                tp.pop()
                tp.pop()
        if not tp:
            return True
        return False