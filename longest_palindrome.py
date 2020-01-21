# +++ START YOUR IMPLEMENTATION

def palindrome_helper(s, left, right):
  if len(s) in [0, 1]: return len(s)
  if s[left] != s[right]: return 0
  while s[left] == s[right] and (0 < left) and right < len(s)-1:
    print('right:%s' % right)
    left -= 1
    right += 1
  length = right - left + 1
  # will count more loop in normal case, so need minus 2
  if s[left] != s[right]:
    length -= 2
  return length


def longest_palindrome(s):
  # Write a function to return the length of the longest palinfrome
  # in an input string.  
  # Ex:
  #   longest_palindrome('aab') => 2
  #   longest_palindrome('Aaab') => 2
  #   longest_palindrome('') => 0
  #   longest_palindrome('fuasdfjh123454321ddd') => 9
  # 
  pass

# --- START YOUR IMPLEMENTATION


print(longest_palindrome('aab'))
print(longest_palindrome('fuasdfjh123454321ddd'))
