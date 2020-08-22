import pyttsx3
import os
import numpy

print("""******************************************************************
*                   Welcome to IIEC RISE                         *
*              Text to execute using python3                     *
******************************************************************
""",end='')

intructions = """******************************************************************
* Intructions to use:                                            *
* => Press 1 to login as admin,                                  *
* => Press 2 to login as user,                                   *
* => Press 3 for help,                                           *
* => Press 4 to exit.                                            *
******************************************************************
"""

helpMenu = """******************************************************************
* Role of Admin is to add or remove keywords to be used as a     *
*               form of accepted or reject from user.            *
* Role of User is to just relax and instruct program to start    *
*              the application in form of text.                  *
* Note: By default, a text from user will be taken as assertive  *
*       in manner                                                *
******************************************************************
"""

adminAction = """******************************************************************
* Ah! Welcome back, Master!                                      *
* Press 1 to add a accept keyword,                               * 
* Press 2 to remove a accept keyword,                            *
* Press 3 to add a deny keyword,                                 *
* Press 4 to remove a deny keyword,                              *
* Press 5 to add support for an application,                     *
* Press 6 to remove support for an application name,             *
* Press 7 for help,                                              *
* Press 8 for list of remaining enhancements in the application, *        
* Press 9 to get back to menu.                                   *
******************************************************************
"""

adminEnhancements= """******************************************************************
* Remaining Enhancements:
* 1. Add connection to DB to save role, keywords etc,
* 2. Allow changing details of an existing application,
* 3. Allow a file input which will have list of accept keywords,
* 4. Add functions to avoid program redundancy,
* 5. Add Use of macros instead of hard-coded integers and strings,
* 6. Add exception handling to handle incorrect input from user,
* 7. Add support to remove lower-case/upper-case dependency,
* 8. Place duplicate check for applications.
******************************************************************
"""

adminhelp = """******************************************************************
* Help:                                                          *   
* Accept keywords: Keywords which when found in the user input   *
*                  are to be considered for executing user       *  
*                  command                                       *  
* Deny keywords: Keywords which when found in the user input are *
*                to be considered for not executing user command *   
******************************************************************             
"""

#Accepted Keywords List
accKeyWords = ["Execute","execute","Run","run","start","Start","Trigger","trigger"]

#Deny Keywords List
denKeyWords = ["Dont ","dont ","no ","do not "]

#Application Name and their program name
suppApp = ["Chrome","chrome","browser","notepad","Notepad","editor","media"]
#Program name for application
appCmd = ["chrome","chrome","chrome","notepad","notepad","notepad","wmplayer"]

while True:
  print(intructions, end='')
#  print("chat with me with your requirements : "  , end='')
  role = int(input("Press a number to select your role: "))
  if(role==1):
    while True:
      print(adminAction, end='')
      action = int(input("Press a number to select action item: "))
      if(action==1):
        accKey = input("Enter accept keyword to be added: ")
        accKeyWords.append(accKey)
        print("Accepted Keywords: "+str(accKeyWords))
      elif(action==2):
        accKey = input("Enter accept keyword to be removed: ")
        accKeyWords.remove(accKey)
        print("Accepted Keywords: "+str(accKeyWords))
      elif(action==3):
        denKey = input("Enter deny keyword to be added: ")
        denKeyWords.append(denKey)
        print("Deny Keywords: "+str(denKeyWords))
      elif(action==4):
        denKey = input("Enter deny keyword to be removed: ")
        denKeyWords.remove(denKey)
        print("Deny Keywords: "+str(denKeyWords))
      elif(action==5):
        appName = input("Enter application name to add support: ")
        cmdName = input("Enter command name to trigger application: ")
        suppApp.append(appName)
        appCmd.append(cmdName)
        print("Applications supported: "+str(suppApp))
        print("Commands for application: "+str(appCmd))
      elif(action==6):
        appName = input("Enter application name to remove support for: ")
        confirm = input("If you're sure you want to remove support, type yes: ")
        if(confirm == "yes"):
          if(appName in suppApp):
            idx = suppApp.index(appName)
            suppApp.remove(appName)
            appCmd.pop(idx)
            print("Application support removed for: " + appName)
            print("Applications supported: "+str(suppApp))
            print("Commands for application: "+str(appCmd))
          else:
            print("Application is not supported currently!")
        else:
          print("Application support removal cancelled for: " + appName)
      elif(action==7):
        print(adminhelp,end='')
      elif(action==8):
        print(adminEnhancements,end='')
      elif(action==9):
        print("So long master.........")
        break
      else:
        print("Invalid input, Please try again!!!")  
  elif(role==2):
    action=input("Tell me my lord, how can I help you today: ")
    if(any(word in action for word in denKeyWords)):
      print("Alright! Alright! Alright! \n Seems like today I to rest.")
    elif(any(word in action for word in accKeyWords)):
      if(any(app in action for app in suppApp)):
        findings = [app for app in suppApp if app in action]
        idx = suppApp.idx(findings[0])    
        os.system(appCmd[idx])
    else:
      print("Operation not supported currently. Please request admin!")
  elif(role==3):
    print(helpMenu, end='')
  elif(role==4):
    print("Bye!")
    break
  else:  
    print("Invalid input, Please try again!!!")