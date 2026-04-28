#This is an example of me practising decorators in python which follow the onion order

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1 start")
        func()
        print("Decorator 1 end")
        return 
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2 start")
        func()
        print("Decorator 2 end")
        return 
    return wrapper

@decorator1
@decorator2
def main_func():
    print("Main function running!")

main_func()