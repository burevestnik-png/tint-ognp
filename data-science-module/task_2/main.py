import pandas

from task_2.services.printer import Printer

DATAFRAME_NAME = 'Aids2.csv'


def to_fixed(num, digits=0):
    return f"{num:.{digits}f}"


def calculate_rows_by_sex(dataframe, sex='M'):
    return {
        'M': len(dataframe.loc[dataframe['sex'] == 'M']),
        'F': len(dataframe.loc[dataframe['sex'] == 'F'])
    }[sex]


def draw_graph_task_5(dead_people_elder_14):
    axis_abscissa = sorted(dead_people_elder_14['age'].unique())
    axis_ordinate = []
    for value in axis_abscissa:
        axis_ordinate.append(
            dead_people_elder_14['age']
                .tolist()
                .count(value)
        )

    graph_data = pandas.DataFrame({
        'age': axis_abscissa,
        'deaths': axis_ordinate,
    })

    # graph_data.plot.line(x="age", y="deaths")
    # px.line(graph_data, x="age", y="deaths").show()


def draw_pie_task_6(dead_patients_under_30, isFirstTask=True):
    area_list = dead_patients_under_30['state'].unique()
    area_amount_list = []
    for area in area_list:
        area_amount_list.append(
            dead_patients_under_30['state'].tolist().count(area)
        )

    pie_data = pandas.DataFrame({
        'amount': area_amount_list,
    }, index=area_list)

    # if isFirstTask:
    #     pie_data.plot.pie(y='amount')
    # else:
    #     plt.pie(
    #         area_amount_list,
    #         explode=(0, 0, 0, 0),
    #         labels=area_list
    #     )
    #     plt.show()


def compute_for_task_7(all_dead_people):
    mean_age = all_dead_people['age'].mean()
    Printer.print_key_value('Mean death age in Australia', to_fixed(mean_age, 3))

    area_list = all_dead_people['state'].unique()
    area_deaths_list = []
    for area in area_list:
        area_deaths_list.append(
            all_dead_people.query(f'state == "{area}"')['age'].mean()
        )

    gist_data = pandas.DataFrame({
        'Australia': mean_age,
        'Regions': area_deaths_list
    })

    gist_data.plot.barh()


def compute_8_task(dataframe):
    all_dead_people = dataframe.query('status == "D"')
    area_list = all_dead_people['state'].unique()
    area_death_list = []
    for area in area_list:
        area_death_list.append(
            all_dead_people.query(f'state == "{area}"')['age']
        )

    area_death_dict = dict(zip(area_list, area_death_list))
    for key in dict(zip(area_list, area_death_list)):
        Printer.print_key_value(f'Age of the youngest dead in {key}', area_death_dict[key].min())
        Printer.print_key_value(f'Age of the oldest dead in {key}', area_death_dict[key].max())

    people_elder_55 = []
    people_younger_30 = []
    people_mean_age = []
    for area in area_list:
        people_elder_55.append(
            dataframe.query(f'state == "{area}" & age > 55').shape[0]
        )
        people_younger_30.append(
            dataframe.query(f'state == "{area}" & age <= 30').shape[0]
        )
        people_mean_age.append(
            dataframe.query(f'state == "{area}" & age >= 31 & age <= 54').shape[0]
        )

    pie_elder_55_data = pandas.DataFrame({
        'Distribution of people elder 55 by regions': people_elder_55
    }, index=area_list)
    pie_younger_30_data = pandas.DataFrame({
        'Distribution of people younger 30 by regions': people_younger_30
    }, index=area_list)
    pie_mean_age_data = pandas.DataFrame({
        'Distribution of people elder 31 and younger 54 by regions': people_mean_age
    }, index=area_list)

    Printer.print_empty()
    pie_elder_55_data.plot.pie(y='Distribution of people elder 55 by regions')
    Printer.print_key_value(
        'The biggest amount of infected elder 55 lived in',
        find_area_for_max_infected(people_elder_55, area_list)
    )
    pie_younger_30_data.plot.pie(y='Distribution of people younger 30 by regions')
    Printer.print_key_value(
        'The biggest amount of infected younger 30 lived in',
        find_area_for_max_infected(people_younger_30, area_list)
    )
    pie_mean_age_data.plot.pie(y='Distribution of people elder 31 and younger 54 by regions')
    Printer.print_key_value(
        'The biggest amount of infected elder 31 and younger 54 lived in',
        find_area_for_max_infected(people_mean_age, area_list)
    )


