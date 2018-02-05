import json
import sys
import os


def load_data(filepath):
    if os.path.isfile(filepath):
        input_file = open(filepath, 'r')
        return input_file
    else:
        return 0


def pretty_print_json(data):
    try:
        json_data = json.load(data)
    except ValueError:
        print("This is not JSON")
    else:
        print(json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    if sys.argv.__len__() == 1:
        print("You did not enter a file name")
    else:
        json_file = load_data(sys.argv[1])
        if json_file == 0:
            print("This file does not exist")
        else:
            pretty_print_json(json_file)
            json_file.close()
