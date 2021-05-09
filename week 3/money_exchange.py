# Uses python3
import sys

def get_change(m):
    #write your code here
    num=0
    while(m>=1):
      if(m>=10):
        m=m-10
      elif(m>=5):
        m=m-5
      else:
        m=m-1
      num=num+1  
    return num

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
