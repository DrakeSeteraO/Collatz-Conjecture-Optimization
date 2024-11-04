from time import perf_counter_ns

class Collatz1:
    
    def __init__(self, num):
        self.num = num
       
    def solve(self): 
        start = perf_counter_ns()
        
        while self.num != 1:
            if self.num % 2 == 1:
                self.num = 3 * self.num + 1
            elif self.num % 2 == 0:
                self.num = self.num / 2
                
        end = perf_counter_ns()
        return end - start