from sys import getsizeof

# Accessing a list:
my_list = list(range(20))

def print_list(my_list:list)->None:
    print("list:", my_list[:10:-1])  # reverses the string, then prints the first half of the reversed string.
    print("list:", my_list[10::-1])  #reverses the string, then prints the 2nd half of the reversed string.
    print("list:", my_list)
    print("list:", my_list[::-1]) # print list, reversed.
    print("list:", my_list[:10])  # print first half
    print("list:", my_list[10:])  # prints second half
    print("list:", my_list[::2])  # prints 
    print("list:", my_list[::-2]) # prints

my_list = list("Hello, welcome to Python World!")

def list_unpacking(my_list:list)->str:
    if my_list and len(my_list) == 3:
        first, last, house = my_list
        return f"{first.title()} {last.title()} is from {house}."
    return ""

def list_unpacking_2(my_list):
    if my_list and len(my_list) >= 2:
        val1, val2, *other_values = my_list
        my_tuple = tuple([val1, val2, other_values])
        return my_tuple
    return None

def list_unpacking_test():
    got_ = []
    assert list_unpacking(got_) == ""
    
    got_ = ["jon","snow", "House Stark"]
    assert list_unpacking(got_) == "Jon Snow is from House Stark."
    
    got_ = ["Serda","Simus", "Simus Capital"]
    assert list_unpacking(got_) == f"{got_[0]} {got_[1]} is from {got_[2]}."
    
    got_ = ["jon","snow", "House Stark"]
    assert list_unpacking(got_) == "Jon Snow is from House Stark."
    
    print("Test Status: Passed!")


# list_unpacking_test()

def list_unpacking_test2():
    got_ = []
    assert list_unpacking_2(got_) == None
    
    got_ = ["jon","snow", "House Stark"]
    assert list_unpacking_2(got_) == ("jon", "snow",["House Stark"])
    
    got_ = ["Serda","Sloan"]
    assert list_unpacking_2(got_) == ("Serda", "Sloan", [])
    
    got_ = ["jon"]
    assert list_unpacking_2(got_) == None

def print_items_in_list(my_list:list):
    if my_list:
        for my_tuple in enumerate( my_list):
            index, item = my_tuple
            print(f"{index}: {item}")
            print(my_tuple)

# print_items_in_list(list("Welcome to Python World!"))

# list comprehension
def using_list_comprehension():
    """ Filtering a list using List Comprehension"""
    my_list = list(range(1,10))
    gt_five = [x for x in my_list if x > 5] # 6, 7, 8, 9
    lt_five = [x for x in my_list if x < 5] # 6, 7, 8, 9
    print("My List:", my_list)
    print("Greater than 5: ", gt_five)
    print("Less than 5: ", lt_five)

# using_list_comprehension()


# zip
def using_zip_func():
    a_list = [1,2,3]
    b_list = [4,5,6]
    c = list(zip(a_list, b_list)) # [(1, 4), (2, 5), (3, 6)]
    return c

# using_zip_func()


def using_sets():
    """sets() -> collection of unique values {1, 2, 5, 10}
    sets() are unordered collection, cannot access any item by an index."""
    a_list = [1,2,3]
    b_list = [x**2 for x in a_list]
    _set1 =set(a_list).union({9,5})
    _set2 = {2, 3, 9}.union(set(b_list))
    print("Set1", _set1)
    print("Set2", _set2)

    """ COMMON USAGE of SETS DS in Python:
    UNION | combination of the unique items in set1 and set2.
    If there are duplicates, the common items ONLY show up ONCE.
    That's because we get back a new set, and sets don't allow duplicates."""
    _set3 = _set1 | _set2
    print(f"union(|): {_set1} | {_set2}:",_set3)

    """ INTERSECTION | items that are in both set1 and set2 """
    _set3 = _set1 & _set2
    print(f"intrsct(^): {_set1} & {_set2}:", _set3)

    # DIFF | items that are in both set1 and set2
    _set3 = _set1 - _set2
    print(f"diff(-): {_set1} - {_set2}:", _set3)

    # SYMETRIC DIFF | all items that are exclusively in a set and not common to both.
    _set3 = _set1 ^ _set2
    print(f"sym-diff: {_set1} ^ {_set2}:",_set3)
# using_zip()


# tuples -> a list that cannot be modified later(constant)
def using_tuples():
    _tuple1 = (1,2,3,3,4) # packing
    _tuple2 = 12,3,40,14 # packing
    _tuple3 = _tuple1 + _tuple2 # combining
    print(_tuple1, type(_tuple1))
    print(_tuple2, type(_tuple2))
    print(_tuple3, type(_tuple3))
    
    # unpacking and *packing
    item1,item2,*_tuple1 = _tuple1 # unpacking
    # _tuple1 = tuple(_tuple1)
    print(item1, item2, _tuple1) # 1, 2, (3,3,4,12,3,40,14)
    print(type(item1),type( item2), type(_tuple1))

# using_tuples()


def using_generators_func():
    """ gen_func()
    generators, cannot provide their current lengths.
    generators are great when you do not need to preallocated or access by index."""
    
    gen_obj1 = (x for x in range(100))
    print("sizeof gen1:100:", getsizeof(gen_obj1), "bytes.")
    
    gen_obj2 = (x for x in range(10000))
    print("sizeof gen2:10000:", getsizeof(gen_obj2), "bytes.")
    
    gen_obj3 = (x for x in range(100000000))
    print("sizeof gen3:100000000:", getsizeof(gen_obj3), "bytes.")

    list_obj1 = list(gen_obj1)
    print("sizeof list1:100:", getsizeof(list_obj1), "bytes.")

    list_obj2 = list(gen_obj2)
    print("sizeof list1:10,000:", getsizeof(list_obj2), "bytes.")

    list_obj3 = list(gen_obj3)
    print("sizeof list1:100,000,000:", getsizeof(list_obj3), "bytes.")

# using_generators_func() # test func

# array -> collection of single data types.
def using_cpython_array():
    from array import array
    _arr1 = array("I", [1,2,3,4,5])
    _arr2 = array("I", [5,6,7,8,9])
    print(f"_arr1: {_arr1} is of type {type(_arr1)}")
    print(f"_arr2: {_arr2} is of type {type(_arr2)}")
    _arr3 = _arr1 + _arr2
    print(f"_arr3: {_arr3} is of type {type(_arr3)}")

# using_cpython_array()


# generator object: great for when we have a long list of data, 
# benefits is that it DOES NOT preallocated all the memory needed at once.

# stacks -> LIFO data structure -> list() is good for this.

# queue() -> FIFO data structure. -> queue(list()) to create a empty queue