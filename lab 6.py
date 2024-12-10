import array as a
arr=a.array('i')
x=int(input("Enter number of elements to be inserted:"))
c_odd=0
c_even=0
for i in range(x):
    arr.append(int(input()))
for j in arr:
    if j%2==0:
        c_even+=1
    else:
        c_odd+=1
print(f"The number of odd number is: {c_odd}")
print(f"The number od even number is: {c_even}")
