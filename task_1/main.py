from task_1.services.dictionary_manager import DictionaryManager as dm
from task_1.services.printer import Printer as p

if __name__ == '__main__':
    empty_dict = dm.create_default_dict()

    while True:
        print("Enter number of generated elements in each list (from 2 to 6):")
        input_value = input("Value: ")

        try:
            value = int(input_value)
        except Exception:
            print("ERROR: You must enter number!")
            continue

        if (value < 2) | (value > 6):
            print("ERROR: The value is out of range!")
            continue
        else:
            break

    filled_dict = dm.fill_dict(value, empty_dict)
    p.print_dict(filled_dict, "Generated dictionary:")

    p.print_dict(dm.find_minimal_average(filled_dict), "Results of computation:")
