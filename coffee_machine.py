from main import MENU
from main import resources

should_continue = True
while should_continue:
    print(resources)
    choice = input("WHAT DO U WANT(ESPRESSO/LATTE/CAPPUCCINO)??")
    required_water = MENU[choice]["ingredients"]["water"]
    required_milk = MENU[choice]["ingredients"]["milk"]
    required_coffee = MENU[choice]["ingredients"]["coffee"]
    required_cash = MENU[choice]["cost"]
    if resources["water"] >= required_water and resources["milk"] >= required_milk and resources[
        "coffee"] >= required_coffee:
        print(f"That'll be {required_cash} $.")
        penny = int(input("ENTER THE NO. OF PENNY COINS: ")) * 0.01
        dime = int(input("ENTER THE NO. OF DIME COINS: ")) * 0.10
        nickel = int(input("ENTER THE NO. OF NICKEL COINS: ")) * 0.05
        quarter = int(input("ENTER THE NO. OF QUARTER COINS: ")) * 0.25
        sufficient = penny + dime + nickel + quarter
        if sufficient >= required_cash:
            print(f"Here's Your {choice}")
            print(f"Here's your {sufficient - required_cash} $ change")
            resources["water"] -= required_water
            resources["milk"] -= required_milk
            resources["coffee"] -= required_coffee
            print("\n")
            if input("DO U WANT COFFEE? Y OR N??").lower() == "y":
                should_continue = True
            else:
                should_continue = False
        else:
            print("You don't have enough money!!")
    else:
        print(f"Sorry we are out of {choice}!!")
        if input("DO U WANT COFFEE? Y OR N??").lower() == "y":
            should_continue = True
        else:
            should_continue = False
