#THIS IS A CALCULATOR, MADE BY USING FUNCTIONS,WHILE LOOP,TRY AND EXCEPT.

def add(a,b):
    return(a+b)
def sub(a,b):
    return (a-b)    
def mul(a,b):
    return (a*b)    
def div(a,b):
    return (a/b)  
def mod(a,b):
   return(a%b)  
def pwr(a,b):
   return(a**b)   

while True:
  try:
    a=int(input("Enter 1st number : "))
    b=int(input("Enter 2nd number : "))
    if(a==0 or  b==0):
        print("Enter a valid number !")  
        continue  
    c=input("Which operation you wanna perform : +,-,*,/,**,% ")
    if(c=="+"):
      print(f"Result is : {add(a,b)}")
    elif(c=="-"):
      print(f"Result is : {sub(a,b)}")
    elif(c=="*"):
      print(f"Result is :{mul(a,b)}")  
    elif(c=="/"):
      print(f"Result is : {div(a,b)}") 
    elif(c=="**"):
      print(f"Result is : {pwr(a,b)}")  
    elif(c=="%"):
      print(f"Result is : {mod(a,b)}")
    else:
       print("Enter valid operation !")  
    
  except Exception as e:
    print(e)
  d=input("Do you wanna continue : yes/no ")  
  if d=="no":
    break
print("Thank you!")  
     
        
    


    