import pyttsx3

def speak(text):
    print(f"[TTS] Speaking: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed (default: 200)
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

