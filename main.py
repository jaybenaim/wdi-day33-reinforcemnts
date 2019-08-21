
def longestConsecutive(strings, k): 
    # s = strings[0].split(' ') 
    strings_list = [] 
    new_list = [] 
    for i in range(len(strings)): 
        if len(strings[i]) > len(strings[i-1]):
            strings_list.append(strings[i] * k) 
    for s in range(k): 

        return  strings_list[s] 
            
        
print(longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3) )
print(longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))
