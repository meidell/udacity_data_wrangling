import time
import csv
import datetime
import collections
import numpy as np
import pandas as pd

DAYS = {"1":"Sunday", "2":"Monday", "3":"Tuesday", "4":"Wednesday", "5":"Thursday", "6":"Friday", "7":"Saturday"}
MONTHS = {"01":"January", "02":"February", "03":"March", "04":"April", "05":"May", "06":"June"}
MONTHS_NUM = {"January":"01", "February":"02", "March":"03", "April":"04", "May":"05", "June":"06"}


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def read_city_data(city):
    city_file = {
        'chicago': 'chicago.csv',
        'new york': 'new_york_city.csv',
        'washington': 'washington.csv'
    }
    filename = city_file.get(city, None)
    path = './{}'.format(filename)
    with open(path, newline='') as finp:
        reader = csv.DictReader(finp)
        return list(reader)


def get_city():
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    bikefound = 0
    while  bikefound == 0:
      if city.lower()=='chicago' or city.lower() == 'new york' or city.lower() == "washington":
        bikefound = 1
      else:
        city=input('That was an invalid input. Add a valid city: ')
        bikefound = 0
    return city.lower()



def get_time_period():
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    valid_input = False
    while valid_input == False:
      if (time_period.lower() == "day" or time_period.lower() == "month" or time_period.lower() == "none"):
        valid_input = True
      else:
        valid_input = False
        time_period = input('\n Invalid input. Please make sure you enter one of the following options: month, day or none. \n')

      return (time_period)

def get_month():
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    bikefound = 0
    while  bikefound == 0:
        if month.lower() =='january' or month.lower() == 'february' or month.lower() == 'march' or month.lower() == 'april' or month.lower() == 'may' or month.lower() == 'june':
            bikefound = 1
        else:
            month = input ('That was an invalid input. Please add a month between January and June.')
    return month.title()


def get_day():

    day = input('\n Which day? Please type your response as an integer. (e.g. 1 = Sunday)\n')
    valid_input = False
    while valid_input == False:
      if (int(day) >= 1 and int(day) <= 7):
          valid_input = True
      else:
        day = input ('\n That was an invalid input. Please add a valid day as an integer. \n')
    return DAYS.get(day)


def popular_month(data, time_period):
    count = collections.Counter()
    for line in data:
        month = line['Start Time'].split("-")[1]
        count[month] += 1
    max_month = count.most_common(1)[0][0]
    return MONTHS[max_month]


def popular_day(data, time_period):
    monthly = False
    if (time_period != 'none'):
        monthly = True
    myList = {}
    weekdays = []
    k = 0
    for line in data:
        textDate = line['Start Time']
        #my_date = datetime.date(int(text[:4]), int(text[5:7]), int(text[8:10]))
        my_date = datetime.date(int(textDate[:2]), int(textDate[3:5]), int(textDate[6:7]))
        if(monthly == True and textDate[3:5] == MONTHS_NUM[time_period]):
            weekdays.append(my_date.strftime('%A'))
    myList = collections.Counter(weekdays)
    max_day = myList.most_common(1)[0][0]
    return max_day



def popular_hour(city_file,day_of_week):
    hours = []
    myDay = ''
    for line in city_file:
        textDate = line['Start Time']
        my_date = datetime.date(int(textDate[:2]), int(textDate[3:5]), int(textDate[6:7]))
        #my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
        myDay = my_date.strftime('%A')
        if myDay == day_of_week:
            hours.append(text[11:13])
    myList = {}
    myList = collections.Counter(hours)
    return myList.most_common(1)[0][0]


def get_trip_stat(city_data, timeUnit):
    ## return trip duration, popular trip, popular
    trip_dur = trip_duration(city_data, timeUnit)
    start_dest_tuple = popular_stations(city_data, timeUnit)
    pop_trip = popular_trip(city_data, timeUnit)
    return trip_dur, start_dest_tuple, pop_trip


