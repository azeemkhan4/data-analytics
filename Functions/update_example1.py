from re import T


def simple_interest(p:int,r:int,t:int):
    ''' Calculates simple interest  ''' #it is a docstring
    return(p*r*t)/100

#int lagana optionl hai
# 3 int  as input lega aur as a output dega float value
# apne lie nhi dusro ki understanding k lie 
# never use input inside a function

def compound_interest(p,r,t):
    return p*(1+r/100)**t

if __name__=="__main__":
#sample use
 p=10000
 r=5
 t=3
 si=simple_interest(p,r,t)
 ci=compound_interest(p,r,t)
 print(f'Simple Interest {si}')
 print(f'Compund interest {ci}')

#sample use 2 input from user
p=float(input("Enter the principle:"))
r=float(input("Enter the rate:"))
t=float(input("Enter the interest:"))
si=simple_interest(p,r,t)
ci=compound_interest(p,r,t)
print(f'Simple Interest {si}')
print(f'Compund interest {ci}')