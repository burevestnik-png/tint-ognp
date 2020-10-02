from task_2.services.colors import Colors


class Printer:
    @classmethod
    def print_task_number(cls, number, message=''):
        print(cls.color_red(f'Task {number} {"" if message == "" else message}'))

    @classmethod
    def print_dataset_info(cls, dataframe, name=""):
        print(f'{cls.color_green("You are working with dataframe:")} {cls.color_blue(name)}')
        print(f'{cls.color_green("Dataframe size:")} {cls.color_blue(dataframe.size)}')
        print(f'{cls.color_green("Dataframe shape:")} {cls.color_blue(dataframe.shape)}')
        print(f'{cls.color_green("Dataframe types:")}')
        print(cls.color_blue(dataframe.dtypes))

    @classmethod
    def print_empty(cls):
        print()

    @classmethod
    def print_key_value(cls, key, value):
        print(f'{cls.color_green(key)}: {cls.color_blue(value)}')

    @classmethod
    def print_percentage_info(cls, females, males):
        print(f'{cls.color_green("Female percentage:")} {cls.color_blue(females)}%')
        print(f'{cls.color_green("Male percentage:")} {cls.color_blue(males)}%')

    @classmethod
    def color_green(cls, value):
        return f'{Colors.GREEN}{value}{Colors.ENDC}'

    @classmethod
    def color_blue(cls, value):
        return f'{Colors.BLUE}{value}{Colors.ENDC}'

    @classmethod
    def color_yellow(cls, value):
        return f'{Colors.WARNING}{value}{Colors.ENDC}'

    @classmethod
    def color_red(cls, value):
        return f'{Colors.FAIL}{value}{Colors.ENDC}'
