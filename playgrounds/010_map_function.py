# Welcome to Python World!
# return a list of the price for these items
items = [{"name": "Mango", "price": 11.26},
         {"name": "Apple", "price": 8.65},
         {"name": "Watermelon", "price": 4.31},
         {"name": "Orange", "price": 5.96}]

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
    assert get_price_values(items) == [11.26, 8.65, 4.31, 5.96]
    assert get_price_with_lambda(items)== [11.26, 8.65, 4.31, 5.96]
    assert get_price_(items) == [11.26, 8.65, 4.31, 5.96]
    print("Passed!")

test_() # Passed!