import speech_recognition as sr
from gtts import gTTS


def hear_file():
    sentence = ""
    r = sr.Recognizer()
    umbrella = sr.AudioFile('audios/umbrella.wav')
    with umbrella as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        print(type(audio))
    try:
        print("Listening...")
        sentence = r.recognize_google(audio)
        print(sentence)
        print(len(sentence))
    except sr.UnkownValueError:
        # Can't recognize the speech
        print("I don't understand! :(")
    return sentence


if __name__ == "__main__":
    hear_file()
