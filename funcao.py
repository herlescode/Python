def outer_function(x):
    y = x + 5
    
    def inner_function():
        z = y * 2        
        print(z)
        
    inner_function()
    
    print(y)
    
outer_function(10)