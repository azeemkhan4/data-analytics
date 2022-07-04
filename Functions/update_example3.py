def area_of_tri(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
    
def area_of_circle(r):
    return  (3.14*(r**2))
    
def area_of_rectangle(l,b):
    return (l*b)

def menu():
    print("1. Area of triangle")
    print("2. Area of circle")
    print("3. Area of rectangle")
    print("4. Quit")
    choice=int(input(" Enter your choice"))
    if choice==1:
        a=float(input("enter first side"))
        b=float(input("enter second side"))
        c=float(input("enter third side"))
        area=area_of_tri(a,b,c)
        print(f'the area is {area}')
    elif choice==2:
        r=int(input("Enter the radius of the circle"))
        area=area_of_circle(r)
        print(f'the area is {area}')
    elif choice==3:
         l=int(input("enter the length:"))
         b=int(input("enter the breadth:"))
         area=area_of_rectangle(l,b)
         print(f'the area is {area}')
    elif choice==4:
        print("goodbye")
    else:
        print("invalid choice")
        menu()
if __name__=="__main__":
    menu()