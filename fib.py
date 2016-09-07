import time
import sys
import os
n = int(input('Enter n value:\t'))
start_time = time.time()
a, b = 0, 1
if n>0:
  print(b)
  for i in range(0,n-1):
    a, b = b, a+b
    print(b)
  print("The %d th element in the fibonacci series is %d" %(n,b))
else:
  print("Can u please enter positive intergers")
print("Time taken to this process is  %s seconds " % (time.time() - start_time))
