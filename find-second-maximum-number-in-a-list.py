if __name__ == '__main__':
    n = int(input()) #input
    
    arr = sorted(set(map(int, input().split()))) 
    print(arr[-2])
    
    #EXPLANATION
    """ the 4th line creates a array with the following functions applied
    the first one is map() function, it takes two params, it will append the value that is being fed by the user as a sequence of space seperated values
    the split() is used for spliting the values at the spaces
    the next function is set() which removes the repetition of the values
    and the final filter is sorted() it makes the array to be sorted # not that we use sorted instead of sort is map returns iterable values and not datatypes
    then for printing the second largest value we specify -2 as index"""
   
