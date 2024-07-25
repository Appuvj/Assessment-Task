#    Create a Grade Calculator using Dictionary


def total(lst,grade):

    total=0
    for index in lst:
        total+=index
    print('the total is : ',total)

    if total>=450:
        print(f'the grade for the mark is: {grade[450]}')
    
    elif total>=370:
         print(f'the grade for the mark is: {grade[370]}')
    
    elif total>=250:
         print(f' the grade for the mark is: {grade[250]}')

    elif total>=130:
         print(f' the grade for the mark is: {grade[130]}')

    elif total>=0:
         print(f'the grade for the mark is: {grade[0]}')

    else:
        print('invalid score')


def main():

    grade={
        450:'A',
        370:'B',
        250:'C',
        130:'D',
        0:'E'
              }
    
    size=int(input('enter the size of marks : '))

    lst=[]
    print('enter the marks: ')

    for i in range(size):
        value=int(input())
        lst.append(value)
    print('the marks list is : ',lst)
    total(lst,grade)



if __name__ == "__main__":
    main()





