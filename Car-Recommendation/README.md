# Car_recommendation

Write a python program that helps a buyer to choose his desired car based on available cars of different models and parameters from a car shop. Consider the following while developing the python code:
1.	Car: This class will represent a car with its attributes (price, fuel efficiency, brand, etc.).
2.	CarShop: This class will represent the car shop that contains available cars.
3.	CarBuyer: This class will assist the buyer in choosing a car based on their preferences.



# Example usage:
# 1. Create a CarShop and add some cars
car_shop = CarShop()
# Adding some car models to the car shop
car_shop.add_car(Car('Honda Civic', 22000, 30, 'Honda', 158, 4.5, 'Red'))
car_shop.add_car(Car('Toyota Corolla', 21000, 32, 'Toyota', 139, 4.7, 'Blue'))
car_shop.add_car(Car('BMW 3 Series', 35000, 25, 'BMW', 255, 4.2, 'Black'))
car_shop.add_car(Car('Ford Focus', 20000, 28, 'Ford', 160, 4.3, 'White'))
car_shop.add_car(Car('Chevrolet Malibu', 23000, 26, 'Chevrolet', 160, 4.4, 'Silver'))
# 2. Ask for buyer preferences and create a CarBuyer object
print("Welcome to the car shop!\n")
# Get buyer preferences (for simplicity, input is taken as plain text)
try:
    budget = float(input("Enter your maximum budget (in USD): $"))
    min_fuel_efficiency = float(input("Enter the minimum fuel efficiency (in MPG): "))
    brand_preference = input("Enter your preferred brand (leave blank for any): ")
    min_safety_rating = float(input("Enter the minimum safety rating (out of 5): "))
    buyer = CarBuyer(budget, min_fuel_efficiency, brand_preference, min_safety_rating)
    # 3. Get recommendations based on buyer preferences
    buyer.recommend_car(car_shop)

except ValueError:
    print("Invalid input! Please enter valid numbers for budget, fuel efficiency, and safety rating.")