def find_area_for_max_infected(list, area_list):
    return area_list[list.index(max(list))]


def compute_9_task(dataframe):
    infection_ways_list = dataframe['T.categ'].unique()
    area_list = dataframe['state'].unique()

    for area in area_list:
        amount_ways_list = []
        for way in infection_ways_list:
            amount_ways_list.append(
                dataframe.query(f'state == "{area}" & `T.categ` == "{way}"').shape[0]
            )

        gist_data = pandas.DataFrame({
            'Infection ways': infection_ways_list,
            'Amount of ways': amount_ways_list
        })

        gist_data.plot.barh(
            x='Infection ways',
            y='Amount of ways',
        )


def compute_10_task(dataframe):
    lowest_group = dataframe.query('age <= 30')
    middle_group = dataframe.query('age > 30 & age < 55')
    highest_group = dataframe.query('age > 55')

    Printer.print_key_value(
        'Is percentage of alive greater than dead in group under 30',
        is_percentage_alive_bigger_dead(lowest_group)
    )
    Printer.print_key_value(
        'Is percentage of alive greater than dead in group between 30 and 55',
        is_percentage_alive_bigger_dead(middle_group)
    )
    Printer.print_key_value(
        'Is percentage of alive greater than dead in group elder 55',
        is_percentage_alive_bigger_dead(highest_group)
    )


def is_percentage_alive_bigger_dead(group):
    alive = group.query('status == "A"').shape[0]
    dead = group.query('status == "D"').shape[0]
    return alive / group.shape[0] > dead / group.shape[0]


if __name__ == '__main__':
    Printer.print_task_number(1, '-> check in code')
    dataframe = pandas.read_csv('resources/Aids2.csv')

    Printer.print_empty()
    Printer.print_task_number(2)
    Printer.print_dataset_info(dataframe, DATAFRAME_NAME)

    Printer.print_empty()
    Printer.print_task_number(3)
    males_percentage = to_fixed(calculate_rows_by_sex(dataframe) / dataframe.shape[0] * 100, 5)
    females_percentage = to_fixed(calculate_rows_by_sex(dataframe, 'F') / dataframe.shape[0] * 100, 5)
    Printer.print_percentage_info(females_percentage, males_percentage)

    Printer.print_empty()
    Printer.print_task_number(4)
    alive_males_under_45 = len(dataframe.query('sex == "M" & age < 45 & status == "A"'))
    alive_males_under_45_per = to_fixed(alive_males_under_45 / calculate_rows_by_sex(dataframe) * 100, 5)
    Printer.print_key_value('Percentage of alive males under 45 years old', alive_males_under_45_per)

    Printer.print_empty()
    Printer.print_task_number(5)
    draw_graph_task_5(dataframe.query('age > 14 & status == "D"'))

    Printer.print_empty()
    Printer.print_task_number(6.1)
    draw_pie_task_6(dataframe.query('age < 30 & status == "D"'))
    Printer.print_task_number(6.2)
    draw_pie_task_6(dataframe.query('age < 30 & status == "D"'), False)

    Printer.print_empty()
    Printer.print_task_number(7)
    compute_for_task_7(dataframe.query('status == "D"'))

    Printer.print_empty()
    Printer.print_task_number(8)
    compute_8_task(dataframe)

    Printer.print_empty()
    Printer.print_task_number(9)
    compute_9_task(dataframe)

    Printer.print_empty()
    Printer.print_task_number(10)
    compute_10_task(dataframe)
