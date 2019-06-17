
import androidhelper, datetime
import re

droid = androidhelper.Android()

def test_message1():
  Allresult = droid.smsGetMessages(False) #returns all sms
  print('\n ----' , len(Allresult[1]) , ' All sms!, Read+Unread')

  countCiti = 0 
  for cnt, msgDict in enumerate(Allresult[1]):  # loop through all messages and print in Key::Value format
	   for sngMsg in msgDict:
		    if sngMsg.startswith('body'):  # Store the body part of the message.
		        textMsg = msgDict['body'] 
			
		    if sngMsg.startswith('date'):   # Store the raw date(epoch time) part of the message.
		        dtReadable = datetime.datetime.fromtimestamp(int(msgDict['date'])//1000) 
		
		    if sngMsg.startswith('address'):
		        #if bool(re.search('(C|c)(I|i)(T|t)(I|i)(B|b)(K|k)', msgDict['address'])):
		            #print("date :: ", dtReadable)
		            #countCiti = countCiti + 1
		            #del textMsg, dtReadable
		        
		        if bool(re.search("(B|b)(r|R)(o|O)", msgDict['address'])):
    		         textMsg = msgDict['body'] 
    		         dtReadable = datetime.datetime.fromtimestamp(int(msgDict['date'])//1000) 
    		         print(dtReadable, ':', msgDict['address'], " :: ", textMsg)
    		         countCiti = countCiti + 1
             
  print("\nTotal YouBro Msgs = ", countCiti)

if __name__ == '__main__':
  test_message1()
