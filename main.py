class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    state = "choosing an action"

    def __init__(self):
        pass

    def action(self, inp):
        if self.state == "choosing an action":
            if inp == "buy":                
                self.state = "choosing a variant of coffee"
            elif inp == "fill":
                self.fill()
            elif inp == "take":
                self.take()
            elif inp == "remaining":
                self.remaining()
            elif inp == "exit":
                self.state = "exiting"
        elif self.state == "choosing a variant of coffee":
            if inp == "1":
                self.buy(1)
                self.state = "choosing an action"
            elif inp == "2":
                self.buy(2)
                self.state = "choosing an action"
            elif inp == "3":
                self.buy(3)
                self.state = "choosing an action"
            elif inp == "back":
                self.state = "choosing an action"
                return

    def remaining(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money\n")

    def buy(self, choice):        
        if choice == 1:
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 250 if self.water > 0 else 0
                self.beans -= 16 if self.beans > 0 else 0       
                self.money += 4
                self.cups -= 1 if self.cups > 0 else 0
            else:
                print("Sorry, not enough resources!\n")
        elif choice == 2:
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 350 if self.water > 0 else 0
                self.milk -= 75 if self.milk > 0 else 0
                self.beans -= 20 if self.beans > 0 else 0 
                self.money += 7
                self.cups -= 1 if self.cups > 0 else 0
            else:
                print("Sorry, not enough resources!\n")        
        elif choice == 3:
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 200 if self.water > 0 else 0
                self.milk -= 100 if self.milk > 0 else 0
                self.beans -= 12 if self.beans > 0 else 0
                self.money += 6
                self.cups -= 1 if self.cups > 0 else 0
            else:
                print("Sorry, not enough resources!\n")        


    def fill(self):        
        self.water += abs(int(input("Write how many ml of water do you want to add: ")))
        self.milk += abs(int(input("Write how many ml of milk do you want to add: ")))
        self.beans += abs(int(input("Write how many grams of coffee beans do you want to add: ")))
        self.cups += abs(int(input("Write how many disposable cups of coffee do you want to add: ")))


    def take(self):
        print(f"\nI gave you ${self.money}\n")
        self.money = 0


coffee_machine = CoffeeMachine()
while True:
    if coffee_machine.state == "choosing an action":
        action = input("Write action (buy, fill, take, remaining, exit): ")
    elif coffee_machine.state == "choosing a variant of coffee":
        action = input("What do you want to buy?\n 1 - espresso,\n 2 - latte,\n 3 - cappuccino,\n back - to main menu: ")
    else:
        break
    coffee_machine.action(action)
