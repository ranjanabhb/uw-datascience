import pandas as pd
from collections import Counter
from ggplot import *
from geojson import geoCode
from bar_plot import *

def extractMonth(date):
    return date.split("/")[0]
        
def extractHour(date):
    return date.split(":")[0]

def extractLatLng(location):
    (lat, lng) = location.split(",")
    return (lat[1:8], lng[:10])

def printCounter(counter, topN = None):
    print 
    for (key, value) in counter.most_common(topN):
        print (str(key) + ", " + str(value))    

def printSortedList(lst):
    print 
    for item in lst:
        print (str(item[0]) + ", " + str(item[1]))            

def extractColumnFromDf(df, column, counter, processor = None):
    for ctg in df[column]:
        if processor:
            counter[processor(ctg)] += 1    
        else:
            counter[ctg] += 1                

def extractZipCodeFromLatLng(source, sink):
    for (latLong, cnt) in source.most_common(10):
        loc = str(latLong[0]) + ", " + str(latLong[1])
        sink[geoCode(loc)] = cnt

def processDF(df):
    category = Counter()
    dayOfWeek = Counter()
    month = Counter()
    hourOfTheDay = Counter()
    latLng = Counter()
    zipCode = Counter()
    print ("\nDF Len - " + str(len(df)))    
    extractColumnFromDf(df, 'Category', category)
    printCounter(category, 10)

    extractColumnFromDf(df, 'DayOfWeek', dayOfWeek)
    printCounter(dayOfWeek, 7)

    extractColumnFromDf(df, 'Date', month, extractMonth)
    sortedMonth = sorted(month.items())
    printSortedList(sortedMonth)

    extractColumnFromDf(df, 'Time', hourOfTheDay, extractHour)
    sortedHourOfTheDay = sorted(hourOfTheDay.items())
    printSortedList(sortedHourOfTheDay)

    extractColumnFromDf(df, 'Location', latLng, extractLatLng)
    extractZipCodeFromLatLng(latLng, zipCode) 
    printCounter(zipCode)

    zcList = [(key, value) for (key, value) in zipCode.most_common(4)]
    plotBar(zcList, 'Incidents Per ZipCode', 'Incident Count', 5)
    
def main():
    df = pd.read_csv('sf_long.csv')    
    print len(df)
    filtered_df = df[df.Category == 'LARCENY/THEFT'];
    print len(filtered_df)
    processDF(df)
    processDF(filtered_df)

if __name__ == "__main__":
    main()
