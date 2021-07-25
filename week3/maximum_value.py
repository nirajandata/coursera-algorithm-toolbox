# Uses python3


def get_optimal_value(capacity, val):
    value = 0.
    cap=0
    i=0
    #print(val)
    for _,i,j in val:
     weight=j
     price=i
     if(cap==capacity):
      return value
     if(weight==0 or price==0) :
      pass
     rate=min(weight,capacity)
     value+=rate*price/weight
     capacity-=rate	

      #print("second part test",price)

      #max value and average formula and density value
     
    return value


if __name__ == "__main__":
    n,capacity=map(int,input().split())
    val=[]
    #max_val=0
    for i in range(n):
     #x=[int(i) for i in input().split()]
     x,y=map(int,input().split())
     if(x==0 or y==0):
       ratio=0
     else:
       ratio=x/y
     #max_val=max(y,max_val)
     val.append([ratio,x,y])
    #first is value and second is weight
    opt_value = get_optimal_value(capacity,sorted(val,reverse=True))
    print("{:.4f}".format(opt_value))
