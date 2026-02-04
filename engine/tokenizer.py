def tokenize(text):
    return [w.strip() for w in text.lower().split() if len(w) > 1]
