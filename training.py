import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

def load_feedback(file_path="emotion_corrections.csv"):
    print("📥 Checking for feedback file...")
    if not os.path.exists(file_path):
        print("❌ No feedback found. Run the bot and give some emotion corrections first.")
        return None
    try:
        df = pd.read_csv(file_path, names=["text", "detected", "correct"], encoding='utf-8')
        print(f"✅ Loaded {len(df)} feedback rows:")
        print(df.head())
        return df
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return None

def train_emotion_model(df):
    print("🧠 Starting training...")
    X = df["text"]
    y = df["correct"]

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X, y)

    joblib.dump(model, "emotion_model.pkl")
    print("✅ Training complete.")
    print("💾 Model saved as 'emotion_model.pkl'.")

def main():
    df = load_feedback()
    if df is not None and not df.empty:
        train_emotion_model(df)
    else:
        print("⚠️ Not enough data to train.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Fatal error: {e}")

