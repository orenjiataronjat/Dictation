import speech_recognition as sr
from pynput.keyboard import Key, Controller

keyboard = Controller()
r = sr.Recognizer()

#Make sure it doesn't record so long that it gets hung up on translating
def recordAudio(): #make it so it records audio for only a period of time 
	with sr.Microphone() as source:
		print('start speaking or say please quit dictation')
		audio = r.listen(source)
		return audio

def audioToText(audio):
	try:
		detectedText = r.recognize_google(audio) 
		print(detectedText)
		return detectedText.lower()
	except sr.UnknownValueError:
			return ''

while 1: #can I recognize a voice?? potentially assign different people to it
	audio = recordAudio()
	text = audioToText(audio)
	if text == 'please quit dictation':
		exit()
	if text != '':
		keyboard.type(text)
		keyboard.press(Key.enter)