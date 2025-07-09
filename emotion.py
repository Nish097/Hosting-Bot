import os
import joblib
import text2emotion as te

# Load trained model if available
MODEL_PATH = "emotion_model.pkl"

if os.path.exists(MODEL_PATH):
    print("🧠 Using your trained emotion model...")
    model = joblib.load(MODEL_PATH)
    use_custom_model = True
else:
    print("📦 Using default emotion detector (text2emotion)...")
    use_custom_model = False

def detect_emotion(text):
    if use_custom_model:
        try:
            prediction = model.predict([text])[0]
            return prediction.capitalize()
        except Exception as e:
            print(f"⚠️ Model failed: {e}")
            return "Unknown"
    else:
        # Fallback to text2emotion
        emotion_scores = te.get_emotion(text)
        if not emotion_scores:
            return "Neutral"
        return max(emotion_scores, key=emotion_scores.get).capitalize()

