from task_2.services.printer import Printer
import pandas
import re

DATAFRAME_NAME = 'vgsales.csv'


def compute_1_task(dataframe):
    platforms = get_platforms(dataframe)
    games = dataframe.query('Year > 1999 & Year < 2011')

    genres_for_platforms = []
    for platform in platforms:
        genres_for_platforms.append(
            games.query(f'Platform == "{platform}"').shape[0]
        )

    pie_data = pandas.DataFrame({
        'Distribution of games for\ndifferent platforms from 2000 to 2010': genres_for_platforms
    }, index=platforms)
    pie_data.plot.pie(y='Distribution of games for\ndifferent platforms from 2000 to 2010', legend=False)


def compute_2_task(dataframe):
    axis_ordinate = sorted([x for x in dataframe['Year'].unique() if str(x) != 'nan'])
    axis_abscissa = []
    for val in axis_ordinate:
        axis_abscissa.append(
            dataframe.query(f'Year == "{val}"').shape[0]
        )

    graph_data = pandas.DataFrame({
        'year': axis_ordinate,
        'quantity of games': axis_abscissa
    })

    graph_data.plot.line(x='year', y='quantity of games')

def compute_3_task(dataframe):
    regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
    for region in regions:
        Printer.print_key_value(
            f'The greatest amount of sold copies of one game in {re.match(r"(NA|EU|JP|Other)", region).group(0)}',
            int(dataframe[region].max() * 1000000)
        )

def compute_4_task(dataframe):
    axis_ordinate = sorted([x for x in dataframe['Year'].unique() if str(x) != 'nan'])
    axis_abscissa = []
    for val in axis_ordinate:
        axis_abscissa.append(
            int(dataframe.query(f'Year == "{val}"')['Global_Sales'].mean() * 1000000)
        )

    graph_data = pandas.DataFrame({
        'year': axis_ordinate,
        'mean sold game copies': axis_abscissa
    })

    graph_data.plot.line(x='year', y='mean sold game copies')


def compute_5_task(dataframe):
    publishers = ['Sega', 'Capcom', 'Atari']
    all_games = dataframe.query('Publisher == "Sega" | Publisher == "Capcom" | Publisher == "Atari"')
    mean_all_sale = all_games['Global_Sales'].mean()

    mean_sales = []
    for publisher in publishers:
        publisher_games = all_games.query(f'Publisher == "{publisher}"')
        mean_sales.append(
            publisher_games['Global_Sales'].mean()
        )

    gist_data = pandas.DataFrame({
        'Publishers together': mean_all_sale,
        'Publishers separately': mean_sales
    })

    gist_data.plot.barh()



def get_platforms(dataframe):
    return dataframe['Platform'].unique()


if __name__ == '__main__':
    dataframe = pandas.read_csv('./resources/vgsales.csv')
    Printer.print_dataset_info(dataframe, DATAFRAME_NAME)

    Printer.print_empty()
    Printer.print_task_number(1)
    compute_1_task(dataframe)

    Printer.print_empty()
    Printer.print_task_number(2)
    compute_2_task(dataframe)

    Printer.print_empty()
    Printer.print_task_number(3)
    compute_3_task(dataframe)

    Printer.print_empty()
    Printer.print_task_number(4)
    compute_4_task(dataframe)

    Printer.print_empty()
    Printer.print_task_number(5)
    compute_5_task(dataframe)
