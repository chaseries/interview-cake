#!/usr/local/bin/python3
import doctest

def is_proper(s):
  '''
  >>> is_proper('a(b(c()))')
  True
  >>> is_proper('a(b(c())')
  False
  >>> is_proper('a(]')
  False
  >>> is_proper('b[a(c{})]')
  True
  '''
  stack = []
  openers = '({['
  closers = ')}]'
  c_o_map = { c : o for c, o in zip(closers, openers) }
  for c in s:
    if c in openers:
      stack.append(c)
    if c in closers:
      last = stack.pop()
      if not last == c_o_map[c]:
        return False
  if stack == []:
    return True
  return False

if __name__ == '__main__':
  doctest.testmod()
