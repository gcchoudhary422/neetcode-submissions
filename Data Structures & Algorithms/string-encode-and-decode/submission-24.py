class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for st in strs:
            # print(st)
            encoded += str(len(st)) + '#' + st
        # print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0
        while i < len(s)-1:
            j = i
            # print(f"loop j : {j}, loop i: {i}")
            while s[j] != '#':
                j += 1
            # print(f"i = {i}, j = {j}")
            # print(s[i:j])
            word_len = int(s[i:j])
            decoded.append(s[j+1 : j + word_len + 1])
            i = j + word_len + 1
        return decoded




