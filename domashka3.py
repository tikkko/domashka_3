import random


# def get_random_value():
#    return random.choice((1, 2, 3, 4, 5))


# def get_random_values(choices, size=2):
#    return random.choices(choices, k=size)

def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


def retry(attempts=5, desired_value=None):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):

            for arg in args:
                if attempts > 5:
                    print('attempts limit reached')

            for arg in kwargs:
                if desired_value is not None:
                    print('true')

        return inner_wrapper

    return wrapper


@retry(desired_value=4)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))

# if __name__ == '__main__':
# get_random_value()
