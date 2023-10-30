#!/usr/bin/python3
def find_replace(original, find, replace):
    my_list = []
    for i in original:
        if i == find:
            my_list.append(replace)
        else:
            my_list.append(i)
    return my_list


if __name__=="__main__":
    original = [0, 11, 13, 9, 4, 3, 4, 7, 7, 1, 0, 9]
    modified = find_replace(original, 9, 13)

    print(f"Original: {original}")
    print(f"Modified: {modified}")
    
