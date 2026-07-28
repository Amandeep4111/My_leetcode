class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for word in strs:

            
            key = "".join(sorted(word))

            if key not in mp:
                mp[key] = []

            mp[key].append(word)

        return list(mp.values())

# class Solution:
#     def groupAnagrams(self, strs):
#         d = {}

#         for word in strs:
#             freq = [0] * 26

#             for ch in word:
#                 freq[ord(ch) - ord('a')] += 1

#             key = tuple(freq)

#             if key not in d:
#                 d[key] = []

#             d[key].append(word)

#         return list(d.values())
        