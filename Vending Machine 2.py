class VendingMachine:
   def __init__(self):
        self.items = {
           1: {"name": "Coca Cola", "price": 1.50, "stock": 20},
           2: {"name": "Lays Chips", "price": 1.00, "stock": 19},
           3: {"name": "Reese's Chocolate", "price": 0.75, "stock": 23},
           4: {"name": "Lacnor Milk", "price": 0.75, "stock": 19},
           5: {"name": "Brownie", "price": 2.00, "stock": 15},
           6: {"name": "Boosting services by merrick (Valorant)", "price": 500.00, "stock": 1},
           7: {"name": "Bueno Kinder Chocolate", "price": 2.00, "stock": 25},
           8: {"name": "Cheese Sticks", "price": 3.00, "stock": 19},
           9: {"name": "Sting Drink", "price": 2.50, "stock": 21},
           10: {"name": "Red Bull", "price": 6.00, "stock": 19},
           11: {"name": "Ferrero", "price": 7.00, "stock": 9},
           12: {"name": "Malteser Chocolate", "price": 4.00, "stock": 12},
           13: {"name": "Barbican Grape Soda", "price": 5.00, "stock": 3},
           14: {"name": "Barbican Orange Soda", "price": 5.00, "stock": 9},
           15: {"name": "Choco Sticks", "price": 3.00, "stock": 4},
           16: {"name": "Rafaello Chocolate", "price": 10.00, "stock": 7},
           17: {"name": "Salad Chips", "price": 3.00, "stock": 13},
           18: {"name": "Celery Sticks", "price": 1.50, "stock": 9},
           19: {"name": "Raffle Ticket", "price": 5.00, "stock": 100},
           20: {"name": "Parking Ticket", "price": 2.00, "stock": 100}}
        
        self.balance = 0.0
#idk what im doing
   def display_items(self):
        print("Available items:")
        for key, item in self.items.items():
            print(f"{key}: {item['name']} - ${item['price']} (Stock: {item['stock']})")
#i understand it now
   def get_user_choice(self):
        choice = int(input("Enter the number of the item you want to buy: "))
        if choice in self.items:
            return choice
        else:
            print("Invalid choice. Please try again.")
            return self.get_user_choice()
#nvm i dont
   def get_quantity(self, choice):
        quantity = int(input("Enter the quantity: "))
        if quantity > 0 and quantity <= self.items[choice]["stock"]:
            return quantity
        else:
            print("Invalid quantity. Please try again.")
            return self.get_quantity(choice)
#please kys
   def calculate_total(self, price, quantity):
        return price * quantity
#i miss valorant
   def update_stock(self, choice, quantity):
        self.items[choice]["stock"] -= quantity
#rahhhhh im HIM
   def process_transaction(self, total):
        print(f"Total cost: ${total}")
        while self.balance < total:
            payment = float(input("Insert money: "))
            self.balance += payment
            print(f"Current balance: ${self.balance}")
        if self.balance >= total:
            change = self.balance - total
            self.balance = 0.0
            print(f"Transaction successful. Your change: ${change}")
#PAANO BA TOHHH
   def main(self):
        self.display_items()
        choice = self.get_user_choice()
        quantity = self.get_quantity(choice)
        total = self.calculate_total(self.items[choice]["price"], quantity)
        self.process_transaction(total)
        self.update_stock(choice, quantity)
        print(f"Dispensing {quantity} {self.items[choice]['name']}(s). Enjoy!")
#finally done
if __name__ == "__main__":
    machine = VendingMachine()
    machine.main()


