class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]: # 거짓이므로 뒤에있는걸 아예 체크하지 않는다

                
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
        used[c] = i
        return max_length;


a = Solution()
print(a.lengthOfLongestSubstring(' abcab'))