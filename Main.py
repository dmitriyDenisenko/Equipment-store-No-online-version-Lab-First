import ProductNotExist
import UserBankError
from User import User
from Product import Product
from TechProduct import TechProduct
from MoneyRepository import MoneyRepository
from ProductsRepository import ProductsRepository
from desir import SerializingMan


def input_number():
    while True:
        numb = input()
        if numb not in "1234567890":
            print("Common, its not Id... Try again")
        else:
            return int(numb)

def get_type():
    print("Whats type?")
    while (True):
        print("1 - LIFE_TECHNIQUE")
        print("2 - PHONES")
        print("3 - TVS")
        print("4 - COMPUTERS")
        print("5 - OFFICE")
        print("6 - LEISURE")
        print("7 - INSTRUMENT")
        print("8 - CONSTRUCTION")
        print("9 - HOUSEHOLD_PRODUCTS")
        print("10 - AUTO_PRODUCTS")
        print("11 - ACCESSORIES")
        choose = input()
        if choose == "1":
            return TechProduct.LIFE_TECHNIQUE
        elif choose == "2":
            return TechProduct.PHONES
        elif choose == "3":
            return TechProduct.TVS
        elif choose == "4":
            return  TechProduct.COMPUTERS
        elif choose == "5":
            return TechProduct.OFFICE
        elif choose == "6":
            return TechProduct.LEISURE
        elif choose == "7":
            return TechProduct.INSTRUMENT
        elif choose == "8":
            return TechProduct.CONSTRUCTION
        elif choose == "9":
            return TechProduct.HOUSEHOLD_PRODUCTS
        elif choose == "10":
            return TechProduct.AUTO_PRODUCTS
        elif choose == "11":
            return TechProduct.ACCESSORIES
        else:
            print("Choose TYPE!")


man = SerializingMan()
products = [Product(1, "Tv - 1", "Some des", TechProduct.TVS, 19999.99),
            Product(1, "Tv - 1", "Some des", TechProduct.TVS, 19999.99),
            Product(1, "Tv - 1", "Some des", TechProduct.TVS, 19999.99),
            Product(1, "Tv - 1", "Some des", TechProduct.TVS, 19999.99),
            Product(2, "iPhone - 2", "Some des", TechProduct.PHONES, 59999.99),
            Product(3, "Chainsaw - 3", "Some des", TechProduct.HOUSEHOLD_PRODUCTS, 29999.99),
            Product(3, "Chainsaw - 3", "Some des", TechProduct.HOUSEHOLD_PRODUCTS, 29999.99),
            Product(4, "Vape - 4", "Charon baby))", TechProduct.LIFE_TECHNIQUE, 69999.99),
            Product(4, "Vape - 4", "Some des", TechProduct.LIFE_TECHNIQUE, 69999.99),
            Product(5, "Monitor - 5", "Some des", TechProduct.COMPUTERS, 89999.99),
            Product(5, "Monitor - 5", "Some des", TechProduct.COMPUTERS, 89999.99),
            Product(5, "Monitor - 5", "Some des", TechProduct.COMPUTERS, 89999.99),
            Product(6, "Fridge - 6", "Some des", TechProduct.LIFE_TECHNIQUE, 99999.99),
            Product(7, "Electric tooth count - 7", "Some des", TechProduct.LIFE_TECHNIQUE, 9999.99)]

mvidio = man.deserial_json(MoneyRepository, "MoneyRepository")
store = ProductsRepository(products)
#store = man.deserial_xml(ProductsRepository, "ProductsRepository").desireal_products()
#man.serial_xml(store)
user = man.deserial_json(User, "User")
#man.serial_json(user)
print("Hello! Let's start our program")
print("You have ", user.get_bank())
print("In Store u can buy :")
print("What u want?")
while (True):
    print("1 - Put on checkout")
    print("2 - Put back product")
    print("3 - Buy")
    print("4 - Add product (if u manager)")
    print("5 - Save all")
    print("0 - Go away from MVIDIO")
    answer = input("Answer: ")
    if answer == "1":
        print("What put on?")
        product_id = input_number()
        user.add_product(product_id, store)
    elif answer == "2":
        print("What put back")
        product_id = input_number()
        try:
            user.remove_product(product_id, store)
        except ProductNotExist as err:
            print(err)
    elif answer == "3":
        try:
            user.make_buy(mvidio)
            print("WOW! Thanks!! Your bank: ", user.get_bank())
        except UserBankError as err:
            print(err)
    elif answer == "4":
        name = input("Name: ")
        des = input("Description: ")
        type = get_type()
        price = float(input("Price: "))
        store.add_product(Product(name,des,type,price))
    elif answer == "5":
        man.serial_json(store)
        man.serial_json(mvidio)
        man.serial_xml(user)
    elif answer == "0":
        exit()
    else:
        print("NEEED COMAND")
