import random


# def get_random_value():
#    return random.choice((1, 2, 3, 4, 5))


# def get_random_values(choices, size=2):
#    return random.choices(choices, k=size)

# def get_random_value():
#    return random.choice((1, 2, 3, 4, 5))
def repeat(n): #Допоміжна функція для розуміння логіки
    for i in range(n):
        print(2 * n)


def decorate(i): #Допоміжна функція для розуміння логіки
    def wrapper(func):
        def inner_wrapper(*args):
            for arg in range(i):
                print(func(arg) + arg)

        return inner_wrapper

    return wrapper


@decorate(5) #Допоміжна функція для розуміння логіки
def get_one(n):
    return n * 2


def retry(attempts=5, desired_value=None):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            out_of_attempts = True
            for arg in range(attempts):
                if len(args) > 0:
                    a = func(args[0])
                else:
                    a = func()
                if a == desired_value:
                    out_of_attempts = False
                    break

            if out_of_attempts:
                print('out of attempts')
            else:
                print(desired_value)
            return


        return inner_wrapper

    return wrapper


@retry(attempts=5, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))

@retry(attempts=5, desired_value=[1, 2, 3])
def get_random_values(choices, size=3):
    return random.choices(choices, k=size)



if __name__ == '__main__':
    print(get_random_value())
   # print(get_random_values((1, 2, 3, 1, 2)))
   # print(get_one(3))
   # print(repeat(5))

