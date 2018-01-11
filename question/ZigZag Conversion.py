class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        dit=[]
        index=0
        line_num=0
        add=1
        if numRows==1 or len(s)==0:
            return s
        for i in range(numRows):
            line=[]
            dit.append(line)
        while True:
            dit[line_num].append(s[index])
            line_num+=add
            if line_num ==numRows-1 or line_num==0:
                add=-add
            if index>=len(s)-1:
                break
            else:
                index+=1
        str=''
        for i in range(numRows):
            str+=''.join(dit[i])
        return str

if __name__=='__main__':
    so=Solution()
    s='ABC'
    print(so.convert(s,1))