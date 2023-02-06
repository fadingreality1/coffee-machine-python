MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 30,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 70,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0,
}

def add():
    """To add more resources after resources have empties out or before"""
    resources['water'] += int(input("How much water to add (in ml): "))
    resources['milk'] += int(input("How much milk to add (in ml): "))
    resources['coffee'] += int(input("How much coffee to add (in g): "))
    start()

def adjust(a):
    """to adjust resources after every transaction"""
    resources['water'] =  resources['water'] - MENU[a]['ingredients']['water']
    resources['milk'] =  resources['milk'] - MENU[a]['ingredients']['milk']
    resources['coffee'] =  resources['coffee'] - MENU[a]['ingredients']['coffee']
    resources['money'] += MENU[a]['cost']
    start()

def check_resources(a):
    """to check if resources are enough for perticular drink or not"""
    for i in resources:
        if MENU[a]['ingredients'][i] > resources[i]:
            print(f"{i} is not enough.")
            start()
        else:
            get_coin(a)
    
def get_coin(a):
    """To Take money and process the Drink and give back change,
        have to call update_resources too
    """
    print("Please insert money.")
    m5 = int(input("How many 5₹ coins: "))
    m10 = int(input("How many 10₹ coins: "))
    m20 = int(input("How many 20₹ coins: "))
    if(m5 * 5 + m10 *10 + m20 *20) < MENU[a]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        start()
    elif (m5 * 5 + m10 *10 + m20 *20) == MENU[a]['cost']:
        print(f"Here is your {a}. enjoy!")
        adjust(a)
    else:
        print(f"Here is ₹{(m5 * 5 + m10 *10 + m20 *20 ) - MENU[a]['cost']} change.")
        print(f"Here is your {a}. enjoy!")
        adjust(a)
    
def report():
    """Have to print report about current resources and money and print it the call start again"""
    print(f"Water = {resources['water']}ml\nMilk = {resources['milk']}ml\nCoffee = {resources['coffee']}g\nMoney = {resources['money']}₹")
    start()

def off():
    """To turn off coffee machine"""
    r = input("press enter to exit")
    exit()

def start():
    """Main game module"""
    ch = input("What would you like? \nespresso 30₹ \nlatte 50₹ \ncappuccino 70₹ :").lower()
    
    while ch == '' or not(ch == 'espresso' or ch == 'latte' or ch == 'cappuccino' or ch == 'report' or ch == 'off' or ch =='add') :
        ch = input().lower()
    
    if ch == 'report':
        report()
    elif ch == 'off':
        off()
    elif ch == 'add':
        add()
    else :
        check_resources(ch)
        
start()