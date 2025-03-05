# Restaurant-Management-System

#Objective
The goal of this assignment is to build a simple Restaurant Management System using Python. This system will allow:
1.	Managing the menu (add, remove, or update items).
2.	Taking customer orders.
3.	Calculating bills with tax and service charges.
4.	Handling errors gracefully using exception handling.
________________________________________
Instructions
1.	Complete the Program Functionality:
Implement all features listed below.
2.	Use Exception Handling:
Handle errors like invalid input, unavailable items, and improper menu management.
________________________________________
Requirements
Features to Implement
1.	Menu Management:
o	Allow the manager to:
	Add new menu items with prices.
	Remove items from the menu.
	Update the price and quantity of existing items.
2.	Take Orders:
o	Display the menu to customers.
o	Allow customers to select items and quantities.
o	Validate that items exist in the menu.
3.	Bill Calculation:
o	Calculate the total cost, including:
	10% service charge.
	5% tax.
4.	Error Handling:
o	Handle invalid inputs (e.g., non-numeric prices, nonexistent menu items).
5.	Exit System:
o	Allow users to exit the system gracefully.
Sample Output:
Restaurant System:
1.	Manage Menu
2.	Take Order
3.	Calculate Bill
4.	Exit
Enter your choice:
Menu Management:
1.	Add Item
2.	Remove Item
3.	Update Item Price
4.	View Menu
5.	Exit Management
Enter your choice: 1
Enter item name: Pasta
Enter item price: 12.50
Item added successfully!

Take Orders
Menu:
1.	Burger - $5.99
2.	Pizza - $8.49
3.	Salad - $4.99
Enter item name to order: Pizza
Enter quantity: 2
Order added: Pizza x 2

Bill Calculation

Order Summary:
Pizza x 2 = $16.98
Tax (5%): $0.85
Service Charge (10%): $1.70
Total: $19.53
