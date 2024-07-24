
def main():

    size=int(input('enter how many dishes you want to add in menu card : '))
    data_input=[]
    print('enter the dishes: ')
    for i in range(size):
        dishes=input()
        data_input.append(dishes)
    print('the dishes are : ',data_input)
    data_input=add(data_input)
    print('dish added successfully')
    print('the dishes are : ',data_input)
    data_input=update(data_input)
    print('the dishes are : ',data_input)
    data_input=remove(data_input)
    print('the dishes are : ',data_input)

print()

def add(data_input):
    
    print('Which starter you want to add in menu? ')
    add_dish=input()
    data_input.append(add_dish)
    return data_input

print()

def update(data_input):

    print('where you want to update : ')
    update_dish=input()
    if update_dish in data_input:
        new_value = input('enter new dish : ')
        index=data_input.index(update_dish)
        data_input[index] = new_value
        print(f'Updated {update_dish} to {new_value}.')
    else:
        print(f'Key {update_dish} not found in the data.')
    return data_input
print()

def remove(data_input):

    print('which dish you want to remove : ')
    remove_dish=input()
    data_input.remove(remove_dish)
    return data_input

if __name__ == "__main__":
    main()
