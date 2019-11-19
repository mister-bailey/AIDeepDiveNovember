def convert_to_string(x):
    '''Converts argument to string'''
    return str(x)

def overlap(l1, l2):
    '''Returns overlapping elements'''
    list = [x for index, x in enumerate(l1) if x in l2 and l1.index(x) == index]
    if list == []: print("No overlap :)")
    return list

def make_pancakes(x):
    '''sets x[0] = \'pancakes\''''
    x[0] = 'pancakes'

