#!/usr/bin/python3
# 7-add_item
"""
Implements a script that adds all arguments to a Python list,
and then save them to a file
"""


def get_args():
    """
    Gets all arguments

    Return:
    A list of arguments
    """
    import sys
    arg_list = []
    for i in range(1, len(sys.argv)):
        arg_list.append(sys.argv[i])
    return arg_list


def read_from_file(filename):
    """
    Creates a list from a "JSON file"

    Args:
    filename (string): The name of the file

    Return:
    A list
    """
    load_file = __import__("6-load_from_json_file").load_from_json_file
    try:
        list = load_file(filename)
    except Exception:
        list = []
    return list


def main():
    """The main function"""
    save_file = __import__("5-save_to_json_file").save_to_json_file
    filename = "add_item.json"
    json_list = read_from_file(filename)
    json_list.extend(get_args())
    save_file(json_list, filename)


main()
