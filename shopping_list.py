shopping_list = []

command = input("Command: Enter command add/delete/print ")

if command == 'add':
    added_item = input("Item: Enter the item to add.  ")
    shopping_list.append(added_item)
    print("{} successfully added to shopping list! ".format(added_item))
elif command == 'delete':
    deleted_item = input("Item: Enter the item to delete. ")
    shopping_list.pop(deleted_list)
    print("{} successfully added to shopping list.")
elif command == "print":
    print(shopping_list)
