import json
import sys


def load_data(filepath):
    try:
        with open(filepath, 'r') as input_file:
            return json.load(input_file)
    except ValueError:
        return None


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    try:
        json_data = load_data(sys.argv[1])
        if json_data:
            pretty_print_json(json_data)
        else:
            print('This file is not JSON')
    except IndexError:
        print('No path JSON file')
    except FileNotFoundError:
        print('File not fount')
