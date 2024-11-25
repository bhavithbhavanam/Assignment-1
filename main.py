# Define recipes and resources
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slices
            "ham": 4,    # slices
            "cheese": 4, # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slices
            "ham": 6,    # slices
            "cheese": 8, # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slices
            "ham": 8,    # slices
            "cheese": 12, # ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  # slices
    "ham": 18,    # slices
    "cheese": 24, # ounces
}


# SandwichMachine class
class SandwichMaker:

    def __init__(self, available_resources):
        """Initialize the machine with available resources."""
        self.resources = available_resources

    def is_resource_sufficient(self, required_ingredients):
        """Check if there are enough resources to fulfill the order."""
        for item, amount in required_ingredients.items():
            if self.resources.get(item, 0) < amount:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def collect_payment(self):
        """Collect coins and calculate the total inserted."""
        print("Please insert coins:")
        dollar_coins = int(input("How many dollar coins? ")) * 1.0
        half_dollars = int(input("How many half-dollars? ")) * 0.5
        quarters = int(input("How many quarters? ")) * 0.25
        nickels = int(input("How many nickels? ")) * 0.05

        total_payment = dollar_coins + half_dollars + quarters + nickels
        return total_payment

    def process_transaction(self, payment, sandwich_cost):
        """Check if the payment is sufficient and provide change if necessary."""
        if payment >= sandwich_cost:
            change = round(payment - sandwich_cost, 2)
            print(f"Transaction successful. Here is ${change} in change.") if change > 0 else None
            return True
        else:
            print("Insufficient payment. Money refunded.")
            return False

    def prepare_sandwich(self, size, required_ingredients):
        """Deduct the used ingredients from available resources."""
        for item, amount in required_ingredients.items():
            self.resources[item] -= amount
        print(f"Your {size.capitalize()} sandwich is ready! Enjoy!")


# Create an instance of SandwichMaker
sandwich_maker = SandwichMaker(resources)

def serve_sandwich():
    while True:
        print("\nMenu: small, medium, large\nOptions: report, off")
        user_choice = input("What would you like? ").lower()

        if user_choice in recipes:
            sandwich_recipe = recipes[user_choice]
            if sandwich_maker.is_resource_sufficient(sandwich_recipe["ingredients"]):
                payment = sandwich_maker.collect_payment()
                if sandwich_maker.process_transaction(payment, sandwich_recipe["cost"]):
                    sandwich_maker.prepare_sandwich(user_choice, sandwich_recipe["ingredients"])
        elif user_choice == "report":
            for item, amount in sandwich_maker.resources.items():
                unit = "slice(s)" if item != "cheese" else "ounce(s)"
                print(f"{item.capitalize()}: {amount} {unit}")
        elif user_choice == "off":
            print("Shutting down the sandwich machine. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from the menu or options.")

# Start the sandwich machine
serve_sandwich()
