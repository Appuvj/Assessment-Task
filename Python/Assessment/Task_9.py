
#Write an application which copy content from one file to another(other file will be created from user)

import os
import shutil
import filecmp

def exchange(filename1,filename2):

    if(not os.path.exists(filename1)):
        print('file not found: ',filename1)
    elif(not os.path.exists(filename2)):
        print('file not found: ',filename2)
    else:
        copy=shutil.copyfile(filename1,filename2)
        print('the file has been successfully copied : ',copy)

        compare = filecmp.cmp(filename1,filename2)
        print('after comparing: ',compare)



def main():
    value_01=input('enter first file name: ')
    value_02=input('enter the second file name: ')

    exchange(value_01,value_02)


if __name__ == "__main__":
    main()
