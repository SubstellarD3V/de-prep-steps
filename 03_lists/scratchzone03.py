
strs = ['a','bb','ccc'] 
max_len = 2
def get_items_longer_than(strs, max_len):
    corlist = []
    for value in strs:
        if len(value)>max_len:
            corlist.append(value)
    print(corlist)
get_items_longer_than(strs, max_len)
    
    