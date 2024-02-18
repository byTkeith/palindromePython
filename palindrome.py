# programme that prints outs palidrome sentences
# Tendai K Nyevedzanai
# NYVTEN001
# 27 April 2022


def palindrome_func(user_input):
    if len(user_input)==0 or len(user_input)==1:
        return True
    elif user_input[0]==user_input[-1]:
        return palindrome_func(user_input[1:-1] ) 
    else:
        return False
   
                              
user_input=input("Enter a string:\n")#  search from first to last of the string
    

# call the function 
# palindrome_func(user_input)

# check for the values 
if palindrome_func(user_input):
    #return True
    print("Palindrome!")
else:
    #return False
    print("Not a palindrome!")