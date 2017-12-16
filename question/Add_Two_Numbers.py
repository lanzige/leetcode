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
        head=None
        mid=head
        tmp=0
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            while (l1 or l2):
                sum=0
                if l1:
                    sum+=l1.val
                    l1=l1.next
                if l2:
                    sum+=l2.val
                    l2=l2.next
                if mid is None:
                    head=ListNode((sum+tmp)%10)
                    mid=head
                else:
                    mid.next=ListNode((sum+tmp)%10)
                    mid=mid.next
                tmp=(sum+tmp)//10
            if tmp !=0:
                mid.next=ListNode(tmp)
        return head

if __name__=='__main__':
    l1=ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(3)
    l2=ListNode(4)
    l2.next=ListNode(5)
    l2.next.next=ListNode(6)

    s=Solution()
    ln=s.addTwoNumbers(l1,l2)
    while ln:
        print(ln.val)
        ln=ln.next