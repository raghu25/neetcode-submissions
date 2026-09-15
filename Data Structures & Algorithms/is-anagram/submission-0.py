class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cS = defaultdict(int)
        cT = defaultdict(int)
        for ch in s:
            cS[ch] += 1
        for ch in t:
            cT[ch] += 1
        return cS == cT
