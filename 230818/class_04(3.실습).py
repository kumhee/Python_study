def calc(a, *args):
    if a == "*":
        sum = 1 
        for arg in args:
            sum *= arg
        return sum
    elif a == "+":
        sum = 0
        for arg in args:
            sum += arg
        return sum

print(calc("+" , 1,2,3,4,5))
print(calc("*" , 1,2,3,4,5))


