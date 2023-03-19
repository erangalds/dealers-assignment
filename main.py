## This is the main app
from modules import my_functions as my_f

dealers_file_name = 'dealer.txt'
dealers_products_file_name = 'products.txt'
dealers = my_f.read_dealers(dealer_file_name=dealers_file_name)
dealers_products = my_f.read_dealers_products(dealers_products_file_name)


print(dealers)
print(dealers_products)

selected_dealers = my_f.select_dealers(dealers, 4)

print(selected_dealers)

my_f.display_products_of_dealer(selected_dealers, dealers_products)

