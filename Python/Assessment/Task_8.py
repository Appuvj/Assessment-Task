import Task_8_arithmatic

def condition(select, num01, num02, operations):
    if select in operations:
        operation_name, operation_func = operations[select]
        Ans = operation_func(num01, num02)
        print(f'{operation_name} of {num01} and {num02}: {Ans}')
    else:
        print('Invalid choice. Please select 1, 2, or 3.')

def main():
    print()
    print('Mathematical Calculation')
    print()
    print('1. Addition\n2. Subtraction\n3. Multiplication')
    print()
    select = int(input('Select 1/2/3 for Calculation: '))
    print()
    num01 = int(input('Enter first number: '))
    num02 = int(input('Enter second number: '))
    print()

    operations = {
        1: ('Addition', Task_8_arithmatic.addition),
        2: ('Subtraction', Task_8_arithmatic.subtraction),
        3: ('Multiplication', Task_8_arithmatic.multiplication)
    }

    condition(select, num01, num02, operations)

if __name__ == "__main__":
    main()
