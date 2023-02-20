class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]
            # greater than target, decrease sum
            if  currSum > target:
                r -= 1
            if  currSum < target:
                l += 1
            if currSum == target:
                return [l+1, r+1]
               
