import re

def sumofin(a):
    c=len(a)
    s=0
    for i in range(c):
        s=s+int(a[i])
    print("sum of digits in entered input is :", s)


u=0
l=0
d=0
s=0
inp=input("enter the input: ")
print("entered input is",inp)
try:
    if inp.isdigit():
        print("input is int")
        if int(inp)%2==0:
            print("its even number")
        else:
            print("its odd number")
        sumofin(inp)
    else:
        b=float(inp)
        print(b)
        print("its float value")
except:
    print("its a string")
    print("length of the input is : ",len(inp))
    for i in inp:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
        elif i.isnumeric():
            d += 1
        else:
            s+=1
    if inp.isalnum():
        print("its alphanumeric")
    if inp.isupper()==True:
        print("its uppercase")
        #print("count of uppercase : ",len(inp))
    if inp.islower()==True:
        print("its lowercase")
        #print("count of lowercase : ", len(inp))
    if inp[0].isupper() and inp[1:].islower():
        print("its capitalize")

    if re.match("^[a-zA-Z0-9_]*$",inp):
        pass
    else:
        print("it contains special character")

    print("count of upperacase: ", u)
    print("count of lowercase: ", l)
    print("count of digits: ", d)
    print("count of special characters: ",s)
