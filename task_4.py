from textblob import TextBlob

# Sample reviews
reviews = ['Great product!', 'Very bad service', 'It was okay']

# Analyze sentiment
for r in reviews:
    analysis = TextBlob(r)
    print(f'Review: {r} | Sentiment: {analysis.sentiment}')
