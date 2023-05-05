# Welcome to Python World!
# return a list of the price for these items
items = [{"name": "Mango", "price": 1.26},
         {"name": "Apple", "price": 3.65},
         {"name": "Watermelon", "price": 4.31},
         {"name": "Mango", "price": 10}]

# problem: writer a function to return items with prices less than 7 dollars.


def cost_more_than(items, value):
    return list(filter(lambda x: (x["price"] > value), items))

# problem: writer a function to return items with prices more than 5 dollars.


def cost_less_than(items, value):
    return list(filter(lambda x: (x["price"] < value), items))


def test_():
    assert cost_less_than(items, 5) == [{"name": "Mango", "price": 1.26}, {
        "name": "Apple", "price": 3.65}, {"name": "Watermelon", "price": 4.31},]

    assert cost_more_than(items, 7) == [{"name": "Mango", "price": 10}]
    print("test: passed!")
    
test_()