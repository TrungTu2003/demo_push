import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("robot: I'm Listening ")
	audio = robot_ear.listen(mic)

try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""


if you == "":
	robot_brain= "I can't hear you, try again"
elif you == "hello":
	robot_brain ="Hello Trung"
elif you == "today":
	robot_brain = "Monday"
elif you == "my love":
	robot_brain = "Pham Thi Hong Nhung"
elif you == "stupid":
	robot_brain = "Dong Ba Yen"
else:
	robot_brain = "I'm fine thank you and you"

print("You:" + you)
print(robot_brain)

import pyttsx3

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()