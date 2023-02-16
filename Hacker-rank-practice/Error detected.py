#Errors detected during execution are called exceptions.



#T=int(input())
for i in range(T):
    
    try:
        a,b=map(int,input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as v:
        print("Error Code:",v)