import androidhelper, datetime
import re

droid = androidhelper.Android()

def test_message1():
  Allresult = droid.smsGetMessages(False) #returns all sms
  # Allresult = [{u'body': u'The available credit limit is now Rs. 12,608.04.', u'status': u'-1', u'read': u'0', u'address': u'AD-CITIBK', u'date': u'1543932311088', u'_id': u'10668', u'type': u'1'}, 
  #              {u'body': u'Dear Customer, get 5% discount', u'status': u'-1', u'read': u'0', u'address': u'MD-459159', u'date': u'1543928139311', u'_id': u'10666', u'type': u'1'}
  #			    ]
  countCiti = 0 
  for cnt, sngMsgKeyDict in enumerate(Allresult[1]):  # loop through all messages and print in Key::Value format
	if bool(re.search("(C|c)(I|i)(T|t)(I|i)(B|b)(K|k)", sngMsgKeyDict['address'])):  # using regular expr, checking if the Address name is CITIBK or citibk.
		countCiti = countCiti + 1
		
		if countCiti < 5:  # execute below statements if count is less than the given number
			dtReadable = datetime.datetime.fromtimestamp(int(sngMsgKeyDict['date'])//1000) # Convert the raw date(epoch time) part of the message.
			textMsg = sngMsgKeyDict['body'] # Store the body part of the message.
			print sngMsgKeyDict['address'], " :: ", textMsg
			print "date :: ", dtReadable 
	
  #print "\nTotal Citibk Msgs = ", countCiti
  print '\n ----' , len(Allresult[1]) , ' All sms!, Read+Unread'

if __name__ == '__main__':
  test_message1()
