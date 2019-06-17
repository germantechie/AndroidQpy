
import androidhelper, datetime
import re

droid = androidhelper.Android()

def test_message1():
  Allresult = droid.smsGetMessages(False) #returns all sms
  print('\n ----' , len(Allresult[1]) , ' All sms!, Read+Unread')

  countFilterMsg = 0
  startService = 0
  stopService = 0
  print("\nHalt_Minutes  Start", (' ')*18 , "Stop", (' ')*18)
  print("\n", ('-')*18)

  for cnt, msgDict in enumerate(Allresult[1]):  # loop through all messages and print in Key::Value format
      for sngMsg in msgDict:
          if sngMsg.startswith('address'):
              if bool(re.search("(Y|y)(O|o)(U|u)(B|b)(r|R)(o|O)", msgDict['address'])):
                  textMsg = msgDict['body'] 
                  dtReadable = datetime.datetime.fromtimestamp(int(msgDict['date'])//1000)
                  #print(dtReadable, ':', msgDict['address'], " :: ", textMsg)
                  countFilterMsg = countFilterMsg + 1
              
                  if bool(re.search("We regret to inform", textMsg)):
                      stopService = int(msgDict['date']) # capture epoch time for that event
                      
                  if bool(re.search("We are pleased to inform", textMsg)):
                      startService = int(msgDict['date']) # capture epoch time for that event
                  
                  if startService != 0 and stopService != 0:
                      epochDiffMillisec = startService - stopService
                      strT = datetime.datetime.fromtimestamp(int(startService)//1000)
                      endT = datetime.datetime.fromtimestamp(int(stopService)//1000)
                      inMinutes = int(epochDiffMillisec/(60*1000))
                      print(inMinutes, strT, endT)
                      startService = 0
                      stopService = 0

             
  print("\nTotal YouBro Msgs = ", countFilterMsg)
  
if __name__ == '__main__':
  test_message1()
