import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

n=24
my_date = datetime.date(1984, 6, 24)
my_date = datetime.date(day=n, year=1984, month=6)

print (my_date)

'''string_date =  my_date.strftime('%m/%d/%Y')  # This writes "06/24/1984"'''
string_date =  my_date.strftime('%B')
print (string_date)
