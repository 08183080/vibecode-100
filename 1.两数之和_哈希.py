from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
            
        for i, num in enumerate(nums):
            complement = target - num
            if complement in record:
                return [i, record[complement]]
            record[num] = i