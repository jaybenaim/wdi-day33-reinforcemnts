
def longestConsecutive(strings, k): 
    # s = strings[0].split(' ') 
    strings_list = [] 
    new_list = [] 
    
    for i in range(len(strings)): 
        if len(strings[i] ) > len(strings[i-1]):
            for s in range(k): 
                strings_list.append(strings[i+s]) 
            
            seperator = ''

            return  seperator.join(strings_list)




long1 = longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3) 
print(long1)
print(longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))

# print(seperator.join(long1))




