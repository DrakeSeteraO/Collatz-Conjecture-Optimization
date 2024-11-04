from Collatz1 import Collatz1
from Collatz2 import Collatz2
from Collatz3 import Collatz3
from Collatz4 import Collatz4
from Collatz5 import Collatz5
from Collatz6 import Collatz6
from Collatz7 import Collatz7

import numpy as np
from matplotlib import pyplot as plt 

num = 1000000
names = ['Original', 'Local var', 'Else:', 'Just IF', 'Bitwise', 'Remove MOD', 'Type Hinting']
times = list()

c1 = Collatz1(num)
times.append(c1.solve())

c2 = Collatz2(num)
times.append(c2.solve())

c3 = Collatz3(num)
times.append(c3.solve())

c4 = Collatz4(num)
times.append(c4.solve())

c5 = Collatz5(num)
times.append(c5.solve())

c6 = Collatz6(num)
times.append(c6.solve())

c7 = Collatz7(num)
times.append(c7.solve())

 
fig = plt.figure(figsize = (10, 5))

# creating the bar plot
br = plt.bar(names, times, color = "blue", 
        width = 0.9)

plt.xlabel("Versions")
plt.ylabel("Time in ns")
plt.title("Collatz Conjecture Optimization")
plt.bar_label(br, label_type= "edge")
plt.show()