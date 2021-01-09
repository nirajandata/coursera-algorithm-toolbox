# Uses python3
import sys

def gcd(a,b):
  if (b==0):
    return a
  a%=b
  return gcd(b,a)

def lcm_naive(a, b):
  result=int((a/gcd(a,b))*b)
  return result


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

