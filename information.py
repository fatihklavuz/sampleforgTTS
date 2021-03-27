from gtts import gTTS
import os
f=open('bilgilendirme.txt')
x=f.read()
langa='tr'
audio=gTTS(text=x,lang=langa,slow=False)
audio.save('bilgilendirme.mp3')
os.system('bilgilendirme.mp3')
