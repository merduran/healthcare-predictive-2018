import csv
import operator
import json

## Sorting file based on timestamp
with open('../../clean_data/5-25_5-26_ECG.csv', 'r') as read_file:
	data = csv.reader(read_file)
	sortedlist = sorted(data, key=lambda row: row[0])
	g = csv.writer(open("../../clean_data/ECG_sorted.csv", "w"))
	g.writerow(['timestamp','ECG','Respiration Rate','SpO2','Pleth','Heart Rate','Airway','Non-invasive Blood Pressure','qos','alarms'])
	for el in sortedlist:
		g.writerow(el)

## Removing duplicates and merging values from different rows with same timestamp

g = csv.writer(open("ECG_sorted_unique.csv", "w"))
# g.writerow(['timestamp','ECG','Respiration Rate','SpO2','Pleth','Heart Rate','Airway','Non-invasive Blood Pressure','qos','alarms'])

with open('../../clean_data/ECG_sorted.csv', 'r') as read_file:
	data = csv.reader(read_file)
	next(data)
	data_list = next(data)
	time = data_list[0]	
	merge_data = data_list[:]
	for row in data:
		print("time 1 = ", time)
		print("row 1 = ", row)
		print("row[0] == time = ", row[0] == time)
		if row[0] == time:
			# print("time 2 = ", time)
			# print("row 2 = ", row)
			break
			# new_pleth = {}
			# new_pleth['Respiration Rate'] = 0
			# new_pleth['etCO2'] = 0
			# new_pleth = json.dumps(new_pleth)

			# curr_pleth = row[4].replace("'",'"').replace("None", "0")
			# curr_pleth = json.loads(curr_pleth)

			# if curr_pleth['Respiration Rate']: 
			# 	new_pleth['Respiration Rate'] = curr_pleth['Respiration Rate']
			# if curr_pleth['etCO2']: 
			# 	new_pleth['etCO2'] = curr_pleth['etCO2']
			# merge_data[4] = str(curr_pleth)

			# curr_BP = row[7].replace("'",'"').replace("None", "0")
			# curr_BP = json.loads(curr_BP)
			# print("curr_pleth = ", curr_BP)

			# new_BP = {}
			# new_BP['mean'] = 0
			# new_BP['systolic'] = 0
			# new_BP['diastolic'] = 0
			# new_BP = json.dumps(new_BP)

			# if curr_BP['mean']: 
			# 	new_BP['mean'] = curr_BP['mean']
			# if curr_BP['systolic']: 
			# 	new_BP['systolic'] = curr_BP['systolic']
			# if curr_BP['diastolic']: 
			# 	new_BP['diastolic'] = curr_BP['diastolic']

			# merge_data[7] = str(curr_BP)
			print("merge_data = ", merge_data)
			# print("merge_data[4] = ", merge_data[4])
			# print("temp_pleth = ", temp_pleth)
			# temp_pleth = json.loads(temp_pleth)
			# print("temp_pleth = ", temp_pleth)

	# 		temp_pleth.replace
	# 		row_list[5] = val_dict.replace('None','0')

	# 		val_next=json.loads(row_list[5])

	# 		#val_list[5]=json.loads(val_list[5])

	# 		if val_next['etCO2']!=0:
	# 			val_list[5]=row_list[5]

	# 		val_dict = row_list[6]
	# 		val_dict = val_dict.replace("'",'"')
	# 		val_dict = val_dict.replace('u"','"')
	# 		row_list[6] = val_dict.replace('None','0')

	# 		val_next=json.loads(row_list[6])
	# 		#val_list[6]=json.loads(val_list[6])

	# 		if val_next['diastolic']!=0:
	# 			val_list[6]=row_list[6]

	# 		if row[5]:
	# 			alarm=row[5]

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