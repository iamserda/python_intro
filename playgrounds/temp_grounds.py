##rogue = list(range(0,10))
##accumulator = 0
##for item in rogue:
##    pre_id = id(rogue)
##    val, *rogue = rogue
##    accumulator += val
##    post_id = id(rogue)
##    print(accumulator, rogue, "is at same memory location:",pre_id == post_id)

# Welcome to Python World!
# return a list of the price for these items
items = [{"name": "Mango", "price": 1.26}, 
         {"name": "Apple", "price": 3.65}, 
         {"name": "Watermelon", "price": 4.31},
         {"name": "Mango", "price": 10}]

# Using programming fundamentals and intuition:
def get_price_values(some_list):
  local_list = list()
  for item in some_list:
    local_list.append(item["price"])
  return local_list

# Using functional programming intuition: map(...)
def get_price_with_lambda(some_list):
  return list(map(lambda item: item["price"], items))

def get_price_(some_list):
  def local_func(item):
    return item["price"]
  return list(map(local_func, items))

def test_():
    assert get_price_values(items) == [1.26, 3.65, 4.31, 10]
    assert get_price_with_lambda(items) == [1.26, 3.65, 4.31, 10]
    assert get_price_(items) == [1.26, 3.65, 4.31, 10]
    print("Test Passed!")

test_() # Passed!
