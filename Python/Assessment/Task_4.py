def frequency(str,letter):
    count=0
    for k in str:
        if(k==letter):
            count+=1
    return count

def main():
    str=input("Enter the str name:")
    letter=input("Enter the word to check:")
    count=frequency(str,letter)
    print(letter,"is repeating",count,"times")
    
if __name__=="__main__":
    main()