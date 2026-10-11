class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # print(sorted(list(s)), sorted(list(t)))
        # return sorted(list(s)) == sorted(list(t))
        return Counter(s) == Counter(t)