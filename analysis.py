#!/usr/bin/env python
# coding: utf-8
#from IPython import get_ipython
import pandas as pd

import requests
from bs4 import BeautifulSoup

def get_text_from_URL(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    paragraphs = soup.find_all('p')
    paragraph = []

    for i in paragraphs:
        paragraph.append(i.text.strip())

    all_paragraph = " ".join(paragraph)
    return all_paragraph


# ## Number Of Words with stopwords

# ### Remove Punctuation

# In[95]:


import string


def remove_punctuation(paragraph):
    # Create a translation table to remove punctuation
    paragraph = paragraph.replace(" ", '')
    paragraph = paragraph.replace("\n", '')
    paragraph = paragraph.replace("“", '')
    paragraph = paragraph.replace("’", '')
    paragraph = paragraph.replace("”", '')
    translator = str.maketrans("", "", string.punctuation)

    # Use translate to remove punctuation
    cleaned_paragraph = paragraph.translate(translator)

    return cleaned_paragraph


# ## Average Word Length

# In[96]:
def calculate_characters(all_paragraph):
    return len(remove_punctuation(all_paragraph))

# Average word length
def average_word_length(all_paragraph):
    number_of_characters = len(remove_punctuation(all_paragraph))
    number_of_words = count_words_with_stopwords(all_paragraph)
    avg_word_length = number_of_characters / number_of_words
    return int(avg_word_length)


# ## Personal Pronouns

# In[97]:


import re


def calculate_personal_pronouns(paragraph):
    pronoun_pattern = re.compile(
        r'\b(?:I|you|he|she|it|we|you|they|me|him|her|them|my|our|your|his|its|their|theirs|hers|yours|ours|mine)\b',
        re.IGNORECASE)

    # Find personal pronouns in the sentence
    personal_pronouns = pronoun_pattern.findall(paragraph)
    personal_pronouns = personal_pronouns + re.findall("us", paragraph)

    # Print the result
    return set(personal_pronouns)


# ## Tokenize and Remove Stopwords

# In[98]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('stopwords')
stopwords = stopwords.words('english')


# In[99]:


def tokenize_and_remove_stopwords(all_paragraph, stopwords):
    translator = str.maketrans("", "", string.punctuation)
    cleaned_paragraph = all_paragraph.translate(translator)
    cleaned_paragraph = cleaned_paragraph.replace('“', "")
    cleaned_paragraph = cleaned_paragraph.replace('’', "")
    cleaned_paragraph = cleaned_paragraph.replace('”', "")
    words = word_tokenize(cleaned_paragraph)
    filtered_words = [word for word in words if word.lower() not in stopwords]

    return filtered_words


def word_count_without_stopword(all_paragraph, stopwords):
    words = tokenize_and_remove_stopwords(all_paragraph, stopwords)
    return len(words)


# ## Count Syllables

# In[119]:


import pyphen


def count_syllables(word):
    dic = pyphen.Pyphen(lang='en_US')
    syllables = dic.inserted(word).count('-') + 1
    return syllables


def count_syllables_in_text(text):
    words = text.split()
    syllable_counts = [count_syllables(word) for word in words]
    return syllable_counts


# # Analysis of Readability
# Analysis of Readability is calculated using the Gunning Fox index formula described below
# 
# - Average Sentence Length = the number of words / the number of sentences
# - Percentage of Complex words = the number of complex words / the number of words 
# - Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)

# ## Average Sentence Length

# In[100]:


def count_words_with_stopwords(paragraph):
    words = paragraph.split()
    return len(words)


# In[101]:


def sentence_length(paragraph):
    return len(paragraph.split("."))


# In[102]:


# Average Sentence Length = the number of words / the number of sentences
def avg_sent_length(paragraph):
    number_of_words = count_words_with_stopwords(paragraph)
    no_of_sentence = sentence_length(paragraph)

    avg_sentence_length = number_of_words / no_of_sentence

    return int(avg_sentence_length)


# ## Complex Word Count

# In[122]:


def complex_word_count(all_paragraph, syllable_counts):
    count = 0
    syllable_counts = count_syllables_in_text(all_paragraph)
    for word, syllables in zip(all_paragraph.split(), syllable_counts):
        if syllables > 2:
            count = count + 1
    return count


# ## Percentage Of Complex Words

# In[104]:


# Percentage of Complex words = the number of complex words / the number of words
def percentage_complex_words(all_paragraph, syllable_counts, number_of_words):
    complex_count = complex_word_count(all_paragraph, syllable_counts)
    per_complex_words = (complex_count / number_of_words) * 100
    return per_complex_words


# ## Fog Index

# In[105]:


# Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)
def calculate_fox_index(avg_sentence_length, per_complex_words):
    fog_index = 0.4 * (avg_sentence_length + per_complex_words)
    return fog_index


# ## Polarity Score

# In[106]:


# Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
def calculate_polarity_score(positive_score_num, negative_score_num):
    polarity_score = (positive_score_num - negative_score_num) / ((positive_score_num + negative_score_num) + 0.000001)
    return polarity_score


# ## Subjectivity Score

# In[107]:


# Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
def calculate_subjective_score(filtered_words, positive_score_num, negative_score_num):
    num_cleaned_words = len(filtered_words)
    subjectivity_score = (positive_score_num + negative_score_num) / ((num_cleaned_words) + 0.000001)
    return subjectivity_score


# In[108]:


def calculate_speaking_time(word_count_without_stopwords):
    minutes = word_count_without_stopwords / 150
    minutes_part = int(minutes)
    seconds_part = int((minutes - minutes_part) * 60)
    return "{} minutes and {} seconds".format(minutes_part, seconds_part)


# ## Sentiment Analysis

# In[109]:


from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
from transformers import pipeline

# In[110]:


MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
pipe = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, max_length=4000, truncation=True)

