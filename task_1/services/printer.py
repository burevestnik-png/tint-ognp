class Printer:
    separator = "<======================================>"

    @classmethod
    def print_dict(cls, dictionary, message=""):
        print("")
        cls.print_separator()

        print(message)
        print("{")
        for key, value in dictionary.items():
            print("    {0}: {1}".format(key, value))
        print("}")

        cls.print_separator()

    @classmethod
    def print_separator(cls):
        print(cls.separator)
