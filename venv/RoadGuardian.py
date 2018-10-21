import pandas as pd

df = pd.read_csv('/Users/Pranav/Documents/Hackathons/HackHarvard/RoadGuardian/venv/Vehicle Crashes 14-15.csv')
numRows = len(df.index);
prevDate = df.iloc[1, 0]
prevHour = df.iloc[1, 1]
dateList = []
hourList = []
finalHourList = []
accidentsList = []
hourCount = 1

for x in range (numRows):
    date = df.iloc[x, 0]
    print(date)
    hour = df.iloc[x, 1]
    print(hour)
    if date == prevDate:
        if hour == prevHour:
            hourCount = hourCount + 1
            print ("hourCount: "+str(hourCount))
        else:
            dateList.append(prevDate)
            hourList.append(prevHour)
            accidentsList.append(hourCount)
            hourCount = 1
            prevHour = hour
            prevDate = date
    else:
        dateList.append(prevDate)
        prevDate = date
        hourList.append(prevHour)
        prevHour = hour
        accidentsList.append(hourCount)
        hourCount = 1

dateList.append(prevDate)
hourList.append(prevHour)
accidentsList.append(hourCount)

print("gello")

print("date list: "+str(len(dateList)))
print("hour list: "+str(len(hourList)))

dictionary = {"date": dateList, "hour": hourList, "accidents": accidentsList}
out = pd.DataFrame(dictionary)
out.to_csv('out.csv')