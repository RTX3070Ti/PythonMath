import math
print("Wat is groter wat is kleiner machine!")

def main():
    x, y= input("X= "), input("Y= ")
    if (x < y):
        st = "x is less than Y"
    elif (x == y):
        st = "x is the same as y"
    elif (x > y):
        st = "x is greater than y"
    else:
        print("Wrong Input!")
    print(st)

main()

def extra():
    x, y= input("what is a?"), input("what is b?")
    if (x < y):
        st = "a is less than b!"
    elif (x == y):
        st = "a is the same as b!"
    elif (x > y):
        st = "a is greater than b!"
    else:
        st= "Wrong input!"
    print(st)
extra()



