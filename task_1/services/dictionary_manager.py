from numpy.random import random_integers
from numpy import mean, amin


class DictionaryManager:
    @staticmethod
    def create_default_dict():
        return {
            '1': [],
            '2': [],
            '3': []
        }

    @staticmethod
    def fill_dict(quantity, dictionary):
        for key in dictionary:
            dictionary[key] = random_integers(1, 10, quantity).tolist()
        return dictionary

    @staticmethod
    def find_minimal_average(dictionary):
        averages = []
        for key in dictionary:
            averages.append(mean(dictionary[key]))

        min_average = amin(averages)
        average_index = averages.index(min_average)

        return {
            'key': list(dictionary.keys())[average_index],
            'value': list(dictionary.values())[average_index],
            'average': round(min_average, 2)
        }