summarizer = pipeline("summarization", model="Falconsai/text_summarization")


# In[111]:


# In[112]:


def polarity_scores_roberta(example):
    encoded_text = tokenizer(example, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        'negative_score': scores[0] * 100,
        'neutral_score': scores[1] * 100,
        'positive_score': scores[2] * 100
    }
    return scores_dict

classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)



# In[125]:


# Get text from the selected website

def calculate_details(url):
    all_paragraph = get_text_from_URL(url)

    if (not all_paragraph):
        print("No Text Extracted")
        return

    result = {}
    # Personal Pronouns
    personal_pronouns = calculate_personal_pronouns(all_paragraph)
    result["Personal Pronouns"] = personal_pronouns

    # Number Of Sentences
    no_of_sentence = sentence_length(all_paragraph)
    result["no_of_sentence"] = no_of_sentence

    # Average Sentence Length
    average_sentence_length = avg_sent_length(all_paragraph)
    result["average_sentence_length"] = average_sentence_length

    # Average Word Length
    avg_word_len = average_word_length(all_paragraph)
    result["avg_word_len"] = avg_word_len

    # Number Of Characters
    number_of_characters = calculate_characters(all_paragraph)
    result["number_of_characters"] = number_of_characters

    # Syllable Counts
    syllable_counts = sum(count_syllables_in_text(all_paragraph))
    result["syllable_counts"] = syllable_counts

    # Complex Word Count
    count_complex_word = complex_word_count(all_paragraph, syllable_counts)
    result["count_complex_word"] = int(round(count_complex_word,0))

    # Number Of Words with Stopwords
    number_of_words = count_words_with_stopwords(all_paragraph)
    result["number_of_words"] = number_of_words

    # Word Count
    word_count_without_stopwords = word_count_without_stopword(all_paragraph, stopwords)
    result["word_count_without_stopwords"] = word_count_without_stopwords

    # Speaking Time
    speaking_time = calculate_speaking_time(word_count_without_stopwords)
    result["speaking_time"] = speaking_time

    # Percentage Of Complex Words
    per_complex_words = percentage_complex_words(all_paragraph, syllable_counts, number_of_words)
    result["per_complex_words"] = round(per_complex_words, 1)

    # Fox Index
    fox_index = calculate_fox_index(average_sentence_length, per_complex_words)
    result["fox_index"] = round(fox_index, 1)

    filtered_words = tokenize_and_remove_stopwords(all_paragraph, stopwords)
    text = " ".join(filtered_words[0:400])
    scores = polarity_scores_roberta(text)

    # Positive Score
    positive_score_num = scores['positive_score']
    result["positive_score_num"] = round(positive_score_num,1)

    # Positive Score
    neutral_score_num = scores['neutral_score']
    result["neutral_score_num"] = round(neutral_score_num,1)

    # Negative Score
    negative_score_num = scores['negative_score']
    result["negative_score_num"] = round(negative_score_num, 1)

    # Polarity Score
    polarity_score = calculate_polarity_score(positive_score_num, negative_score_num)
    result["polarity_score"] = round(polarity_score,2)

    # Filtered Words
    filtered_words = tokenize_and_remove_stopwords(all_paragraph, stopwords)
    result["filtered_words"] = filtered_words

    # Subjective Score
    subjective_score = calculate_subjective_score(filtered_words, positive_score_num, negative_score_num)
    result["subjective_score"] = round(subjective_score, 2)

    #Text Summary
    summary = summarizer(all_paragraph, max_length=300, min_length=30, do_sample=False)
    result["summary"] = summary

    #Emotions
    emotions = classifier(text)
    emotions = pd.DataFrame(emotions[0])
    emotions =  emotions.sort_values(by=['score'], ascending=False)[:5]
    result["emotions"] = emotions

    return result


