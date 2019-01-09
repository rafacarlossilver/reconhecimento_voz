from gtts import gTTS
from subprocess import call
def cria_audio(audio):
    tts = gTTS(audio, lang="pt-br")
    tts.save('audios/bem_vindo.mp3')
    call(['mpg123',"audios/bem_vindo.mp3"])

cria_audio("ola Nelson tudo bom, fassa como os turcos")