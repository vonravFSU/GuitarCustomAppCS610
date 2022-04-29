import re


# Declaring Variables
possible_guitars = []
master_list = list(set())
temp_set = set()


# Loads each guitar and its corresponding attributes into a set
# & Loads each set into master list
def load_items():

    with open('guitar_list.txt', 'r') as f:
        for line in f:
            if any(c.isdigit() for c in line):
                if len(temp_set) != 0:
                    master_list.append(set(temp_set))
                    temp_set.clear()
            else:
                temp_set.add(line.strip())
    master_list.append(set(temp_set))
    temp_set.clear()


# Appends guitar to file
def append_to_file():
    count = len(master_list) + 1
    attribute = ' '

    guitar_name = input('Enter guitar name: ')

    while attribute != '':
        attribute = input('Enter attribute or Press |ENTER| when done: ')
        if attribute == '':
            break
        temp_set.add(attribute)

    with open('guitar_list.txt', 'a') as f:
        f.write(str(count))
        f.write('\n')
        f.write('name: ')
        f.write(guitar_name)
        f.write('\n')
        for i in temp_set:
            f.write(i)
            f.write('\n')
    f.close()
    temp_set.clear()
    master_list.clear()


# Writes guitars to file
def write_to_file():
    count = 0
    with open('guitar_list.txt', 'w') as f:
        for item in master_list:
            f.write(str(count))
            f.write('\n')
            for i in item:
                f.write(i)
                f.write('\n')
            count += 1
    f.close()


# Prints the name of all available guitars
def print_guitar_list():
    load_items()
    if check_if_empty():
        return

    num = 0

    for count in range(len(master_list)):
        for i in master_list[count]:
            if re.match("name", i):
                i = i.removeprefix("name: ")
                possible_guitars.append(i)

    print('Guitar List: ')
    for i in possible_guitars:
        num += 1
        print(num, i)
    possible_guitars.clear()
    wait_for_user()
    master_list.clear()


# Checks if user entry is subset of sets in master list
def check_list():
    load_items()
    if check_if_empty():
        return

    attribute = ' '

    while attribute != '':
        attribute = input('Enter attribute or Press |ENTER| when done: ')
        if attribute == '':
            break
        temp_set.add(attribute)

    print('---')
    for count in range(len(master_list)):
        if temp_set.issubset(master_list[count]):
            for i in master_list[count]:
                if re.match("name", i):
                    i = i.removeprefix("name: ")
                    possible_guitars.append(i)

    print('Guitars matching term(s): ')
    if len(possible_guitars) != 0:
        for i in possible_guitars:
            if i != possible_guitars[len(possible_guitars) - 1]:
                print(i, end=", ")
            else:
                print(i, end=".")
    else:
        print('No guitars found based on entered attribute')

    print('\n---')
    master_list.clear()
    wait_for_user()


# Deletes guitar from master list and rewrites to file
def delete_guitar():
    load_items()
    if check_if_empty():
        return

    num = int(input('Select guitar to delete: ')) - 1
    master_list.pop(num)
    write_to_file()
    print('Guitar removed')
    master_list.clear()


# Checks if guitar list is empty
def check_if_empty():
    if len(master_list) == 0:
        print('Sorry, the guitar list is empty. Try adding some.')
        wait_for_user()
        return True
    return False


# Waits for user to press ENTER to continue
def wait_for_user():
    status = ' '

    while status != '':
        status = input('Press |ENTER| to continue')
        if status == '':
            break
