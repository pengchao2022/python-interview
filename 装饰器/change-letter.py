def decrator(func):
    def wrapper(s):
        s = s[0].upper() + s[1:].lower()
        func(s)
        
    return wrapper


@decrator
def my_app(name):
    print(f"Hello, {name}")



my_app('kate')


