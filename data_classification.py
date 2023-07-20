import pandas as pd
from collections import Counter
import re
from tqdm import tqdm
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('punkt')

lemmatizer = WordNetLemmatizer()

emolex_df = pd.read_csv('NRC-Emotion-Lexicon-Wordlevel-v0.92.txt', names=["word", "emotion", "association"], sep='\t')
emolex_words = emolex_df.pivot(index='word', columns='emotion', values='association').reset_index()

poems_df = pd.read_csv('poems.csv')


def clean_text(text):
    text = text.lower()

    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation

    words = nltk.word_tokenize(text)

    lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]

    text = ' '.join(lemmatized_words)

    return text


poems_df['Cleaned_Poem'] = poems_df['Poem'].apply(clean_text)


def get_emotion(text):
    emotion_scores = Counter()

    words = re.findall(r'\b\w+\b', text)

    for word in words:
        # print(word)
        if word in emolex_words['word'].values:
            # print(word)
            # print(emolex_words)
            emotion_score = emolex_words.loc[emolex_words['word'] == word].iloc[0][1:]
            emotion_scores += emotion_score
            # print(emotion_scores)
            # print(emotion_score)

    emotion_scores.pop('positive', None)
    emotion_scores.pop('negative', None)

    if not emotion_scores:
        # print("Neutral")
        return "Neutral"

    # print(emotion_scores.most_common(1)[0][0])
    return emotion_scores.most_common(1)[0][0]


with tqdm(total=len(poems_df)) as pbar:
    for i in range(len(poems_df)):
        poems_df.loc[i, 'Emotion'] = get_emotion(poems_df.loc[i, 'Cleaned_Poem'])
        pbar.update(1)

poems_df.to_csv('poems_with_emotions.csv', index=False)
