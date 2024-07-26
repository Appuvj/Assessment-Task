# to remove or delete the file 

import os

def delete(filename):

    if(not os.path.exists(filename)):
        print('file not exist : ',filename)
    
    else:
        delete=os.remove(filename)
        print(f'the selected {filename} is deleted',delete)


def main():
    file=input("enter the file name which you want to delete : ")
    delete(file)


if __name__ == "__main__":
    main()