from pyicloud import PyiCloudService
import os
from dotenv import load_dotenv, find_dotenv
import re
from icecream import ic


def get_contacts(firstArg = None):
    allContactsText = ""

    load_dotenv(find_dotenv())
    api = PyiCloudService(os.environ.get("APPLE_ID"))

    contacts = api.contacts.all()

    for contact in contacts:
        try:
            if "firstName" in contact and "phones" in contact:
                firstName = re.sub('\W', "" ,contact.get('firstName'))
                numberList = contact.get('phones',[0])
                for item in numberList:
                    number = re.sub('[^0-9.]', "", item.get('field'))
                if(number==None or firstName==None):
                    pass
                fullContact = firstName.lower(),number
            
            else:
                pass
            if(fullContact!=None):
                allContactsText+=str(fullContact)
        except:
            pass
    return (allContactsText)

# no good way to send texts through python without spending a lot of money :(
# def text_contact(firstArg):
#     search = firstArg

#     textOnly=os.environ.get('TEXT_ONLY')

#     allContacts = get_contacts()
    
#     yes = {'yes','y', 'ye', ''}
#     no = {'no','n'}

#     yesText = False

#     for x in range(len(allContacts)-1):
#         if search in allContacts[x][0]:
#             if (not textOnly):
#                 recognizer = sr.Recognizer()
#                 with sr.Microphone() as source:
#                     print("What would you like to say?")
#                     listening = gTTS(text="What would you like to say?", lang='en', tld="us")
#                     listening.save('WWYLTS.mp3')
#                     playsound('WWYLTS.mp3')
#                     os.remove("WWYLTS.mp3")
#                     audio = recognizer.listen(source)

#                     # Convert speech to text
#                     user_input = recognizer.recognize_google(audio)
#                     print("You said:", user_input)
#                     print("Send it?")
#                     user_answer = recognizer.recognize_google(audio)
#                     if (user_answer.lower()=='yes'):
#                         #TODO
#                         #make text thingy :)
#                         print()
#                     elif(user_answer.lower()=="no"):
#                         return "cancelled"

#             else:
#                 print("What would you like to say?")
#                 user_input = input()
#                 user_answer = input("You wrote: ", user_input," Send it?(y/n)")
#                 while (not yesText):
#                     if user_answer in yes:
#                         #TODO
#                         #make text thingy :)
#                         yesText=True
#                         return "Text sent successfully"
#                     elif user_answer in no:
#                         #TODO
#                         #don't send text :D
#                         return "Cancelled"
#                     else:
#                         print("Please say yes or no")
#                         #redundant but set again for readability
#                         yesText=False

#         else:
#             pass
    
if __name__ == '__main__':
    ic(get_contacts())