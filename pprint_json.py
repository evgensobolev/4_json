import json
import sys


def load_data(filepath):
    try:
        return json.load(filepath)
    except ValueError:
        print("This is not JSON")


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r') as input_file:
            json_data = load_data(input_file)
            if json_data != None:
                pretty_print_json(json_data)
    except IndexError:
        print("You did not enter a file name")
    except IOError:
        print("Such file does not exist")
