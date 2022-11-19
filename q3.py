import doctest
'''
    This class adds the ability to access multi-level array indexes.
'''


class List(list):
    '''
    TESTS:
    >>> my_list = List([ [[1,2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]] ])

    >>> print(my_list[0])
    [[1, 2, 3, 33], [4, 5, 6, 66]]
    >>> print(my_list[0,1,3]) 
    66
    '''

    '''
        Constructor
    '''
    def init(self, *args):
        super(List, self).__init__(*args)

    '''
        Overload [] operator - allowing access to a layers within layers.
    '''
    def __getitem__(self, index):
        # if received index is a tuple - meaning a multi-levels access is required
        if isinstance(index, tuple):
            init = index[0]
            remain_index = index[1:]
            # create a new List with the upper layer of the wanted element
            ans = super(List, self).__getitem__(init)
            # go layer by layer until the wanted element is found
            for i in remain_index:
                ans = ans[i]
            return ans
        # if the given index is for single-layered list - same as list behavior
        return super(List, self).__getitem__(index)

if __name__ == '__main__':
    doctest.testmod()
