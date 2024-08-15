import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis, Sir. Please tell me how I can help you.")
    speak("Hamza is a good boy")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")

    except Exception as e:
        print("Say That Again Please....")
        return "None"
    return query

def send_email():
    # Replace with your email and password
    sender_email = "your_191400038@gift.edu.pk"
    password = "your_hamza 789"
    receiver_email = "hamza.malik4352@gmail.com"
    subject = "Test Email"
    body = "This is a test email sent from Jarvis."

    # Create a MIMEText object to represent the email body
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message["Subject"] = subject
    email_message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Assuming Gmail SMTP
            server.starttls()  # Start TLS encryption
            server.login(sender_email, password)  # Login to the email server
            server.send_message(email_message)  # Send the email

        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
        speak("Sorry, I encountered an error while sending the email. Please try again later.")

if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()

    # Logic 
    if 'wikipedia' in query:
        speak('Searching Wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com/")

    elif "open google" in query:
        webbrowser.open("https://www.google.com/")
    
    elif "open stack overflow" in query:
        webbrowser.open("https://stackoverflow.com/")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Hamza, the time is {strTime}")

    elif "open code" in query:
        codePath = "C:\\Users\\Pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
    elif "open assignment" in query:
        assignmentPath = "C:\\Users\\Pc\\Desktop\\Assignment"
        os.startfile(assignmentPath)
    
    elif "send email" in query:
        send_email()
