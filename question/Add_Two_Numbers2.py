# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.to_ListNode(self.to_int(l1)+self.to_int(l2))
    def to_int(self,ln):
        sum=0
        mul=1
        if ln:
            while ln:
                sum=sum+ln.val*mul
                mul=mul*10
                ln=ln.next
        else:
            num=None
        return sum
    def to_ListNode(self,num):
        mul=10
        head=None
        mid=None
        if num == 0:
            return ListNode(0)
        while (num%10) !=0 or num//10 !=0:
            if head:
                mid.next=ListNode(num%10)
                mid=mid.next
            else:
                head=ListNode(num%10)
                mid=head
            num=num//10
        return head
if __name__=='__main__':
    l1=ListNode(1)
    l1.next=ListNode(5)
    l1.next.next=ListNode(3)
    l2=ListNode(4)
    l2.next=ListNode(5)
    l2.next.next=ListNode(6)

    s=Solution()
    ln=s.addTwoNumbers(l1,l2)
    while ln:
        print(ln.val)
        ln=ln.next