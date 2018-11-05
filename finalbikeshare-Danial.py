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


def read_data(city):
  if city == 'chicago':
    data_file = './chicago.csv'
  elif city == 'new york':
    data_file = './new_york_city.csv'
  else:
    data_file = './washington.csv'


  myList = []
  with open(data_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        myList.append(row)
  return myList


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
        text = line['Start Time']
        my_date = datetime.date(int(text[:4]), int(text[5:7]), int(text[8:10]))
        if(monthly == True and text[5:7] == MONTHS_NUM[time_period]):
            weekdays.append(my_date.strftime('%A'))
    myList = collections.Counter(weekdays)
    max_day = myList.most_common(1)[0][0]
    return max_day



def popular_hour(city_file,day_of_week):
    hours = []
    myDay = ''
    for line in city_file:
        text = line['Start Time']
        my_date = datetime.date(int(text[:4]), int(text[5:7]), int(text[8:10]))
        myDay = my_date.strftime('%A')
        #if myDay == day_of_week:
            #hours.append(text[11:13])
    myList = {}
    #myList = collections.Counter(hours)
    return myList.most_common(1)[0][0]


def trip_duration(city_file, timeUnit):
    k = 0
    duration = 0.0

    for line in city_file:
        text = line['Start Time']
        my_date = datetime.date(int(text[:4]), int(text[5:7]), int(text[8:10]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')

        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            duration += int(line['Trip Duration'])
            k+=1

    mylist = []
    mylist.append(0.0+duration/k)
    mylist.append(0.0+duration)
    return mylist


def popular_stations(city_file, timeUnit):

    startStations = []
    endStations = []
    for line in city_file:
        text = line['Start Station']
        textDate = line['Start Time']
        textEnd = line['End Station']
        my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')
        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            startStations.append(text)
            endStations.append(textEnd)

    myList = collections.Counter(startStations)
    max_station = myList.most_common(1)
    new_list = [ seq[0] for seq in max_station ]

    myList1 = collections.Counter(endStations)
    max_station1 = myList1.most_common(1)
    new_list1 = [ seq[0] for seq in max_station1 ]

    return new_list[0],new_list1[0]

def popular_trip(city_file, timeUnit):
    trips = []
    for line in city_file:
        text = line['Start Station']
        textEnd = line['End Station']
        textDate = line['Start Time']
        my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
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
        my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')
        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            types.append(text)
    myList = collections.Counter(types)
    print (myList.values(),myList.keys())
    return myList

def gender(city_file, timeUnit):
    genders = []
    for line in city_file:
        text = line['Gender']
        textDate = line['Start Time']
        my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')
        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            genders.append(text)
    myList = collections.Counter(genders)
    print (myList.values(),myList.keys())
    return myList

def birth_years(city_file, timeUnit):
    birthYear = []
    for line in city_file:
        text = line['Birth Year']
        textDate = line['Start Time']
        my_date = datetime.date(int(textDate[:4]), int(textDate[5:7]), int(textDate[8:10]))
        myDay = my_date.strftime('%A')
        myMonth = my_date.strftime('%B')
        if timeUnit == myMonth or timeUnit == myDay or timeUnit=='':
            if text != "":
                birthYear.append(text)
    myList = collections.Counter(birthYear)
    most_pop_age = myList.most_common(1)
    return myList,most_pop_age


def display_data():
    display = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n')


def statistics():

    city = get_city()
    data = read_data(city)
    timeUnit = ''
    time_period = get_time_period()


    if time_period == 'month':
        timeUnit = get_month()
        popday = popular_day(data, timeUnit)
        print("The most popular bike rental day is: ",popday)

    if time_period == 'day':
        timeUnit = get_day()
        pophour = popular_hour(data,timeUnit)
        print ("The most popular bike rental hour is: ",pophour)

    popduration = trip_duration(data,timeUnit)
    print ("The average bike rental in seconds is: ",popduration[0])

    startStation,endStation=popular_stations(data,timeUnit)
    print ("The most popular start station is: ",startStation)
    print ("The most popular end station is: ",endStation)


    popularTrip = popular_trip(data,timeUnit)
    print ("The most popular trip is: ",popularTrip)

    popularType = users(data,timeUnit)
    print ("The user types are: ")
    for line in popularType:
        print (line)

    popularGender = gender(data,timeUnit)

    print ("The genders are: ")
    #for line in popularGender:
   #print (popularGender.keys(line),popularGender.values(line))

    birthYears,popAge = birth_years(data,timeUnit)
    print ("The most popular birth year is: ",popAge)
    i = 0
    for line in sorted(birthYears):
        i+=1
        if i == 1:
            print("The oldest user was born in: ",line)
    print("The youngest user was born in: ",line)


    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results


    # Display five lines of data at a time if user specifies that they would like to
    #display_data()
     # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
