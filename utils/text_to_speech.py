import pyttsx3


'''
Function that recieves a list of words to read out loud
'''
def text_to_speech(lables):

    # init text to speech agent
    speaker = pyttsx3.init()
    # add each lable to the speaker
    for label in lables:
        if label.description != None:
            speaker.say(label.description)
            
    # run the agent
    speaker.runAndWait()