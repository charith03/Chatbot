import datetime
currentDate = datetime.datetime.now()
print("Hello , I am chatty ")
name = input("Hello, what is your name? ")
print("Hello " + name)
feeling = input("How are you today? ")
if "good" in feeling:
    print("I'm feeling good too!")
else:
    print("I'm sorry to hear that!")
interest = input(print("do you want to know your age in years, days, hours, minutes, sec you live till now ?"))
if 'yes' in interest:
    print("okay,then lets find out now")
elif 'no' in interest:
    print("okay then bye.....")
deadline= input ('Bot : Plz enter your date of birth (mm/dd/yyyy) :: ')
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
print (deadlineDate)
daysLeft = currentDate - deadlineDate
print(daysLeft)

years = ((daysLeft.total_seconds())/(365.242*24*3600))
yearsInt=int(years)

months=(years-yearsInt)*12
monthsInt=int(months)

days=(months-monthsInt)*(365.242/12)
daysInt=int(days)

hours = (days-daysInt)*24
hoursInt=int(hours)

minutes = (hours-hoursInt)*60
minutesInt=int(minutes)

seconds = (minutes-minutesInt)*60
secondsInt =int(seconds)

print('You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} \
 minutes, {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt))