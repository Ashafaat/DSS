data = []
hashtags = []
countries = []

# extract data from text file and fill data variable
f = open('hashtag.txt')
text = f.read()
rows = text.split('\n')
for row in rows:
    array = row.split('\t')
    data.append(array)

# find all countries and hashtags
for row in data:
    hashtag = row[2].split(',')
    country = row[1]
    if (not country in countries):
            countries.append(country)
    for tag in hashtag:
        if (not tag in hashtags):
            hashtags.append(tag)
hashtags.remove('')
countries.remove('')

# create result file of hashtag repetition
hashtagFile = open('hashtagResult.txt','w')
for hashtag in hashtags:
    counter = 0
    for tweet in data:
        tweetHashtags = tweet[2].split(',')
        if '' in tweetHashtags:
            tweetHashtags.remove('')
        if hashtag in tweetHashtags:
            counter = counter + 1
    hashtagFile.write(hashtag)
    hashtagFile.write(',')
    hashtagFile.write(str(counter))
    hashtagFile.write('\n')
    print(counter)

# create result file of hashtag repetition by country
hashtagByCountriesFile = open('hashtagResultByCountries.txt','w')
for country in countries:
    for hashtag in hashtags:
        counter = 0
        for tweet in data:
            if tweet[1] == country:
                tweetHashtags = tweet[2].split(',')
                if '' in tweetHashtags:
                    tweetHashtags.remove('')
                if hashtag in tweetHashtags:
                    counter = counter + 1
        hashtagByCountriesFile.write(country)
        hashtagByCountriesFile.write(',')
        hashtagByCountriesFile.write(hashtag)
        hashtagByCountriesFile.write(',')
        hashtagByCountriesFile.write(str(counter))
        hashtagByCountriesFile.write('\n')
        print(counter)