from time import perf_counter_ns

class Collatz7:
    
    def __init__(self, num: int):
        self.num: int = num
       
    def solve(self): 
        start: int = perf_counter_ns()
        
        num: int = self.num
        while num != 1:
            if num & 0b1 == 1:
                num: int = (num << 1) + num + 1
            num: int = num >> 1
                
        end: int = perf_counter_ns()
        return end - start
    
c = Collatz7(10)
print(c.solve())