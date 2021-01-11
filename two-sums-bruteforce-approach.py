class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.i = 0
        self.j = 0
        self.op = []
        for self.i in range(len(nums)-1):
            for self.j in range(self.i+1,len(nums)):
                #if self.j == self.i:
                #    continue
                if nums[self.j] + nums[self.i] == target:
                    self.op.append(self.i)
                    self.op.append(self.j)
                    return self.op
