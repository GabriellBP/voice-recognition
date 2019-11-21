import speech_recognition as sr


# Function to hear and recognize the speech
def hear_microphone():
    phrase = ""
    # Enables the microphone to hear the user
    microphone = sr.Recognizer()
    # Using the microphone
    with sr.Microphone() as source:
        # Reduces noise
        microphone.adjust_for_ambient_noise(source)
        print("Say something: ")
        # Captures microphone input and stores the information
        audio = microphone.listen(source)
    try:
        # Tries to recognizes the pattern
        phrase = microphone.recognize_google(audio, language='pt-BR')
        # Returns the sentence
        print('Did you say "' + phrase + '"?')
    except sr.UnkownValueError:
        # Can't recognize the speech
        print("I don't understand! :(")
    return phrase


def main():
    hear_microphone()


if __name__ == "__main__":
    main()