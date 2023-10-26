def print_item(name, price_in_pennies):
    formatted_price = '£{:.2f}'.format(price_in_pennies / 100.0)
    print('Item: ' + name)
    print('Price: ' + formatted_price)
 
print_item('Milk', 85)
print_item('Coffee', 249)
print_item('Orange Juice', 110)