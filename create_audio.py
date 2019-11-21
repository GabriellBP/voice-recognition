from hear_microphone import hear_microphone as hm
from gtts import gTTS
from playsound import playsound


# Create and reproduces the audio
def create_audio(audio):
    # Generating an audio with Google Text-to-Speech
    tts = gTTS(audio, lang='pt-br')
    # Saving the file
    tts.save('audios/audio.mp3')
    # Waiting save the file
    print("Learning what you said...")
    # Play the audio
    playsound('audios/audio.mp3')


def main():
    phrase = hm()
    create_audio(phrase)


if __name__ == "__main__":
    main()
