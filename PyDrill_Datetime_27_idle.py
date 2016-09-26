from datetime import date, time, datetime, timedelta

timeNow = datetime.now()
portlandTime = timeNow
newYorkTime = timeNow + timedelta(hours=3)
londonTime = timeNow + timedelta(hours=8)
opentime = timeNow.replace(hour=9, minute=0, second=0, microsecond=0)
closetime = timeNow.replace(hour=21, minute=0, second=0, microsecond=0)
opentimetomorrow = opentime + timedelta(days=1)
closetimetomorrow = closetime + timedelta(days=1)

print portlandTime, newYorkTime, londonTime

def portlandBranch():
    if opentime < portlandTime < closetime:
        print 'The branch in Portland is OPEN'
    else:
        print 'The branch in Portland is CLOSED'
    return;
        
def newYorkBranch():
    if opentime < newYorkTime < closetime or opentimetomorrow < newYorkTime < closetimetomorrow:
        print 'The branch in New York is OPEN'
    else:
        print 'The branch in New York is CLOSED'
    return;
        
def londonBranch():
    if opentime < londonTime < closetime or opentimetomorrow < londonTime < closetimetomorrow:
        print 'The branch in London is OPEN'
    else:
        print 'The branch in London is CLOSED'
    return;

print "Hello, this program will tell you whether a certain branch is open or closed."
print "Please enter the branch you would like to check by entering 'Portland' 'New York or 'London' without quotations"

city = raw_input()

if city == "Portland":
    portlandBranch()
elif city == "New York":
    newYorkBranch()
elif city == "London":
    londonBranch()
else:
    print "Sorry, you have entered the incorrect keyword"
