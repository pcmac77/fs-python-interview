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
answer_dict = dict([(7, 13), (10, 55), (20, 6765), (30, 832040), (40, 102334155)])
for k,v in answer_dict.items():
  t0=time.time()
  print("fibonacci({})={}".format(k, fibonacci(k)))
  assert fibonacci(k) == v
  print("Took {} seconds".format(time.time()-t0))
print("---Done with fibonacci")
