import string

# mood keyword dictionaries
MOODS = {
    "happy": ["love", "joy", "smile", "sun", "happy"],
    "sad": ["cry", "lonely", "sad", "dark", "tears"],
    "calm": ["peace", "dream", "soft", "slow", "calm"],
    "energetic": ["fire", "wild", "dance", "fast", "run"]
}

# read lyrics from the file and return as list of words
def load_lyrics(filename):
    with open(filename, "r") as f:
        text = f.read().lower()
        # remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()
    return words

# count mood related words and return results
def analyze_mood(words):
    counts = {mood: 0 for mood in MOODS}

    for word in words:
        for mood, keywords in MOODS.items():
            if word in keywords:
                counts[mood] += 1

    total = sum(counts.values())
    if total == 0:
        return counts, "neutral"

    # calculate percentages
    percentages = {mood: round((count / total) * 100, 2) for mood, count in counts.items()}

    # find predicted mood
    predicted = max(counts, key=counts.get)
    return percentages, predicted

# main function
def main():
    words = load_lyrics("lyrics.txt")
    percentages, predicted = analyze_mood(words)

    print("\n--- Music Mood Analyzer ---")
    for mood, perc in percentages.items():
        print(f"{mood.capitalize():<10}: {perc}%")
    print(f"\nPredicted Mood: {predicted.capitalize()}")

# run main
if __name__ == "__main__":
    main()
