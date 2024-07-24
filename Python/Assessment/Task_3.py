def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

def main():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    print('1.add\n2.sub\n3.mul\n4.div')

    choice=int(input("Enter the choice: "))
    if choice == 1:
        print("The Addition of",a,"and",b,"is",add(a,b))
    elif choice == 2:
        print("The Subtraction of",a,"and",b,"is",sub(a,b))
    elif choice == 3:
        print("The Subtraction of",a,"and",b,"is",sub(a,b))
    elif choice == 4:
        print("The Subtraction of",a,"and",b,"is",div(a,b))
    else:
        print("pls enter correct choice.")
        
if __name__ == "__main__":
    main()
    