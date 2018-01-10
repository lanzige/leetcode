class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dit={}
        length=0
        start=0
        end=0
        for index,ch in enumerate(s):
            if ch in dit:
                for mid in dit[ch]:
                    sign=False
                    if s[mid+1:index]==s[index-1:mid:-1]:
                        if index-mid+1>length:
                            length=index-mid+1
                            start=mid
                            end=index
                            sign=True
                    if sign:
                        break
                dit[ch].append(index)
            else:
                dit[ch]=[index]
        return s[start:end+1]

if __name__=='__main__':
    so=Solution()
    s="babadada"
    print(so.longestPalindrome(s))