if __name__ == '__main__':
    lst = [] #list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score]) #appends a list into a list
    lst = sorted(lst, key = lambda x: x[1]) # sorts the list using the score value as key
    
    second_low_sorted_score = sorted(list(set([i[1] for i in lst])))[1] #stores the second least value by sorting the score values without repetition and takes the [1]th item of the array

    lst_second_low = [] #list to hold all the second lowest elements
    for x in lst:
        if x[1] == second_low_sorted_score: #if the score in the list lst equals the second_low_sorted_score
            lst_second_low.append(x[0]) # then pnly the name from the lst will be appended to the new lst_second_low list
            
    for x in sorted(lst_second_low):
        print(x) #prints the names
