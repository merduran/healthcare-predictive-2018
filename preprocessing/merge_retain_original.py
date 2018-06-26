import csv

## Merging values from previous row to retain the original alarm
g = csv.writer(open("../../clean_data/5_25-5_26_ECG_merged.csv", "w"))
g.writerow(['timestamp','ECG','Respiration Rate','SpO2','Pleth','Heart Rate','Airway','Non-invasive Blood Pressure','qos','alarms'])

with open('../../clean_data/5_25-5_26_ECG_sorted_unique.csv', 'r') as read_file:
	data = csv.reader(read_file)
	
	## Skip header
	next(data)

	prev = next(data)
	for row in data:
		cur=row
		# print("prev = ", prev)
		# print("cur = ", cur)
		if cur[9]=='ECG' and cur[5]=='':
			print("YO")
			print("prev = ", prev)
			print("cur = ", cur)
			prev[9]=cur[9]
			g.writerow(prev)
			#next(data)
			prev=next(data)
			# print(prev)
		else:
			g.writerow(prev)
			prev=cur

	if cur[9]=='ECG' and cur[5]!='':
		g.writerow(cur)