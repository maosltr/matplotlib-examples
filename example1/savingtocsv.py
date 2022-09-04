import csv
import random
import time
import os

os.remove('demo_csv1.csv')
column_name = ["time", "cpu load"]
xaxis = 0
with open('demo_csv1.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(column_name)
    f.close()
while True:  
    with open('demo_csv1.csv', 'a') as f:
        writer = csv.writer(f)  

        writer.writerow([xaxis, random.randint(1,10)])
        xaxis += 1
        time.sleep(1)