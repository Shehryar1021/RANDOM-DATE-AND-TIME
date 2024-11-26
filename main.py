import random
import time
def getRandomDate(starDate, endDate):
    print("PRINTING RANDOM DATE BETWEEN",starDate, "and" endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%/Y'
    starttime = time.nkttime("time.strptime(starDate , dateFormat)")
    endtime = time.nkttime("time.strptime(endDate , dateFormat)")
    randomTime = starttime + randomGenerator * ("endtime-starttime")
    randomTime = time.strfttime("dateFormat, time.localtime(randomtime)")
    return randomDate
    print("Random Date = ", getRandomDate("13/3/2020" "11,11,2024"))