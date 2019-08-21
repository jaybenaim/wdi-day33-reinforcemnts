
def longestConsecutive(strings, k): 
    # s = strings[0].split(' ') 
    strings_list = [] 
    for string_index, string in enumerate(strings): 
        # if len(string) > len(string[string_index]): 
        strings_list.append(string)
        
    for s in strings_list: 
        return s + s
    # for string in strings: 

print(longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3) )
# longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)

