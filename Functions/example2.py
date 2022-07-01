from example1 import ci_calc,si_calc
choice=input(" What you want to do ? si/ci")
if choice =="si":
    si_calc()
elif choice=="ci":
    ci_calc()
else:
    print("Inavlid choice")
    