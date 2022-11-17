# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries
groceries_list = ["Water", "Butter", "Eggs", "Apples", "Cinnamon", "Sugar", "Milk"]
print(groceries_list)

# @TODO: Find the first two items on the list
first_two = groceries_list[:2]
print(first_two)

# @TODO: Find the last five items on the list
last_five = groceries_list[-5:]
print(last_five)

# @TODO: Find every other item on the list, starting from the second item
every_other = groceries_list[1::2]
print(every_other)

# @TODO: Add an element to the end of the list
groceries_list.append("Flour")
print(groceries_list)

# @TODO: Changes a specified element within the list at the given index
groceries_list[3] = "Gala Apples"
print(groceries_list)

# @TODO: Calculate how many items you have in the list
count_items = len(groceries_list)
print(count_items)

# ----------------------Go to the grocery store---------------------------")

# @TODO: Find the index of the particular element name
print('Find the index of gala apples.')
print(groceries_list.index('Gala Apples'))


# @TODO: Remove an element from the list based on the given element name





# @TODO: Remove an element from the list based on the given index






# @TODO: Remove the last element of the list





print("You continue on your journey purchasing groceries...")
