def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

# first star is implemented,then func completes the percent func
# and then completes the star function

@star
@percent
def printer(msg):
    print(msg)


printer("Hello")