
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == "":
            return 0
        else:
            str_list=list(s)
            maxlength=1
            dictx={}
            head=0
            length=len(s)
            tail=head
            while True:
                if tail>=length:
                    if tail - head > maxlength:
                        maxlength=tail-head
                    break
                if str_list[tail] in dictx:
                    if tail - head > maxlength:
                        maxlength=tail-head
                    head+=1
                    tail=head
                    if length-head<maxlength:
                        break
                    dictx={}
                    continue
                else:
                    dictx[str_list[tail]]=tail
                tail+=1
            return maxlength

if __name__=='__main__':
    str_test="qwewweerqwr"
    sol=Solution()
    print(sol.lengthOfLongestSubstring(str_test))