n = 2
print(type(n))
n= 4.99
print(type(n))
n = (2 + 5j)
print(type(n))
n = "235"
print(type(n))

# or
num = input()
if num == "0":
    print("The number is zero")
elif "." in num:
    print("It is a floating value")
elif "+" in num:
    print("it is a complex value")
elif num.isdecimal():
    print("It is a real number")
else:
    print("entered value is a string")