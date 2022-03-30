class Solution:
    def firstUniqChar(self, s: str) -> int:
#         cnt = collections.Counter()
#         for ch in s:
#             cnt[ch]+=1

#         for index in range(len(s)):
#             if cnt[s[index]] == 1:
#                 return index
#         return -1

            d = {}
            for i in range(len(s)):
                if s[i] not in d:
                    d[s[i]] = 1
                else:
                    d[s[i]] += 1
            
            for i in range(len(s)):
                if d[s[i]] == 1:
                    return i
            return -1

                                               