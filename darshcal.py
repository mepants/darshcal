from icalendar import Calendar, Event, vCalAddress, vText, vDate, vDatetime
from datetime import datetime, date, timedelta

#Generates iCal appointments for Darshini's nights.
#It outputs ical files for Craig and Chantal from a given Monday when D is staying with Craig.
#The iCal files should be imported into Google Calendar, to the appropriate calendars.
#Always import into a test calendar first, since appointments will be added every time the file is imported
#and entries are a pain to delete from Google


#CRAIG_CALENDAR_PATH=r"/Users/micro/Downloads/craiggallagher1976@gmail.com.ical/Darshini at Daddy's_a2kp2o80sj5nteeokb3l1pi6p4@group.calendar.google.com.ics"
CRAIG_CALENDAR_PATH_NEW=r"/Users/micro/Downloads/DaddyCalendarNew.ics"
CHANTAL_CALENDAR_PATH_NEW=r"/Users/micro/Downloads/MummyCalendarNew.ics"

#Enter a Monday when Darshini is staying with Craig
CRAIG_FROM_MONDAY=datetime.fromisoformat("2023-08-21")
#How many weeks to generate
NUM_WEEKS=26

START_DATE_ICAL = vDatetime(CRAIG_FROM_MONDAY).to_ical()

def createEvent(startDate: date, endDate: date, title) -> Event:
   evt1 = Event()
   evt1.add('dtstart', startDate)
   evt1.add('dtend', endDate)
   evt1.add('dtstamp', startDate)
   evt1.add('summary', title)
   evt1.add('fbtype', 'FREE')
   evt1.add('transp', 'TRANSPARENT')
   evt1.add('status', 'CONFIRMED')
   return evt1

# init the output calendars
outCalCraig = Calendar()
outCalChantal = Calendar()

# e = open(CRAIG_CALENDAR_PATH, 'rb')
# inCal = Calendar.from_ical(e.read())
# for component in inCal.walk():
#    if component.name=='VEVENT':
#       if component['dtstart'].to_ical() > START_DATE_ICAL:
#          #outCal.add_component(component)
#          component['status'] = 'CANCELLED'
#          outCalCraig.add_component(component)

for i in range(0, int(NUM_WEEKS/2)):
   fortnightStart = (CRAIG_FROM_MONDAY + timedelta(weeks=i * 2)).date()
   evt1 = createEvent(fortnightStart, fortnightStart, '@D')
   outCalCraig.add_component(evt1)
   evt2 = createEvent(fortnightStart + timedelta(days=3), fortnightStart + timedelta(days=6),'@D')
   outCalCraig.add_component(evt2)
   evt3 = createEvent(fortnightStart + timedelta(days=10), fortnightStart + timedelta(days=10), '@D')
   outCalCraig.add_component(evt3)

   evt4 = createEvent(fortnightStart + timedelta(days=1), fortnightStart + timedelta(days=3),'@M')
   outCalChantal.add_component(evt4)
   evt5 = createEvent(fortnightStart + timedelta(days=6), fortnightStart + timedelta(days=10),'@M')
   outCalChantal.add_component(evt5)
   evt6 = createEvent(fortnightStart + timedelta(days=11), fortnightStart + timedelta(days=14),'@M')
   outCalChantal.add_component(evt6)

for component in outCalCraig.walk():
   if component.name == 'VEVENT':
      print(component['dtstart'].to_ical())

#e.close()

f1 = open(CRAIG_CALENDAR_PATH_NEW, 'wb')
f1.write(outCalCraig.to_ical())
f1.close()

f2 = open(CHANTAL_CALENDAR_PATH_NEW, 'wb')
f2.write(outCalChantal.to_ical())
f2.close()