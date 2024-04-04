from random import randint

print("Tai , Xiu:")
import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("robot: I'm Listening ")
	audio = robot_ear.listen(mic)

try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""

nhacai = randint(0,1)

if nhacai == 0:
	nhacai = "hello"
if nhacai == 1:
	nhacai = "hi"

print("You:" + you)
print("Nhacai:" + nhacai)

if you == nhacai:
	robot_brain = "you win"
	print("You Win")
else:
	if you == "hello":
		if nhacai == "hi":
			robot_brain = "you lose"
			print("You Lose")
	elif you == "hi":
		if nhacai	== "hello":
			robot_brain = "you lose"
			print("You Lose")
	else:
		print("Nhap Cung Ngu Nua!")
import pyttsx3


robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
