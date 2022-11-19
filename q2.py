import doctest


def last_call(func):
    '''
    TESTS:
    >>> print(sum(1, 2))
    3
    >>> print(sum(num_1=5, num_2=5))
    10
    >>> print(sum(1, 2))
    These argument were given before! Result: 3
    >>> print(sum(num_1=5, num_2=5))
    These argument were given before! Result: 10
    '''
    # holds all given arguments for this function given in previous calls
    arguments_history = list()

    def wrapper(*args, **kwargs):
        # a list that holds each argument
        current_args = list()
        # extracting arguments from args
        for i in range(len(args)):
            current_args.append(args[i])
        # extracting arguments from kwargs
        for key, val in kwargs.items():
            current_args.append(val)
        # test wether the arguments were given before
        if current_args in arguments_history:
            return f'These argument were given before! Result: {func(*args, **kwargs)}'

        # if no such call - add current result to cache and return it.
        else:
            arguments_history.append(current_args)
            return func(*args, **kwargs)

    return wrapper


@last_call
def sum(num_1, num_2):
    return num_1 + num_2


if __name__ == '__main__':
    doctest.testmod()
