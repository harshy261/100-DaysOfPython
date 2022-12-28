# MATCHCASE STATEMENT

# Similar to Switch Case in C++
# Break is not compulsory in PYTHON


x = int(input("Enter the value of x: "))


match x:
    case 0:
        print("X is Zero")
    case 2:
        print("X is 2")
    case 4:
        print("X is 4")
    case 6:
        print("X is 6")
    case _ if x!=20:
        print("X is not 20")
    case _:
        print(x)