#Uses python3

def largest_number(val):
    answer=[]
    while(val!=[]):
     max_num="0"
     for i in val:
      if(int(i+max_num)>=int(max_num+i)):
       max_num=i
     answer.append(max_num)
     val.remove(max_num)   
 
    return "".join(answer) 

if __name__ == '__main__':
    n=int(input())
    val=[x for x in input().split()]
    print(int(largest_number(val)))
    
