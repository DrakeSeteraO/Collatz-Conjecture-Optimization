from time import perf_counter_ns

class Collatz6:
    
    def __init__(self, num):
        self.num = num
       
    def solve(self): 
        start = perf_counter_ns()
        
        num = self.num
        while num != 1:
            if num & 0b1 == 1:
                num = (num << 1) + num + 1
            num = num >> 1
                
        end = perf_counter_ns()
        return end - start