import nltk

print nltk.__version__
exit(0)

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(tweets)
    return all_words


def get_word_features(wordlist):
    l = []
    for li, senti in wordlist:
        for w in li:
            l.append(w)
    wordlist = l
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def extract_features(document):
    global word_features
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))

"""
The new list of tweets will now look like this:
tweets =  [
    (['love', 'this', 'car'], 'positive'),
    (['this', 'view', 'amazing'], 'positive'),
    (['feel', 'great', 'this', 'morning'], 'positive'),
    (['excited', 'about', 'the', 'concert'], 'positive'),
    (['best', 'friend'], 'positive'),
    (['not', 'like', 'this', 'car'], 'negative'),
    (['this', 'view', 'horrible'], 'negative'),
    (['feel', 'tired', 'this', 'morning'], 'negative'),
    (['not', 'looking', 'forward', 'the', 'concert'], 'negative'),
    (['enemy'], 'negative')]


Note: here, we have used a rule based on the length etc. We have to define our own domain specific rules.

"""
# TODO: define rules for domain specific games.

test_tweets = [
    (['feel', 'happy', 'this', 'morning'], 'positive'),
    (['larry', 'friend'], 'positive'),
    (['not', 'like', 'that', 'man'], 'negative'),
    (['house', 'not', 'great'], 'negative'),
    (['your', 'song', 'annoying'], 'negative')]

word_features = get_word_features(get_words_in_tweets(tweets))
# print word_features
# print extract_features(["love","this","car"])


training_set = nltk.classify.apply_features(extract_features, tweets)
print training_set
classifier = nltk.NaiveBayesClassifier.train(training_set)
print "FINAL: ", classifier.classify(extract_features("she is a good girl".split()))
###################################################################
























"""
def word_feats(words):
	return dict([(word, True) for word in words])

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4

trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))

classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()
"""
