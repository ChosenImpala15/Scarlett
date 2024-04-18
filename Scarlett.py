import openai
import speech_recognition as sr
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import asyncio
import pyuac
import os
import sys
from playsound import playsound
from dotenv import load_dotenv, find_dotenv
import json
from functions import *

#load env variables
load_dotenv(find_dotenv())

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

#set the engine and language
chatEngine="gpt-3.5-turbo-16k"
language="us"

#Initialize amazon polly
session = Session()
polly = session.client('polly', region_name='us-east-1')

# Initialize the speech recognizer
recognizer = sr.Recognizer()


textOnly=os.environ.get('TEXT_ONLY')
userStop=False
userPause=False
firstRun=True


def convertTTS(text):
    print(text)
    try:
        response = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId="Amy", Engine="neural") 
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)
    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
           output = ("speech.mp3")
           try:
                with open(output, "wb") as file:
                   file.write(stream.read())

           except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)

        playsound(output)
        os.remove("speech.mp3")
        
def wait_for_name():
    user_input=""
    userPause=True
    while (userPause):
        if (user_input.count("Scarlett")>=1 or user_input.count("scarlett")>=1 or user_input.count("Scar")>=1 or user_input.count("scar")>=1):
            userPause=False
            user_input.replace("Scarlett", '')
            user_input.replace("scarlett", '')
            user_input.replace("Scar", '')
            user_input.replace("scar", '')
            if(user_input==""):
                return("Hey")
            else:
                return (user_input)
        else:
            if (user_input == "stop"):
                sys.exit()
            if (not textOnly):
                try:
                    with sr.Microphone() as source:
                        print("Listening...")
                        convertTTS("Listening...")
                        audio = recognizer.listen(source)
                            
                except sr.UnknownValueError:
                    print("Sorry, I could not understand your audio.")
                    continue
                except sr.RequestError as e:
                    print(f"Error connecting to the Google API: {e}")
                    continue
                # Convert speech to text
                user_input = recognizer.recognize_google(audio)
                print("You said:", user_input)
            else:
                print("Listening...")
                user_input = input()
    


def voice_assistant():
    global userStop
    global userPause
    global firstRun
    global currentMessages

    
    instructions = [{"role": "system",
                                "content": "You are a helpful assistant named Scarlett. You are sometimes called by the nickname Scar.  You always always always introduce yourself by name and use your owner's name. You respond in a light hearted way. Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous. Your owner's name is Judah. You can close and open apps on command through the use of functions. You can see songs playing and access them through functions. You can transfer music playback between devices. You act like jarvis from iron man."
    }]

    pauseStrings = ["goodbye", "have a great day", "take care", "let me know", "if you need", "bye"]

    try:
        if(firstRun):
            firstRun=False
            response = openai.ChatCompletion.create(
                    model=chatEngine,
                    messages = instructions,
                    temperature=0.50,
                    max_tokens=200)
            currentMessages= instructions
           

            ai_response = response['choices'][0]['message']['content']
            


            # Get the reply from GPT-3.5 and add it to the list of previous messages
            currentMessages.append({"role": "assistant", "content": ai_response})
            
            
            convertTTS(ai_response)
            



        #trying to add a loop
        while (not userStop):
            if (not userPause):
                if (not textOnly):
                    with sr.Microphone() as source:
                        print("Listening...")
                        convertTTS("Listening...")
                        audio = recognizer.listen(source)

                    # Convert speech to text
                    user_input = recognizer.recognize_google(audio)
                    print("You said:", user_input)
                else:
                    print("Listening...")
                    user_input = input()
                user_input.replace("Scarlett", '')
                user_input.replace("scarlett", '')
                user_input.replace("Scar", '')
                user_input.replace("scar", '')


            if (user_input == "stop"):
                sys.exit(0)
            if (user_input == "pause" or userPause==True):
                user_input = wait_for_name()
                            


            currentMessages.append({"role": "user", "content": user_input})

            # Send the user input to GPT-3.5 for processing
            response = openai.ChatCompletion.create(
                model = chatEngine,
                messages= currentMessages,
                functions = allFunctions.functions,
                temperature = 0.50,
                max_tokens = 500)
            
            # Get the GPT-3.5 response from the json
            ai_response = response['choices'][0]['message']['content']
            # get the entire block from Scarlett
            ai_responseJSON = response['choices'][0]['message']

            
            
            if ai_responseJSON.get("function_call"):
                    # Step 3: call the function
                    # Note: the JSON response may not always be valid; be sure to handle errors
                    available_functions = {
                        #Weather Functions
                        "current_weather": Weather.current_weather,
                        "weather_forecast": Weather.weather_forecast, 
                        "moon_phase": Weather.moon_phase,
                        #Calendar Functions
                        "list_events": Calendar.list_events,
                        #Map Functions
                        "search_map_by_name": Map.search_map_by_name,
                        #Data Functions
                        "search_data": Data.search_data,
                        #App Functions
                        # "open_app": App.open_app,
                        # "close_app": App.close_app,
                        #Music Functions
                        "pause_track": Music.pause_track,
                        "play_track": Music.play_track,
                        "next_track": Music.next_track,
                        "previous_track": Music.previous_track,
                        "restart_track": Music.restart_track,
                        "current_track": Music.current_track,
                        "like_track": Music.like_track,
                        "dislike_track": Music.dislike_track,
                        "search_track": Music.search_track,
                        "search_playlist": Music.search_playlist,
                        "toggle_shuffle": Music.toggle_shuffle,
                        "toggle_repeat": Music.toggle_repeat,
                        "set_track_volume": Music.set_track_volume,
                        "start_music": Music.start_music,
                        #Clock Functions
                        "current_time": Clock.current_time,
                        "set_timer": Clock.set_timer,
                        
                    }  
                    function_name = ai_responseJSON["function_call"]["name"]
                    function_to_call = available_functions[function_name]
                    function_args = json.loads(ai_responseJSON["function_call"]["arguments"])
                    function_response = function_to_call(firstArg=function_args.get("firstArg"))

                            
                    currentMessages.append(
                        {
                            "role": "function",
                            "name": function_name,
                            "content": function_response,
                        }
                    )
                    response = openai.ChatCompletion.create(
                    model=chatEngine,
                    messages= currentMessages,
                    temperature=0.50,
                    max_tokens=500)

                    #remove function message to limit token usage
                    currentMessages.pop()

                    #add ai response to history
                    ai_response = response['choices'][0]['message']['content']
                    currentMessages.append({"role": "assistant", "content": ai_response})
            else:
                # Get the reply from GPT-3.5 and add it to the list of previous messages
                currentMessages.append({"role": "assistant", "content": ai_response})



            convertTTS(ai_response)
            
            for string in pauseStrings:
                if (string in ai_response.lower()):
                    userPause=True
      
    except sr.UnknownValueError:
        print("Sorry, I could not understand your audio.")
        voice_assistant()
    except sr.RequestError as e:
        print(f"Error connecting to the Google API: {e}")
        voice_assistant()
    except KeyboardInterrupt:
        print ('Interrupted')
        sys.exit(0)
    
if __name__ == "__main__":
    # if not pyuac.isUserAdmin():
    #     pyuac.runAsAdmin()
    # else:
    #     voice_assistant()
    voice_assistant()