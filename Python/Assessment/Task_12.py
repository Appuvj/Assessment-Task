# compare and remove


import os
import filecmp

def com_rem(filename1,filename2):

    if(not os.path.exists(filename1)):
        print('file not exist')
    elif(not os.path.exists(filename2)):
        print('file not exist')
    
    else:
        compare=filecmp.cmp(filename1,filename2)
        print('after comparing : ',compare)

        if compare == True:
            os.remove(filename1)
            print(f'{filename1} deleted successfully')



def main():
    file1=input('enter the fisrt file name: ')
    file2=input('enter the second file name: ')
    com_rem(file1,file2)

if __name__ == "__main__":
    main()
