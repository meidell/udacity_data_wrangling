## TODO: import all necessary packages and functions
import time
import csv
import datetime
import collections




## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def read_data(city):

    if city == 'chicago':
        data_file = './chicago.csv'
    elif city == 'new york':
        data_file = './new_york_city.csv'
    else:
        data_file = './washington.csv'
    myList = []
    k = 0
    with open(data_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            myList.append(row)
    return myList


def get_city():
    city = input('\nHello! Let\'s explore some minor US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    bfound = 0
    while  bfound == 0:
        if city.lower()=='chicago' or city.lower() == 'new york' or city.lower() == "washington":
            bfound = 1
        else:
            city=input('That was an invalid input. Add a valid city : ')
            bfound = 0
    return(city.lower())


def get_time_period():
    time_period = input('\nWould you like to filter the data by month, day,or not at all? Type "none" for no time filter.\n')
    bfound = 0
    while  bfound == 0:
        if time_period.lower()=='month' or time_period.lower() == 'day' or time_period.lower() == "none":
            bfound = 1
        else:
            time_period=input('That was an invalid input. Add day, month or none : ')
    return(time_period)


def get_month():
    month = input('\nWhich month? January, February, March, April, May or June')
    bfound = 0
    while  bfound == 0:
        if month.lower()=='january' or month.lower() == 'february' or month.lower() == 'march' or month.lower() == 'april' or month.lower() == 'may' or month.lower() == 'june':
            bfound = 1
        else:
            month=input('That was an invalid input. Add a month between January and June : ')
    return(time_period)


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function


def popular_month(data, time_period):
    myList = {}
    months = []
    for line in data:
        text = line['Start Time']
        months.append(text[6:7])

    myList = collections.Counter(months)
    for k,v in myList.items():
        print (k,v)

def popular_day(data, time_period):

    myList = {}
    weekdays = []
    k=0
    for line in data:
        text = line['Start Time']
        my_date = datetime.date(int(text[:4]), int(text[5:7]), int(text[8:10]))
        weekdays.append(my_date.strftime('%A'))
    myList = collections.Counter(weekdays)
    for k,v in myList.items():
        print (k,v)


def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What hour of the day (1, 2, ... 23, 24) occurs most often in the start time?
    '''
    # TODO: complete function


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most frequently used start station and most frequently
    used end station?
    '''
    # TODO: complete function


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most common trip (i.e., the combination of start station and
    end station that occurs the most often)?
    '''
    # TODO: complete function


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the earliest birth year (when the oldest person was born),
    most recent birth year, and most common birth year?
    '''
    # TODO: complete function


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function


def statistics():
    city = get_city()
    data = read_data(city)

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        print("List of most popular months: ")
        popular_month(data,time_period)
        print("That took %s seconds." % (time.time() - start_time))

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        # TODO: call popular_day function and print the results
        print("List of most popular day of week: ")
        popular_day(data,time_period)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":

	statistics()
