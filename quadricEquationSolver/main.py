from numpy import sqrt
print("You have an equation ax^2 +bx+c = 0")
def getOngetOnlyNumlyNum(num):    
    while 1:
        try:
            return int(input(num+" = "))
            break
        except ValueError:
            print("Enter a number")
            continue
a = getOngetOnlyNumlyNum('A')
b = getOngetOnlyNumlyNum('B')
c = getOngetOnlyNumlyNum('C')

if a ==0:
    print('This is not Quadric Formula')
    b = 0
    c = 0
    a = 1
x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
print("x1 = "+str(x1))
print("x2 = "+str(x2))