def trip_duration(city_file, timeUnit):
    k = 0
    duration = 0.0

    for line in city_file:
        textDate = line['Start Time']
        #my_date = datetime.date(int(text[:4]), int(text[5:7]), int(text[8:10]))
        my_date = datetime.date(int(textDate[:2]), int(textDate[3:5]), int(textDate[6:7]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')

        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            duration += float(line['Trip Duration'])
            k+=1

    mylist = []
    mylist.append(0.0+duration/k)
    mylist.append(0.0+duration)
    return mylist[0]


def popular_stations(city_file, timeUnit):

    initial_station = []
    final_station = []
    for line in city_file:


        text = line['Start Station']
        textDate = line['Start Time']
        end_station = line['End Station']
        #my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
        my_date = datetime.date(int(textDate[:2]), int(textDate[3:5]), int(textDate[6:7]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')
        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            initial_station.append(text)
            final_station.append(end_station)

    mydata = collections.Counter(initial_station)
    max_station = mydata.most_common(1)
    new_list = [ seq[0] for seq in max_station ]

    myList1 = collections.Counter(final_station)
    max_station1 = myList1.most_common(1)
    new_list1 = [ seq[0] for seq in max_station1 ]

    return new_list[0],new_list1[0]

def popular_trip(city_file, timeUnit):
    trips = []
    for line in city_file:
        text = line['Start Station']
        textEnd = line['End Station']
        textDate = line['Start Time']
        #my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
        my_date = datetime.date(int(textDate[:2]), int(textDate[3:5]), int(textDate[6:7]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')
        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            trips.append(text+" to "+textEnd)
    myList = collections.Counter(trips)
    max_trip = myList.most_common(1)
    new_list = [ seq[0] for seq in max_trip ]
    return new_list[0]

def users(city_file, timeUnit):
    types = []
    for line in city_file:
        text = line['User Type']
        textDate = line['Start Time']
        #my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
        my_date = datetime.date(int(textDate[:2]), int(textDate[3:5]), int(textDate[6:7]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')
        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            types.append(text)
    myList = collections.Counter(types)
    #print (myList.values(),myList.keys())
    return myList

def gender(city_file, timeUnit):
    genders = []
    for line in city_file:
        text = line['Gender']
        textDate = line['Start Time']
        #my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
        my_date = datetime.date(int(textDate[:2]), int(textDate[3:5]), int(textDate[6:7]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')
        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            genders.append(text)
    myList = collections.Counter(genders)
    print (myList.values(),myList.keys())
    return myList

def birth_years(city_file, timeUnit):
    year_birth = []
    for line in city_file:
        text = line['Birth Year']
        textDate = line['Start Time']
        #my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
        my_date = datetime.date(int(textDate[:2]), int(textDate[3:5]), int(textDate[6:7]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')

        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            if text != "":
                year_birth.append(text)
    myList = collections.Counter(year_birth)
    most_pop_age = myList.most_common(1)
    return myList,most_pop_age


def display_data(data):
    display = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    if display == "yes":
        for row in data[:5]:
            print(row)
#        print (data[:5]) #.head(5))



def statistics():

    city = get_city()
    data = read_city_data(city)
    timeUnit = ''
    time_period = get_time_period()

    if time_period == 'month':
        timeUnit = get_month()
        popday = popular_day(data, timeUnit)
        print("Most popular bike rental day is: ",popday)
    elif time_period == 'day':
        timeUnit = get_day()
        pophour = popular_hour(data,timeUnit)
        print ("Most popular bike rental hour is: ",pophour)


    popduration, start_dest_tuple, popularTrip = get_trip_stat(data, timeUnit)

    print ("Average bike rental in seconds is: ",popduration)
    print ("Most popular start station is: ",start_dest_tuple[0])
    print ("Most popular end station is: ",start_dest_tuple[1])
    print ("The most popular trip is: ",popularTrip)


    popularType = users(data,timeUnit)
    print ("The user types are: ")
    for line in popularType:
        print (line, popularType[line])


    if city in ["new york", "chicago"]:
        popularGender = gender(data,timeUnit)
        print ("The genders are: ")

        birthYears,popAge = birth_years(data,timeUnit)
        print ("The most popular birth year is: ",popAge)
        i = 0
        for line in sorted(birthYears):
            i+=1
            if i == 1:
                print("The oldest user was born in: ",line)
            elif i == len(birthYears):
                print("The youngest user was born in: ",line)

    # Display five lines of data at a time if user specifies that they would like to
    #display_data()
    display_data(data)
     # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    return restart.lower()=='yes'


if __name__ == "__main__":
    while(statistics()):
        pass
