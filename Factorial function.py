def factorial_func(n):
    if n < 0 :
        return None
    if n < 2:
        return 1
    
    else:
        product = 1
        
        for i in range (1, n+1) :
            
            product *= i
        
        return product
        
for n in range (1,12):
    print(f"{n}! =   {factorial_func(n)}")