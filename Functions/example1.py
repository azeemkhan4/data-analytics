#creation
def si_calc():
    p=float(input("Enter the principle:"))
    r=float(input("Enter the rate:"))
    t=float(input("Enter the interest:"))
    si=p*(r*t)/100
    print(f'Simple interest is {si}')

def ci_calc():
    p=float(input("Enter the principle:"))
    r=float(input("Enter the rate:"))
    t=float(input("Enter the interest:"))
    ci=p*(1+r/100)**t
    print(f'Compund interest is {ci}')
#calling functions
#si_calc()
#ci_calc()