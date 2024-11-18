

def q1(): 
  #Write Assignment code here
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: ")) 
  num3 = int(input("Enter the third number: ")) 

   if num1 <= num2:
     if num1 <= num3: 
       smallest = num1
     else: 
       smallest = num3 
   else:
     if num2 <= num3:
       smallest = num3 
     else: 
       smallest = num3 
   print("The smallest number is:", smallest)    

def q2(): 
  #Write Assignment code here



#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
