import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

recog1 = spr.Recognizer()

mc = spr.Microphone()

with mc as source:
	print("Say 'Hello' to initiate the translation!")
	print("----------------------------------------")
	recog1.adjust_for_ambient_noise(source, duration=0.2)
	audio = recog1.listen(source)
	MyText = recog1.recognize_google(audio)
	MyText = MyText.lower()

if 'hello' in MyText:
	translator = Translator()
	from_lang = 'en'
	to_lang = 'hi'
	with mc as source:
		
		print("Say a sentence...")
		recog1.adjust_for_ambient_noise(source, duration=0.2)
		
		audio = recog1.listen(source)
		
		get_sentence = recog1.recognize_google(audio)

		try:
			print("Phrase to be Translated :"+ get_sentence)
			text_to_translate = translator.translate(get_sentence,
													src= from_lang,
													dest= to_lang)
			
			text = text_to_translate.text

			speak = gTTS(text=text, lang=to_lang, slow= False)

			speak.save("captured_voice.mp3")	

			os.system("start captured_voice.mp3")

		except spr.UnknownValueError:
			print("Unable to understand the input")
			
		except spr.RequestError as e:
			print("Unable to provide the required output".format(e))
