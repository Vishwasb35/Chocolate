from database import initialize_db, insert_seasonal_flavor, insert_ingredient, insert_customer_suggestion, fetch_seasonal_flavors, fetch_ingredients, fetch_customer_suggestions

def main():
    # Initialize the database
    initialize_db()

    # Example: Add some seasonal flavors
    insert_seasonal_flavor("Pumpkin Spice", "A warm seasonal flavor with cinnamon and pumpkin", "2024-10-01", "2024-12-31")
    insert_seasonal_flavor("Mint Chocolate", "A refreshing mint paired with rich chocolate", "2024-11-01", "2024-12-31")
    
    # Example: Add some ingredients
    insert_ingredient("Cocoa", 100)
    insert_ingredient("Milk", 50)
    
    # Example: Add some customer suggestions
    insert_customer_suggestion("John Doe", "Caramel Sea Salt", "Peanuts")
    
    # Fetch and display data
    print("Seasonal Flavors:")
    for flavor in fetch_seasonal_flavors():
        print(f"{flavor['name']} - {flavor['description']} (Available from {flavor['available_from']} to {flavor['available_until']})")
    
    print("\nIngredients:")
    for ingredient in fetch_ingredients():
        print(f"{ingredient['name']} - Quantity: {ingredient['quantity']}")
    
    print("\nCustomer Suggestions:")
    for suggestion in fetch_customer_suggestions():
        print(f"{suggestion['customer_name']} suggests {suggestion['flavor_suggestion']} (Allergies: {suggestion['allergies']})")

if __name__ == "__main__":
    main()