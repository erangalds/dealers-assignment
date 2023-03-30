# Defining a function read the dealers file and return a list

def read_dealers(dealer_file_name):
    with open(dealer_file_name, 'r') as f:
        temp_dealers = f.readlines()[1:]

    dealers = list()

    for dealer in temp_dealers:
        dealers.append( dealer.replace('\n', '').split(',')) 

    return dealers

# Defining a function read the products of dealers from the file and return a list

def read_dealers_products(dealer_products_file_name):
    with open(dealer_products_file_name, 'r') as f:
        temp_dealers_products = f.readlines()[1:]

    dealers_products = list()

    for dealer_products in temp_dealers_products:
        dealers_products.append( dealer_products.replace('\n', '').split(',')) 

    return dealers_products

## Defining a funtion to select 4 dealers from the list randomly\
def select_dealers(dealers, number_of_dealers):
    import random 

    random_number_list = list()
    #print('Current random numbe list: ', random_number_list)
    #print('Given number of dealers : ', number_of_dealers)

    for number_of_dealer in range(number_of_dealers):

        #print('Current Dealer Number: ',number_of_dealer)

        while True:
            #print(len(dealers))
            random_number = random.randint(0,len(dealers)-1)

            if random_number not in random_number_list:
                random_number_list.append(random_number)
                break
            else:
                continue

    # Selected Dealers 
    selected_dealers = list()

    #print(random_number_list)

    for random_number in random_number_list:
        selected_dealers.append(dealers[random_number])

    #print('Full Dealer list ')
    #print(dealers)
    
    #print(random_number_list)
    #print('Selected Dealers')
    #print(selected_dealers)

    return selected_dealers


# Defining a function to display the products of a dealer
def display_products_of_dealer(selected_dealers, dealer_products_list):

    selected_dealer_products = list()

    for dealer in selected_dealers:
        dealer_name = dealer[0]

        for dealer_products in dealer_products_list:
            if dealer_name == dealer_products[0]:
                selected_dealer_products.append(dealer_products)
                print('Dealer Name: ', dealer_name, ' Brand:', dealer_products[1], ' Price: ', dealer_products[2], ' Quantity: ', dealer_products[3])

    print(selected_dealer_products)

def display_products_of_dealer_using_dealer_class(selected_dealer, dealer_products_list):

    selected_dealer_products = list()

    dealer_name = selected_dealer.name

    for dealer_products in dealer_products_list:
        if dealer_name == dealer_products[0]:
            selected_dealer_products.append(dealer_products)
            print('Dealer Name: ', dealer_name, ' Brand:', dealer_products[1], ' Price: ', dealer_products[2], ' Quantity: ', dealer_products[3])

    print(selected_dealer_products)

def sorting_dealer_based_on_location(dealers):

    sorted_location_list = list()
    dealer_count = len(dealers)

    for x in range(dealer_count):

        if x == 0:
            print('First Iteration')
        for index, dealer in enumerate(dealers):

            if index == 0:
                print('First Iteration')

                max_location = dealer[2]
                continue 
            else:
                if max_location <= dealer[2]:
                    max_location = dealer[2]
                    continue


def calling_inside_class():
    print('Hey this is calling a function in the module from the class')