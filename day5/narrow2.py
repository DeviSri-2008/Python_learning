def sentiment(text):
    pos = ["good","great","happy"]
    neg = ["bad","sad","poor"]
    text = text.lower()
    if any(w in text for w in pos):
        return "positive"
    elif any(w in text for w in neg):
        return "negative"
    else:
        return "neutral"
print(sentiment("this is a great day"))
 
