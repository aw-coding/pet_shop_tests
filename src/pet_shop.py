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

def find_pet_by_name(list,name):
    for pet in list["pets"]:
        if pet["name"] == "name":
            return pet
        return "Not found."

# 11

