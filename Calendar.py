from datetime import timedelta, datetime, timezone
import pytz
from pyicloud import PyiCloudService
import os
from dotenv import load_dotenv, find_dotenv

def list_events(firstArg = 0):
    print("Retrieving...")
    days = firstArg

    startDate  = datetime.now(tz=pytz.UTC)
    endDate    = startDate + timedelta(days=days)
    utcEndDate = endDate.replace(tzinfo=timezone.utc)

    allEvents  = ""

    load_dotenv(find_dotenv())
    api = PyiCloudService(os.environ.get("APPLE_ID"))

    events  = api.calendar.events(startDate, utcEndDate)
    for x in range(len(events)-1):
        try:
            eventName = events[x]['title'] + " - "
            eventDateTime = str(datetime.strptime(str(events[x]['startDate'][0])+" "+str(events[x]['startDate'][4])+":"+str(events[x]['startDate'][5]), '%Y%m%d %H:%M').strftime("%A %b %d, %I:%M%p")) + " - "
            eventLocationWSpaces=str(events[x]['location'])
            eventLocation = " ".join(eventLocationWSpaces.split())+'\n'
            eventInfo = eventName+eventDateTime+eventLocation
            allEvents += eventInfo
        except:
            pass
    return allEvents



if __name__ == '__main__':
    print(list_events(5))