import random ;
import time
def get_Random_Date(start_date,end_date):
    print("Printing random date bewteen",start_date,"and",end_date)
    randomGenrator = random.random()
    dateformat='%m/%d/%Y'
    start_time = time.mktime(time.strptime(start_date, dateformat))
    end_time = time.mktime(time.strptime(end_date, dateformat))
    random_time=random.uniform(start_time, end_time)
    random_date = time.strftime(dateformat, time.localtime(random_time))
    return random_date
print("Random date:",get_Random_Date("1/1/2016","12/12/2026"))

