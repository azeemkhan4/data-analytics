def heronf():
    a=float(input("enter first side"))
    b=float(input("enter second side"))
    c=float(input("enter third side"))
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print(" the area of triangle is:",area)

def area_circle():
    r=int(input("Enter the radius of the circle"))
    area=3.14*(r**2)
    print("the area of the circle is", area)

def area_rectangle():
    l=int(input("enter the length:"))
    b=int(input("enter the breadth:"))
    area= l*b
    print(" the area of the rectangle is :",area)
    
def menu():
    print("1. Area of triangle")
    print("2. Area of circle")
    print("3. Area of rectangle")
    print("4. Quit")
    choice=int(input(" Enter your choice"))
    if choice==1:
        heronf()
    elif choice==2:
        area_circle()
    elif choice==3:
        area_rectangle()
    elif choice==4:
        print("goodbye")
    else:
        print("invalid choice")
        menu()
if __name__=="__main__":
    menu()