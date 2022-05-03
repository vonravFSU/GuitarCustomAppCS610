"""
Author: Hazmed Moreno & James Whittington
Class: Utility
Description: Contains essential functions to the Guitar App.
Version: 1.0.0
Release Date: 5.1.2022
contact: hmoreno0@frostburg.edu
         jrwhittington0@frostburg.edu
"""

import re


# Declaring Variables
possible_guitars = []  # array for printing possible guitars
guitar_counter = []  # array for popularity counter
guitar_cost = []  # array for costs of guitars
master_list = list(set())  # list of sets for reading guitars
temp_set = set()  # temporary set for reading into master_list
guitar_set = set()  # temporary set to write for


# Loads each guitar and its corresponding attributes into a set
# & Loads each set into master list
def load_items():
    with open('guitar_list.txt', 'r') as f:
        for line in f:
            if any(c == '-' for c in line):
                if len(temp_set) != 0:
                    master_list.append(set(temp_set))
                    temp_set.clear()
            else:
                temp_set.add(line.strip())
    master_list.append(set(temp_set))
    temp_set.clear()


# Appends guitar to file
def append_to_file():
    attribute = ' '

    guitar_name = input('Enter guitar name: ')
    g_cost = input('Enter guitar cost or (0) if not available: ')

    while attribute != '':
        attribute = input('Enter attribute or Press |ENTER| when done: ')
        if attribute == '':
            break
        temp_set.add(attribute)

    with open('guitar_list.txt', 'a') as f:
        f.write('-')
        f.write('\n')
        f.write('name: ')
        f.write(guitar_name)
        f.write('\n')
        f.write('counter: ')
        f.write('0')
        f.write('\n')
        f.write('cost: ')
        f.write(str(g_cost))
        f.write('\n')
        for i in temp_set:
            f.write(i)
            f.write('\n')
    f.close()
    temp_set.clear()
    master_list.clear()


# Writes guitars to file
def write_to_file():
    with open('guitar_list.txt', 'w') as f:
        for item in master_list:
            f.write('-')
            f.write('\n')
            for i in item:
                f.write(i)
                f.write('\n')
    f.close()
    master_list.clear()


# Prints the name of all available guitars
def print_guitar_list():
    sorting_list = list(list())  # temporary list of lists to sort guitars by price
    temp_list = list() #temporary list
    g_count = 0
    load_items()
    if check_if_empty():
        return

    num = 0

    for count in range(len(master_list)):
        for i in master_list[count]:
            if re.match("name", i):
                i = i.removeprefix("name: ")
                possible_guitars.append(i)
            elif re.match("counter", i):
                i = i.removeprefix("counter: ")
                guitar_counter.append(i)
            elif re.match("cost", i):
                i = i.removeprefix("cost: ")
                guitar_cost.append(i)

    print('Guitar List sorted by price: ')
    for i in possible_guitars:
        temp_list.append(i)
        temp_list.append(guitar_counter[g_count])
        temp_list.append(int(guitar_cost[g_count]))
        sorting_list.append(list(temp_list))
        temp_list.clear()
        g_count += 1

    # Sorting List By Price Using TimSort
    sorting_list.sort(key=lambda x: x[2])

    for i in sorting_list:
        num += 1
        print(num, i[0],
              '| Popularity: ', i[1],
              ' | Cost: $', i[2])

    possible_guitars.clear()
    master_list.clear()
    guitar_counter.clear()
    sorting_list.clear()
    wait_for_user()


# Checks if user entry is subset of sets in master list
def check_list():
    load_items()
    sorting_list = list(list())  # temporary list of lists to sort guitars by price
    temp_list = list() #temporary list
    num = 0

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
                    guitar_set.add(i)
                    i = i.removeprefix("name: ")
                    possible_guitars.append(i)
                elif re.match("counter", i):
                    i = i.removeprefix("counter: ")
                    guitar_counter.append(i)
                    g_count = int(i)
                    i = 'counter: ' + str(g_count + 1)
                    guitar_set.add(i)
                elif re.match("cost", i):
                    guitar_set.add(i)
                    i = i.removeprefix("cost: ")
                    guitar_cost.append(i)
                else:
                    guitar_set.add(i)
            master_list[count] = set(guitar_set)
            guitar_set.clear()

    print('Guitars matching term(s): ')
    if len(possible_guitars) != 0:
        count = 0
        g_count = 0
        for i in possible_guitars:
            temp_list.append(i)
            temp_list.append(guitar_counter[g_count])
            temp_list.append(int(guitar_cost[g_count]))
            sorting_list.append(list(temp_list))
            temp_list.clear()
            g_count += 1

        # Sorting List By Price Using TimSort
        sorting_list.sort(key=lambda x: x[2])

        for i in sorting_list:
            num += 1
            print(num, i[0],
                  '| Popularity: ', i[1],
                  ' | Cost: $', i[2])

        """
        for i in possible_guitars:
            count += 1
            print(count, '', i, '| Popularity: ',
                  guitar_counter[g_count],
                  '| Cost: $', guitar_cost[g_count])
            g_count += 1
        """
    else:
        print('No guitars found based on entered attribute')
    print('---')

    guitar_counter.clear()
    guitar_cost.clear()
    possible_guitars.clear()
    guitar_set.clear()
    sorting_list.clear()
    write_to_file()
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
    if not master_list[0]:
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
