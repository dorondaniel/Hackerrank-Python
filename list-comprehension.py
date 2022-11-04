if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    N = int(input()) #gets inputs
    
    arr = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k !=N]
    
    #the above line creates a nested list
    #[i,j,k] are going to be the temporary process variables
    #the loops assigns the value to the respective variable from the range of 0 to <inp>+1
    #all the loops are nested as i{j{k}}
    #if all loops are true it computes i + j + k !=N
    #if the condition is true then the respected values are appended to the nested array and until the range of loop becomes false the main array will get appended with nests
    
    print(arr) #prints the array
