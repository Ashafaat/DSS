from nltk.sentiment.vader import SentimentIntensityAnalyzer

f = open('tweets.txt')
text = f.read()
tweets = text.split('\n')
analyzer = SentimentIntensityAnalyzer()
file = open('sentimentResult.txt','w')
i = 0
for tweet in tweets:
    vs = analyzer.polarity_scores(tweet)
    file.write(str(vs['pos']))
    file.write(', ')
    file.write(str(vs['neg']))
    file.write(', ')
    file.write(str(vs['neu']))
    file.write(', ')
    file.write(str(vs['compound']))
    file.write('\n')
    i = i + 1
    print(i)