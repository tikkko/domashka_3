
def print_square_wrong(n):  #Допоміжна функція для розуміння логіки
    if n == 1:
        print('*')
    else:
        print('*' * n)
        for i in range(n - 2):
            print('*' + (' ' * (n-2)) + '*')
        print('*' * n)




def print_square(n, i = 0):
    if n < 1 or n > 220:
        print('Please write the correct parameter - n. In range [1 - 220]')
        return
    if i == 0:
        i = n
        if i == 1:
            print('*')
            return
        n = (n - 2)
        print('*' * i)
    if n <= 1:
        if n == 1:
            print('*' + (' ' * (i - 2)) + '*')
        print('*' * i)
    else:
        print('*' + (' ' * (i-2)) + '*')
        print_square(n - 1, i)


if __name__ == '__main__':
    #print(print_square(4))
    #print(raw_square(4, 1))
    print_square(221)

