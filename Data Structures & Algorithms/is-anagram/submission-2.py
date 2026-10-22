class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # print(sorted(list(s)), sorted(list(t)))
        # return sorted(list(s)) == sorted(list(t))
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False

        counts = [0] * 26
        # print(counts)

        for char_s, char_t in zip(s, t):
            counts[ord(char_s) - ord('a')] += 1
            # print(counts)
            counts[ord(char_t) - ord('a')] -= 1
            # print(counts)
            # print("----------------------------------")

        return all(count == 0 for count in counts)