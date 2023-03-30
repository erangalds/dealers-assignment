## This is the main app
from modules import my_functions as my_f

dealers_file_name = 'dealer.txt'
dealers_products_file_name = 'products.txt'
dealers = my_f.read_dealers(dealer_file_name=dealers_file_name)
dealers_products = my_f.read_dealers_products(dealers_products_file_name)


#print(dealers)
#print(dealers_products)

selected_dealers = my_f.select_dealers(dealers, 4)

#print(selected_dealers)

my_f.display_products_of_dealer(selected_dealers, dealers_products)

class dealer():
    from modules import my_functions as f

    name = None
    contact_number = None 
    location = None 

    def __init__(self, name, contact_number, location):
        self.name = name 
        self.contact_number = contact_number 
        self.location = location

    def call_module_functions(self):
        self.f.calling_inside_class()

    def dealers_products(self):
    
        with open('products.txt', 'r') as f:
            temp_dealers_products = f.readlines()[1:]

        dealers_products = list()

        for dealer_products in temp_dealers_products:
            dealers_products.append( dealer_products.replace('\n', '').split(',')) 

        selected_dealer_products = list()

        dealer_name = self.name

        for dealer_products in dealers_products:
            if dealer_name == dealer_products[0]:
                selected_dealer_products.append(dealer_products)
                print('Dealer Name: ', dealer_name, ' Brand:', dealer_products[1], ' Price: ', dealer_products[2], ' Quantity: ', dealer_products[3])

        #print(selected_dealer_products)

for selected_dealer in selected_dealers:
    d = dealer(selected_dealer[0], selected_dealer[1], selected_dealer[2])

    print('Dealer Name : ', d.name)
    print('Dealer Contact Number : ', d.contact_number)
    print('Dealer Location : ', d.location)

    print('-------------------------')

    d.dealers_products()
    d.call_module_functions()


