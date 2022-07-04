def fine(category,days):
    if category=='A':
        if days<=10:
            return days*100
        else:
            return (days*100)*2
    elif category=='B':
        if days<=10:
            return days*50
        else:
            return (days*50)*2
    elif category=='C':
        if days <=10:
            return days*10
        else:
            return (days*10)*2

if __name__=='__main__':
    cate=input("which category do you have : ?? ")
    days=int(input("enter the number of days : ??"))
    print(f'you have to pay {fine(cate,days)}')