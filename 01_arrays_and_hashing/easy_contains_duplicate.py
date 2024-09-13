class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        # T: O(n)
        # S: O(n)
        
# class Solution(object):
#     def containsDuplicate(self, nums):
#         sorted_nums = sorted(nums)

#         for i in range(len(sorted_nums)-1):
#             if sorted_nums[i] == sorted_nums[i+1]:
#                 return True
#         return False
#         # T: O(nlog(n))  because the sorting step dominates the runtime
#         # S: O(1)  no additional space is used that grows with the input size.


# class Solution(object):
#     def containsDuplicate(self, nums):

#         for i in range (len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False 
#         # T: O(n^2) the inner loop runs a decreasing number of times for each iteration of the outer loop (n*(n-1)/2)
#         # S: O(1)  no additional space is used that grows with the input size.