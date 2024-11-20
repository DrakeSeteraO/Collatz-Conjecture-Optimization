from time import perf_counter_ns

class Collatz8:
    
    def __init__(self, num: int):
        self.num: int = num
       
    def solve(self): 
        start: int = perf_counter_ns()
        
        num: int = self.num
        if num & 0b1 == 1:
            num: int = (num << 1) + num + 1
        while num != 1:
            num: int = (num << 1) + num + 1
            while num & 0b1 == 0:
                num: int = num >> 1
        end: int = perf_counter_ns()
        return end - start
