a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))

if (a > b and a > c):
    print("a is Greatest")
elif(b > a and b > c):
    print("b is Greatest")
elif(c > a and c > b):
    print("c is Greatest")
elif(a == b and a > c):
    print("a & b are Greatest")
elif(b == c and b > a):
    print("b & c are Greatest")
elif(c == a and c > b):
    print("c & a are Greatest")
else:
    print("All are equals")