import json
import time
from emotion import detect_emotion
from voice import speak
from jokes import get_random_joke

def run_show():
    with open("script.json", "r") as file:
        script = json.load(file)

    print("🎤 Starting the AI Show Host...\n")
    
    for item in script:
        text = item["text"]
        
        section = item["section"]
        emotion = detect_emotion(text)
        print(f"[{section}] ({emotion}) -> {text}")
        
        speak(text)
        
                # Ask for feedback to help the bot learn emotions
        try:
            feedback = input(f"❓ Was the emotion correct for: '{text}'? (yes/no/custom): ").strip().lower()

            if feedback == "no":
                correct = input("👉 What should it be? (e.g., Happy, Sad, Angry): ").strip()
                with open("emotion_corrections.csv", "a", encoding="utf-8") as f:
                    f.write(f"{text},{emotion},{correct}\n")

            elif feedback not in ["", "yes"]:
                with open("emotion_corrections.csv", "a", encoding="utf-8") as f:
                    f.write(f"{text},{emotion},{feedback}\n")

        except Exception as e:
            print(f"⚠️ Skipping feedback due to error: {e}")


        time.sleep(2)
        
        if section.lower() == "joke":
            bonus_joke = get_random_joke()
            print(f"[Bonus Joke] -> {bonus_joke}")
            speak(bonus_joke)
            time.sleep(2)

    print("\n🎉 Show finished!")

if __name__ == "__main__":
    run_show()

