import os
import sys
import openai
import pyttsx3
import speech_recognition as sr


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def talk(text):
    print("John:", text)
    pyttsx3.speak(text)


def query(text):
    res = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0, logprobs=5, echo=False, max_tokens=2000)
    all = [x['text'] for x in list(res['choices'])]
    return " ".join(all).strip()


def hidePrint(callback):
    old_stdout = sys.stdout  # backup current stdout
    sys.stdout = open(os.devnull, "w")
    result = callback()
    sys.stdout = old_stdout  # reset old stdout
    return result


def hasKey():
    try:
        f = open("api-key.txt", "r")
        openai.api_key = f.read()
    except:
        print("OpenAI: https://beta.openai.com/account/api-keys")
        talk("Please enter your OpenAI API Key to continue, if you dont have one check the link above:")
        key = input()
        openai.api_key = key
        f = open("api-key.txt", "w")
        f.write(key)
        f.close()


def capture():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        rec.pause_threshold = 1
        audio = rec.listen(source)
        try: return rec.recognize_google(audio, language='en-US')
        except Exception: return ""


def main():
    talk("Welcome to OpenAI with Speech Recognition")
    while (True):
        try:
            text = hidePrint(capture)
            if text != "":
                print("You:", text)
                talk(query(text))
        except Exception:
            talk("Unable to connect to OpenAI. (Make sure your API-KEY is correct)")


if __name__ == '__main__':
    hasKey()
    cls()
    main()
