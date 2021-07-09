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
        print("Foute input!")
    print(st)

main()

def extra():
    x, y= input("wat is a?"), input("wat is b?")
    if (x < y):
        st = "a is kleiner!"
    elif (x == y):
        st = "a is gelijk!"
    elif (x > y):
        st = "a is groter!"
    else:
        st= "foute input!"
    print(st)
extra()



