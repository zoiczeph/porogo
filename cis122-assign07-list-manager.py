'''
CIS 122 Fall 2019 Assignment 7
Author: Zoe Turnbull
Partner:
Description:  List manager program.
'''
# VARIABLES
list_var = []
list_cmd = ["Add", "Delete", "List", "Clear"]
list_cmd_desc = ["Add to list.", "Delete Information.", "List information.", "Clear list."]
left = True
right = False

# FUNCTIONS

def cmd_help():
    print("*** Available Commands ***")
    for item in list_cmd:
        item_num = list_cmd.index(item)
        print(pad_right(item, (10 - get_max_list_item_size(item))) + list_cmd_desc[item_num])
    print("Empty to exit.")
    
def cmd_add(t):
    while True:
        add_data = input("Enter information (empty to stop): ").strip()
        if add_data == '':
            break
        else:
            list_var.append(add_data)
            print("Added, item count = " + str(len(list_var)))
    return list_var


def cmd_delete(t):
    while True:
        for item in list_var:
            item_num = list_var.index(item)
            print(pad_right(str(item_num), 2) + str(item))
        print()
        del_data = input("Enter number to delete (empty to stop): ").strip()
        if del_data == '':
            break
        elif del_data.isdigit() == False:
            print("Must be digit.")
            print()
        else:
            del_data = int(del_data)
            if (len(list_var) - 1) < del_data:
                print("Invalid input")
                print()
            elif len(list_var) >= del_data:
                if len(list_var) > 0:
                    del list_var[del_data]
                elif len(list_var) == 0:
                    print("All items deleted.")
                    break

    
def cmd_list(t):
    print("List contains " + str(len(list_var)) + " item(s).")
    for item in list_var:
        print(item)

    
def cmd_clear(t):
    print(str(len(list_var)) + " item(s) removed, list empty.")
    list_var.clear()

    
def get_max_list_item_size(t):
    max_size = len(t)
    return max_size

def pad_string(data, size, direction = left, character = " "):
    data = str(data.strip())
    if direction == left:
        padded_string = str(character * size) + str(data)
        return padded_string
    elif direction == right:
        padded_string = str(data) + str(character * size)
        return padded_string


def pad_left(data, size, character = " "):
    direction = left
    padded_string = (pad_string(data, size, direction, character))
    return padded_string


def pad_right(data, size, character = " "):
    direction = right
    padded_string = (pad_string(data, size, direction, character))
    return padded_string


# CODE
while True:
    cmd = str(input("Enter a command (? for help): ").strip().lower())
    if cmd == '':
        print("Goodbye!")
        break
    elif cmd == '?':
        cmd_help()
        print()
    elif cmd == 'add':
        cmd_add(list_var)
        print()
    elif cmd == 'delete' or cmd == 'del':
        cmd_delete(list_var)
        print()
    elif cmd == 'list':
        cmd_list(list_var)
        print()
    elif cmd == 'clear':
        cmd_clear(list_var)
        print()
    else:
        print("Unknown command.")
        print()
