class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(" : ")", "[": "]", "{" : "}"}
        st = []
        for ch in s:
            if ch in {'(', '{', '['}:
                st.append(ch)
            else:
                if not st or d[st[-1]] != ch:
                    return False
                st.pop()
        return True if not st else False