
#strs = ['a','bb','ccc'] 
#max_len = 2
#def get_items_longer_than(strs, max_len):
#    corlist = []
#    for value in strs:
#        if len(value)>max_len:
#            corlist.append(value)
#    print(corlist)
#get_items_longer_than(strs, max_len)

def get_sandwich_filling(sandwich):
    # your code here
    dupelist = sandwich.copy()
    for value in dupelist: 
        if value == 'bread':
            dupelist.remove('bread')
    print(dupelist)
    return(dupelist)


get_sandwich_filling(["bread","bread"])

    