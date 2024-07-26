# append the text in the txt file

import os

def add(file):

    if (not os.path.exists(file)):
        print('file not exist')
    else:
        extra=input('enter the test you have appended in the file : ')
        append_file=open(file,'a')
        append_file.writelines([extra])
        print('done')



def main():
    file=input('Enter the file you want to append : ')
    add(file)


if __name__ == "__main__":
    main()