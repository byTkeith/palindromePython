# programme that finds palidromic primes between two numbers
# Tendai K Nyevedzanai
# NYVTEN001
# 29 March 2022

import sys
sys.setrecursionlimit (30000)


def isPrime(number):
    
   if (2**number-1)%number==1:
      return True
   else:
      return False
   
def palindrome_func(user_input):
   if len(user_input)==0 or len(user_input)==1 :
      return True
   elif user_input[0]==user_input[-1]:
      return palindrome_func(user_input[1:-1] ) 
   else:
      return False
   
def palindrome_func(string):
   number=str(string)
   if len(number)<=1:
      return True
   else:
      return number[0]==number[-1] and palindrome_func(number[1:-1])
 

   
# Function check if the number Prime is Palindrome or not
def pali_prime(startnum, endnum):
      
   if startnum>endnum:
      return False
   if isPrime(startnum)==True:
       
      if palindrome_func(str(startnum))==True:

               
         print(startnum)

      return pali_prime(int(startnum)+1,endnum)
       
   else:

      return pali_prime(startnum+1, endnum)
def main():
   
   startnum = int(input('Enter the starting point N: \n'))
   endnum = int(input('Enter the ending point M: \n'))
        
   print('The palindromic primes are:')
   pali_prime(startnum, endnum)
   
if __name__=="__main__":
   main()
   