def calculate_text_details(all_paragraph):
    if (not all_paragraph):
        print("No Text Extracted")
        return

    result = {}
    # Personal Pronouns
    personal_pronouns = calculate_personal_pronouns(all_paragraph)
    result["Personal Pronouns"] = personal_pronouns

    # Number Of Sentences
    no_of_sentence = sentence_length(all_paragraph)
    result["no_of_sentence"] = no_of_sentence

    # Average Sentence Length
    average_sentence_length = avg_sent_length(all_paragraph)
    result["average_sentence_length"] = average_sentence_length

    # Average Word Length
    avg_word_len = average_word_length(all_paragraph)
    result["avg_word_len"] = avg_word_len

    # Number Of Characters
    number_of_characters = calculate_characters(all_paragraph)
    result["number_of_characters"] = number_of_characters

    # Syllable Counts
    syllable_counts = sum(count_syllables_in_text(all_paragraph))
    result["syllable_counts"] = syllable_counts

    # Complex Word Count
    count_complex_word = complex_word_count(all_paragraph, syllable_counts)
    result["count_complex_word"] = int(round(count_complex_word,0))

    # Number Of Words with Stopwords
    number_of_words = count_words_with_stopwords(all_paragraph)
    result["number_of_words"] = number_of_words

    # Word Count
    word_count_without_stopwords = word_count_without_stopword(all_paragraph, stopwords)
    result["word_count_without_stopwords"] = word_count_without_stopwords

    # Speaking Time
    speaking_time = calculate_speaking_time(word_count_without_stopwords)
    result["speaking_time"] = speaking_time

    # Percentage Of Complex Words
    per_complex_words = percentage_complex_words(all_paragraph, syllable_counts, number_of_words)
    result["per_complex_words"] = round(per_complex_words, 1)

    # Fox Index
    fox_index = calculate_fox_index(average_sentence_length, per_complex_words)
    result["fox_index"] = round(fox_index, 1)

    filtered_words = tokenize_and_remove_stopwords(all_paragraph, stopwords)
    text = " ".join(filtered_words[:439])
    scores = polarity_scores_roberta(text)

    # Positive Score
    positive_score_num = scores['positive_score']
    result["positive_score_num"] = round(positive_score_num,1)

    # Positive Score
    neutral_score_num = scores['neutral_score']
    result["neutral_score_num"] = round(neutral_score_num,1)

    # Negative Score
    negative_score_num = scores['negative_score']
    result["negative_score_num"] = round(negative_score_num, 1)

    # Polarity Score
    polarity_score = calculate_polarity_score(positive_score_num, negative_score_num)
    result["polarity_score"] = round(polarity_score,2)

    # Filtered Words
    filtered_words = tokenize_and_remove_stopwords(all_paragraph, stopwords)
    result["filtered_words"] = filtered_words

    # Subjective Score
    subjective_score = calculate_subjective_score(filtered_words, positive_score_num, negative_score_num)
    result["subjective_score"] = round(subjective_score, 2)

    #Text Summary
    summary = summarizer(all_paragraph, max_length=200, min_length=30, do_sample=False)
    result["summary"] = summary

    #Emotions
    emotions = classifier(text)
    emotions = pd.DataFrame(emotions[0])
    emotions =  emotions.sort_values(by=['score'], ascending=False)[:5]
    result["emotions"] = emotions

    return result
