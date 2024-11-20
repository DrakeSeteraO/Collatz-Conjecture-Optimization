from time import perf_counter_ns

class Collatz9:
    
    def __init__(self, num: int):
        self.num: int = num
       
    def solve(self): 
        start: int = perf_counter_ns()
        
        a: int = self.num
        if a & 0b1 == 1:
            a: int = (a << 1) + a + 1
        while a != 1:
            a: int = (a << 1) + a + 1
            while a & 0b1 == 0:
                a: int = a >> 1
        end: int = perf_counter_ns()
        return end - start
