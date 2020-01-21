###########
# Fibonacci
# Write a function fib(n) that returns a Fibonacci num.
# Your solution should be *performant*
# +++ START YOUR IMPLEMENTATION
def fibonacci(n):
  # fibonacci secuence
  # 0, 1, 1, 2, 3, 5, 8, 13
  # --- START YOUR IMPLEMENTATION
  pass

# Test code below
import time
for x in [7, 10, 20, 30, 40]:
  t0=time.time()
  print("fibonacci({})={}".format(x, fibonacci(x)))
  print("Took {} seconds".format(time.time()-t0))
print("---Done with fibonacci")
