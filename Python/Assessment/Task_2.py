
def main():

    size=int(input('enter the size: '))
    result_1=[]

    for i in range(size):
        value=int(input())

        result_1.append(value)
    print(result_1)
    addition(result_1)
    max(result_1)

    
def addition(result_1):

    sum=0

    for index in result_1:
        sum+=index
    print(sum)

def max(result_1):

    maximum=0

    for maxi in result_1:

        if(maximum<maxi):
            maximum=maxi
    print(maximum)










if __name__ == "__main__":
    main()
