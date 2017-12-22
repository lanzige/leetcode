'''
此算法的具体思维是，在两个重复之间都是没重复的字符
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexes = {}
        longest = 0
        last_repeating = -1
        for i, c in enumerate(s):
            if c in indexes and last_repeating < indexes[c]:
                last_repeating = indexes[c]
            if i - last_repeating > longest:
                longest = i - last_repeating
            indexes[c] = i

        return longest

if __name__=='__main__':
    str_test="qwedsadasas"
    sol=Solution()
    print(sol.lengthOfLongestSubstring(str_test))