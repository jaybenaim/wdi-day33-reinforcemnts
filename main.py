
def longestConsecutive(strings, k): 
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


def longestInRow(strings, k): 
    items = []
    new_list = [] 
    for list_item_index, list_item in enumerate(strings):
        if list_item not in items: 
            items.append(list_item)

    items.sort(key=len, reverse=True) 
    new_list = items[:k]
    new_list = list(new_list)
    new_list = ''.join(new_list)

    return new_list

     
  
print(longestInRow(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3))
print(longestInRow(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))

