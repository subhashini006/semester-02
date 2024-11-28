a=int("enter the marks obtained in subject 1:")
b=int("enter the marks obtained in subject 2:")
c=int("enter the marks obtained in subject 3:")
d=int("enter the marks obtained in subject 4:")
e=int("enter the marks obtained in subject 5:")
tot=a+b+c+d+e
per=(tot/500)*100
if per>=80:
    print("Grade A")
elif per>=70:
    print("Grade B")
elif per>=60:
    print("Grade C")
elif per>=40:
    print("Grade D")
else:
    print("Grade E")
