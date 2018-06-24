import csv
import operator
import json

## Sorting file based on timestamp
data = csv.reader(open('../../clean_data/5_25-5_26_ECG.csv', 'r'))
sortedlist = sorted(data, key=lambda row: row[0])
g = csv.writer(open("../../clean_data/5_25-5_26_ECG_sorted.csv", "w"))
g.writerow(['timestamp','ECG','Respiration Rate','SpO2','Pleth','Heart Rate','Airway','Non-invasive Blood Pressure','qos','alarms'])
for el in sortedlist:
	g.writerow(el)

## Removing duplicates and merging values from different rows with same timestamp
g = csv.writer(open("../../clean_data/5_25-5_26_ECG_sorted_unique.csv", "w"))	
data = csv.reader(open('../../clean_data/5_25-5_26_ECG_sorted.csv', 'r'))
next(data)
data_list = next(data)
time = data_list[0]	
merge_data = data_list[:]
data = csv.reader(open('../../clean_data/5_25-5_26_ECG_sorted.csv', 'r'))
next(data)
for row in data:
	# print("row = ", row)
	# print("row[0] = ", row[0], ", time = ", time)
	# print("row[0] === time = ", row[0] == time)
	if row[0] == time:
		# print(row[4])
		for i in range(len(row)): 
			# print(row)
			if i is 4 or i is 7:
				new_sign = {}
				row[i] = row[i].replace("'",'"').replace("None", "0")
				row_json = json.loads(row[i])
				for key, value in row_json.items():
					if value 
					new_sign[key] = value
				print(new_sign)
				merge_data[i] = json.dumps(curr_pleth)


			# new_sign = {}

			# row[i].replace("'",'"').replace("None", "0")

		# 	print(i)
		# 	# print(row[i].replace("'",'"').replace("None", "0"), (row[i]))
		# break

		# new_pleth = {}
		# val = 'Respiration Rate'
		# new_pleth[val] = 0
		# new_pleth['etCO2'] = 0
		# # new_pleth = json.dumps(new_pleth)

		# curr_pleth = row[4].replace("'",'"').replace("None", "0")
		# curr_pleth = json.loads(curr_pleth)

		# if curr_pleth['Respiration Rate']: 
		# 	new_pleth['Respiration Rate'] = curr_pleth['Respiration Rate']

		# if curr_pleth['etCO2']: 
		# 	new_pleth['etCO2'] = curr_pleth['etCO2']

		# merge_data[4] = json.dumps(curr_pleth)

		# curr_BP = row[7].replace("'",'"').replace("None", "0")
		# curr_BP = json.loads(curr_BP)
		# # print("type(curr_BP) = ", type(curr_BP))
		# 	# print("curr_pleth = ", curr_BP)

		# new_BP = {}
		# new_BP['mean'] = 0
		# new_BP['systolic'] = 0
		# new_BP['diastolic'] = 0
		# # new_BP = json.dumps(new_BP)

		# if curr_BP['mean']:
		# 	# print("if curr_BP['mean'] true = ", row) 
		# 	new_BP['mean'] = curr_BP['mean']

		# if curr_BP['systolic']: 
		# 	# print("if curr_BP['systolic'] true = ", row) 
		# 	new_BP['systolic'] = curr_BP['systolic']

		# if curr_BP['diastolic']:
		# 	# print("if curr_BP['diastolic'] true = ", row) 
		# 	new_BP['diastolic'] = curr_BP['diastolic']

		# merge_data[7] = json.dumps(curr_BP)
		# print("if merge_data = ", merge_data) 
	else:
		# print("YOOO")
		g.writerow(merge_data)
		merge_data = row
		# print("new merge_data = ", merge_data)
		time = row[0]
		# print("changed time = ", time)
		new_pleth = {}
		new_pleth['Respiration Rate'] = 0
		new_pleth['etCO2'] = 0
		# new_pleth = json.dumps(new_pleth)

		curr_pleth = row[4].replace("'",'"').replace("None", "0")
		curr_pleth = json.loads(curr_pleth)

		if curr_pleth['Respiration Rate']: 
			# print("YAA")
			new_pleth['Respiration Rate'] = curr_pleth['Respiration Rate']

		if curr_pleth['etCO2']: 
			new_pleth['etCO2'] = curr_pleth['etCO2']

		merge_data[4] = json.dumps(curr_pleth)

		curr_BP = row[7].replace("'",'"').replace("None", "0")
		curr_BP = json.loads(curr_BP)
			# print("curr_pleth = ", curr_BP)

		new_BP = {}
		# print("1 new_BP = ", type(new_BP))
		new_BP['mean'] = 0
		# print("2 new_BP = ", type(new_BP))
		new_BP['systolic'] = 0
		# print("3 new_BP = ", type(new_BP))
		new_BP['diastolic'] = 0
		# print("4 new_BP = ", type(new_BP))
		# new_BP = json.dumps(new_BP)
		# print("new_BP = ", type(new_BP))
		if curr_BP['mean']:
			# print("if curr_BP['mean'] true = ", new_BP) 
			new_BP['mean'] = curr_BP['mean']

		if curr_BP['systolic']: 
			# print("if curr_BP['systolic'] true = ", row) 
			new_BP['systolic'] = curr_BP['systolic']

		if curr_BP['diastolic']:
			# print("if curr_BP['diastolic'] true = ", row) 
			new_BP['diastolic'] = curr_BP['diastolic']

		merge_data[7] = json.dumps(curr_BP)
		# print("else merge_data = ", merge_data) 
		# break


	# 	else:
	# 		final_list=[time]
	# 		final_list.extend(val_list)
	# 		final_list.append(alarm)
	# 		g.writerow(final_list)


	# 		val=row
			
	# 		val_dict = val[6]
	# 		val_dict = val_dict.replace("'",'"')
	# 		val_dict = val_dict.replace('u"','"')
	# 		val[6] = val_dict.replace('None','0')

	# 		val_dict = val[9]
	# 		val_dict = val_dict.replace("'",'"')
	# 		val_dict = val_dict.replace('u"','"')
	# 		val[9] = val_dict.replace('None','0')
			

	# 		val_list=[val[0],val[1],val[3],val[4],val[7],val[6],val[9],val[8]]
	# 		time=val[2]
	# 		alarm=val[5]
	
	# final_list=[time]
	# final_list.extend(val_list)
	# final_list.append(alarm)
	# g.writerow(final_list)

'''
with open('ECG_sample.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)
'''