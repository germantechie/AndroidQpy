import datetime

#Below is the sample list object of the Android.getSmsMessages output after reading the SMS.
sample = [{u'body': u'Rs.104.00 was spent on your Citi Card XXXXXXXXX80XX on 04-DEC-18 at Rouge Place. The available credit limit is now Rs. 12,608.04.', u'status': u'-1', u'read': u'0', u'address': u'AD-CITIBK', u'date': u'1543932311088', u'_id': u'10668', u'type': u'1'}, {u'body': u'Dear Customer, get 5% discount on ICICI Pru iProtect Smart term plan. Get life cover till 75 years of age in 3 steps at icicibank.com/iprulifecover .T&C apply', u'status': u'-1', u'read': u'0', u'address': u'MD-459159', u'date': u'1543928139311', u'_id': u'10666', u'type': u'1'}]

print("Count = " , len(sample) , " ObjectType - " , type(sample))

dt = datetime.datetime.fromtimestamp(int(u'1543932534022')/1000)
dt_no_ms = datetime.datetime.fromtimestamp(int(u'1543932311088')//1000)
print("With MilliSec - " , dt, " \nNo MilliSec - ", dt_no_ms)
print(dt.strftime('%d/%m/%Y'))

#print(sample[0])
#print(sample[1],"\n\n")

# for i in sample[0]:  # only for one single message
	# print(i, "::", sample[0][i])
print("\n...Looping through all messages .....")	
for cnt, msgDict in enumerate(sample):  # loop through all messages and print in Key::Value format
	for sngMsg in msgDict:
		if cnt < 2:  # restricting to print only 3(0+2) messages
			if sngMsg.startswith('date'):
				dtHuman = datetime.datetime.fromtimestamp(int(msgDict['date'])//1000)
				print(sngMsg, "::", dtHuman)
				del dtHuman
			else:
				print(sngMsg, "::", msgDict[sngMsg])
