import csv
# (['timestamp','ECG','Heart Rate','Respiration Rate','alarms','Airway','Pleth','SpO2','Non-invasive Blood Pressure','qos'])
fieldnames = ['timestamp', 'ECG', 'Respiration Rate','SpO2','Pleth','Heart Rate','Airway','Non-invasive Blood Pressure', 'qos', 'alarms']
writer = csv.DictWriter(open('../../clean_data/5_25-5_26_ECG.csv','w'), fieldnames=fieldnames)
good_data = csv.DictReader(open("../../clean_data/5_25-5_26_good.csv"), delimiter=',')

# Question: should we add alarm or window annotations into set date?
# Current opinion: alarm annotations. that's precisely when alarms set off. Window annotations on the other hand
# pertain to data from within the range [t-5min, t+5min], with some windows for which the alarm is silent.
# On the other hand, we may wanna consider such windows nonetheless because of our assumption that alarms at t 
# might correspond to vital signs within [t-5, t+5].
# Extracting QoS=1 .json data, put in csv file (assume QoS=0 reliable indicator of an actually bad signal)
# Find data row of alarms (if alarm annotations) and change val of alarms field to "ECG"
# write every such row to '../../clean_data/5-25_5-26_ECG.csv', also write rows with no alarms


for row in good_data:
    if row["alarms"] is '': 
        writer.writerow(row)
    elif "'string': 'ECG'" in row["alarms"]:
        row["alarms"] = "ECG"
        writer.writerow(row)
