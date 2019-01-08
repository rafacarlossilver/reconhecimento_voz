from gtts import gTTS
tts = gTTS('Oi, eu sou a Vick', lang="pt-br")
tts.save('audios/hello.mp3')