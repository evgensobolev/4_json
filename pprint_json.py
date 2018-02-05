import json
import sys
import os


def load_data(filepath):
    if os.path.isfile(filepath):
        data = open(filepath, 'r')
        return data
    else:
        return 0


def pretty_print_json(data):
    try:
        jl = json.load(data)
    except ValueError:
        print("This is not JSON")
    else:
        print(json.dumps(jl, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    if sys.argv.__len__() == 1:
        print("You did not enter a file name")
    else:
        lf = load_data(sys.argv[1])
        if lf == 0:
            print("This file does not exist")
        else:
            pretty_print_json(lf)
            lf.close()
