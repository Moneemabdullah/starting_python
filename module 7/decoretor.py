def timer():
    def inner():
        print('time started')
        
        
        print('time ended')
        
    return inner


# timer()()
@timer
def factiorial():
    print('starting.')
    
    
    
factiorial()

