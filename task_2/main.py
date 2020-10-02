import pandas
import plotly.express as px
import matplotlib.pyplot as plt

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
        area_deaths = all_dead_people.query(f'state == "{area}"')
        area_deaths_list.append(
            area_deaths['age'].mean()
        )

    gist_data = pandas.DataFrame({
        'Australia': mean_age,
        'Regions': area_deaths_list
    })

    gist_data.plot.barh()



if __name__ == '__main__':
    Printer.print_task_number(1, '-> check in code')
    dataframe = pandas.read_csv('./resources/Aids2.csv')

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
