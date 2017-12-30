class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1 is None or len(nums1)==0:
            m=len(nums2)
            if m%2!=0:
                return nums2[m//2]
            else:
                mid=m//2
                return (nums2[mid]+nums2[mid-1])/2
        elif nums2 is None or len(nums2)==0:
            m=len(nums1)
            if m%2!=0:
                return nums1[m//2]
            else:
                mid=m//2
                return (nums1[mid]+nums1[mid-1])/2
        else:
            k=len(nums2)+len(nums1)
            dit={}
            mid,n=0,0
            sign=-1
            if k%2!=0:
                mid=k//2
            else:
                mid=k//2
                n=mid-1
            while sign<mid:
                sign+=1
                if len(nums1)==0 and len(nums2)!=0:
                    dit[str(sign)]=nums2[0]
                    nums2=nums2[1:]
                    continue
                if len(nums2)==0 and len(nums1)!=0:
                    dit[str(sign)]=nums1[0]
                    nums1=nums1[1:]
                    continue
                if nums1[0] <= nums2[0]:
                    dit[str(sign)]=nums1[0]
                    nums1=nums1[1:]
                    continue
                if nums1[0] > nums2[0]:
                    dit[str(sign)]=nums2[0]
                    nums2=nums2[1:]

            if k%2!=0:
                return dit[str(mid)]
            else:
                return (dit[str(mid)]+dit[str(mid-1)])/2

if __name__=='__main__':
    a=[1]
    b=[2,3,4]
    so=Solution()
    print(so.findMedianSortedArrays(a,b))