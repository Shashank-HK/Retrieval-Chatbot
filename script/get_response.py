import sys
import zmq
import pickle
import glob
import pandas as pd
import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import numpy as np
from nltk.tokenize import word_tokenize
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow_hub as hub
from tensorflow.keras.models import load_model



ignore_stopwords = ['what','why','how','against','who','where','myself']
STOPWORDS = set(stopwords.words('english')) - set(ignore_stopwords)


module_url = "E:/Chatbot/universal-sentence-encoder_4"
encoder_model = hub.load(module_url)
print("Module loaded")

path = "e:/Chatbot/v2Frontend/script/"
intent_model = load_model(path+'saved/intent_model.h5')
with open(path+'saved/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open(path+'saved/cat_codes.pickle', 'rb') as handle:
    cat_codes = pickle.load(handle)

MAX_LENGTH = 50
TRUNCATE_TYPE = 'post'
PADDING_TYPE = 'post'


def cosine(u, v):
     return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

def getLemma(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

def cleanText(text):
    text = text.lower() 
    punct_table = str.maketrans(' ',' ',string.punctuation)
    text = text.translate(punct_table)
    text = [x for x in text.split() if not x in STOPWORDS]
    return ' '.join(text)

def getAnswer(query,category):
    similarities = []
    query_vec = encoder_model([query])[0]
    data_file = path+"Data/"+category+".csv"
    df = pd.read_csv(data_file, index_col=None, header=0)
    for index,question in enumerate(df['Question']):
        question = cleanText(question)
        sim = cosine(query_vec, encoder_model([question])[0])
        similarities.append((index,question,sim))
    similarities.sort(key = lambda x: x[2], reverse=True)
    if similarities[0][2]>0.5:
        answer = df.iloc[similarities[0][0]]['Answer']
    else:
        answer="Sorry I did not understand. I will need more information"
    return answer

def predict(query):
    prediction_probs = intent_model.predict(query)[0]
    prediction_index = np.argmax(prediction_probs)
    prediction = cat_codes[prediction_index]
    print(prediction)
    return prediction

def getResponse(query):
    query = cleanText(query)
    query = getLemma(query)
    query_tokenized = tokenizer.texts_to_sequences([query])
    query_pad = pad_sequences(query_tokenized, maxlen=MAX_LENGTH, padding=PADDING_TYPE, truncating=TRUNCATE_TYPE)
    predicted_class = predict(query_pad)
    answer = getAnswer(query,predicted_class)
    return answer

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:4242")

    print("Ready for input")
    while True:
        query = socket.recv()
        query = query.decode()
        response = getResponse(query)
        socket.send_string(response)
        #print(response,flush=True)
        
if __name__ == "__main__":
    main()



















