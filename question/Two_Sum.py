'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

目的是查找两个数(a+b=c)，但是如果我们让它的目的变成一个数就可以简化算法(a=c-b)
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexa=-1
        indexb=-1
        dictx={}

        for index,n in enumerate(nums):
            rest=target-n
            #查看key是否在dictx中
            if rest in dictx:
                indexa=index
                indexb=dictx[rest]
            else:
                dictx[n]=index
        if indexb > indexa:
            return [indexa,indexb]
        else:
            return [indexb,indexa]

if __name__=='__main__':
    s=Solution()
    nums=[1,3,2,5,7,10,23,11]
    target=16
    print(s.twoSum(nums,target))