
#strs = ['a','bb','ccc'] 
#max_len = 2
#def get_items_longer_than(strs, max_len):
#    corlist = []
#    for value in strs:
#        if len(value)>max_len:
#            corlist.append(value)
#    print(corlist)
#get_items_longer_than(strs, max_len)

#def get_sandwich_filling(sandwich):
    # your code here
#    dupelist = sandwich.copy()
#    for value in sandwich: 
#        if value == 'bread':
#            dupelist.remove('bread')
#    print(dupelist)
#    return(dupelist)

#get_sandwich_filling(["bread","bread"])

#def remove_item(items, n):
#    newremove_item = items.copy()
#    newremove_item.pop(n)
#    print(items)
#    print(newremove_item)

#remove_item([1, 2, 1, 2, 1], 2)
    
#def merge_lists(list1, list2):
#    merged = list1+list2 
#    print(merged)


#merge_lists([1], [2]) == [1, 2]

#def is_item_omnipresent(lists, item):
#    for value in lists:
#        if item in value:
#            state = bool(True)
#        else:
#            state = bool(False)
#    print(state)
#is_item_omnipresent([[1], [2]], 1)

def flatten_list_by_one(nested_lists):
    new = []
    for value in nested_lists: 
        new.extend(value)
    print(new)

flatten_list_by_one([[1], [2]]) == [1, 2]   
    