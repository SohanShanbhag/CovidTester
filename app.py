#The NSSS Covid-19 Tester#
import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init()

count = ""
count2 = ""

query = ""
query2 = ""
query3 = ""
query4 = ""
query5 = ""

#rate#
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)

#voice#
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

def myCommand():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:
        print("Hello and Welcome to NSSS Covid-19 Self-Tester !")
        
        print("\nListening...")
        engine.say("Hello and Welcome to N triple s Covid-19 Self-Tester!! Would You Like To check Your Symptoms For Coronavirus")
        engine.runAndWait()
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('You Said : ' + str(query) + '\n')
        
    except sr.UnknownValueError:
        engine.say('Sorry! I didn\'t get that! You might want to type in YES OR NO!')
        engine.runAndWait()
        
        query = str(input("Enter 'YES' or 'NO' : "))

    return query

query = myCommand()
query = query.lower()

if ("yes" in query):

    def myCommand():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:           
            print("Okay. What is your age [ in integers ] ?")
            engine.say("Okay. What is your age?")
            engine.runAndWait()
            print("\nListening.....")
            r.pause_threshold =  1
            audio = r.listen(source)
        try:
            query1 = r.recognize_google(audio, language='en-in')
            print('You Said : ' + str(query1) + '\n')
            
        except sr.UnknownValueError:
            engine.say('Sorry! I didn\'t get that! You might want to type in your age')
            engine.runAndWait()
            
            query1 = str(input("Enter your age : "))

        return query1

    query1 = myCommand()
    query1 = query1.lower()

    query1 = int(query1)

    if(query1 > 65):
        count = 1
    if(query1 < 65):
        count = 0
    
    def myCommand():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:           
            print("Okay. Do you have any of the following? \n *Cough \n *Fever or chills \n *Shortness of breath or difficulty breathing \n *Muscle or body aches \n *Sore throat \n *New loss of taste or smell \n *Diarrhea \n *Headache \n *Nausea or vomiting ")
            engine.say("Okay. Do you have any of the following?")
            engine.runAndWait()
            print("\nListening.....")
            r.pause_threshold =  1
            audio = r.listen(source)
        try:
            query2 = r.recognize_google(audio, language='en-in')
            print('You Said : ' + str(query2) + '\n')
            
        except sr.UnknownValueError:
            engine.say('Sorry! I didn\'t get that! You might want to type in YES OR NO for your symptom check!')
            engine.runAndWait()
            
            query2 = str(input("Enter 'YES' or 'NO' for symptoms : "))

        return query2

    query2 = myCommand()
    query2 = query2.lower()
    if("yes" in query2):
        count1 = 1
    elif("no" in query2):
        count1 = 0

    def myCommand():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:           
            print("Have you had close contact with someone diagnosed with COVID-19 or been notified that you may have been exposed to it?")
            engine.say("Have you had close contact with someone diagnosed with COVID-19 or been notified that you may have been exposed to it?")
            engine.runAndWait()
            print("\nListening.....")
            r.pause_threshold =  1
            audio = r.listen(source)
        try:
            query3 = r.recognize_google(audio, language='en-in')
            print('You Said : ' + str(query3) + '\n')
            
        except sr.UnknownValueError:
            engine.say('Sorry! I didn\'t get that! You might want to type in YES OR NO for your symptom check!')
            engine.runAndWait()
            
            query3 = str(input("Enter 'YES' or 'NO' for symptoms : "))

        return query3

    query3 = myCommand()
    query3 = query3.lower()
    if("yes" in query3):
        count2 = 2
    elif("no" in query3):
        count2 = 1

    totalC = count+count1

    if(totalC <=1):
        print("Based on your Answers, you are at low risk. But, taking precautions is always good for you, your family and all of us. Stay Home and Stay Safe!")
        engine.say("Based on your Answers, you are at low risk. But, taking precautions is always good for you, your family and all of us. Stay Home and Stay Safe!")
        engine.runAndWait()

    if(totalC >= 2):
        print("Based on your Answers, you are at high risk. Consult a doctor as soon as you can. It doesn't mean that you have the virus with symptoms, but treating symptoms keeps you and your family on the safer side. Take Care.")
        engine.say("Based on your Answers, you are at high risk. Consult a doctor as soon as you can. It doesn't mean that you have the virus with symptoms, but treating symptoms keeps you and your family on the safer side. Take Care.")
        engine.runAndWait()

    if(count2 == 2):
        print("Contact a health care provider as you have been in close contact with someone diagnosed. The provider may have a solution for keeping yourself safe. Please Stay Home!")
        engine.say("Contact a health care provider as you have been in close contact with someone diagnosed. The provider may have a solution for keeping yourself safe. Please Stay Home!")
        engine.runAndWait()

    def myCommand():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:           
            print("WHO - World Health Organization - has some tips and latest information about Coronavirus. Would you like to check it out? All links we open are safe and secure!")
            engine.say("W H O - World Health Organization - has some tips and latest information about Coronavirus. Would you like to check it out? All links we open are safe and secure!")
            engine.runAndWait()
            print("\nListening.....")
            r.pause_threshold =  1
            audio = r.listen(source)
        try:
            query4 = r.recognize_google(audio, language='en-in')
            print('You Said : ' + str(query4) + '\n')
            
        except sr.UnknownValueError:
            engine.say('Sorry! I didn\'t get that! You might want to type in YES OR NO for your symptom check!')
            engine.runAndWait()
            
            query4 = str(input("Enter 'YES' or 'NO' for symptoms : "))

        return query4

    query4 = myCommand()
    query4 = query4.lower()

    if("yes" in query4):
        webbrowser.open_new("https://www.who.int/health-topics/coronavirus#tab=tab_1")
        print("All right, opening WHO")
        engine.say("All Right, opening W H O")
        engine.runAndWait()   
    if("no" in query4):
        print("Okay. You can test again at any time")
        engine.say("Okay. You can test again at any time")
        engine.runAndWait()

else:
    if("no" in query):
        print("Okay. That's not a problem. Stay Home and Stay Safe")
        engine.say("Okay. That's not a problem. Stay Home and Stay Safe")
        engine.runAndWait()
        exit(0)