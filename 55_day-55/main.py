# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        fn = function.__name__
        arg = ",".join(map(str, args))
        print(f"You called {fn}({arg})")
        result = function(*args)
        print(f"It returned: {result}")
        return result
    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


s = a_function(1, 2, 3)
print(s)