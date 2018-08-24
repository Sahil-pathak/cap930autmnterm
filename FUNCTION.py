def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
          print(i," is not prime")
        else:
             print(i," is  prime")
        
    
n=input("Enter a number")
is_prime(int(n))

    
        


