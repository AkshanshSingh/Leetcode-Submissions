class Solution:
    def reverse(self, x: int) -> int:
        self.rev = 0
        self.ctr = 0
        self.x = x
        self.demo = x
        self.flag = 1
        if self.x < 0:
            self.x = abs(self.x)
            self.demo = abs(self.demo)
            self.flag = -1
        while self.demo > 0 :
            self.demo = self.demo//10
            self.ctr += 1
        while self.ctr > 0:
            self.rev = self.rev + (self.x%10)*(10 **(self.ctr - 1))
            self.x = self.x//10
            self.ctr -= 1
        return self.flag*self.rev
