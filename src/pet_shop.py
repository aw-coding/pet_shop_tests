# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return shop["name"]


# 2

def get_total_cash(shop):
    return shop["admin"]['total_cash']

# 3

def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash

# 4

def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash

# 5

def get_pets_sold(shop):
    return shop["admin"]['pets_sold']

# 6 

def increase_pets_sold(shop, number):
    shop["admin"]['pets_sold'] += number

# 7

def get_stock_count(shop):
    return len(shop["pets"])


# 8

def get_pets_by_breed(shop, breed_desired):
    number_of_desired_breed = []
    for pet in shop["pets"]:
        if pet["breed"] == breed_desired:
            number_of_desired_breed.append(pet)
    return number_of_desired_breed

#9 is the same function

# 10

def find_pet_by_name(shop,name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet
        

# 11 same function

#12

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)
    #return

#13

def add_pet_to_stock(shop, pet_to_add):
    shop["pets"].append(pet_to_add)


#14 

def get_customer_cash(customer):
    return customer["cash"]

#15

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount 

#16 

def get_customer_pet_count(customer):
    return len(customer["pets"])

#17

def add_pet_to_customer(customer, pet_to_add):
    customer["pets"].append(pet_to_add)
    return len(customer["pets"])


# Optional no. 1

def customer_can_afford_pet(customer, pet_desired):
    if customer["cash"] >= pet_desired["price"]:
        return True
    else:
        return False


# Optional no. 2 - same function as above


# Optional no. 3 same as above


# Optional no. 4- integrations

def sell_pet_to_customer(shop, name, customer):
  #  find_pet_by_name(shop, pet)
    amount = 0

    if remove_pet_by_name(shop, name) != None:
        amount = name["price"]
        shop["admin"]["total_cash"] += amount   
        add_pet_to_customer(customer, name)
        shop["admin"]["pets_sold"] += 1
    
    get_customer_pet_count(customer)
    get_pets_sold(shop)
    remove_customer_cash(customer, amount)
    get_customer_cash(customer)




    get_total_cash(shop)

