
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# from rank_bm25 import BM25Okapi

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import re
# import gensim
import numpy as np
# from gensim.models import word2vec
# from gensim.models import KeyedVectors

# import gensim.downloader as api

# wv = api.load('word2vec-google-news-300')

EMBEDDING_FILE = './GoogleNews-vectors-negative300-SLIM.bin'
# wv = KeyedVectors.load_word2vec_format(EMBEDDING_FILE, binary=True)

# wv["html"]

# Download stopwords if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')

def read_pdf(filename):
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def read_text_file(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text

# Define the job description file and the list of resumes (PDF files)


# prompt: I have loaded Word2Vec dictionary, and I have a query and a set of documents, I want to represent the query and the text within documents in Word2Vec embedding to use cosine similarity and rank the documents from the most similar to query to the least

def get_word2vec_embedding(text):
    if len(text) == 0:
        return None
    wnl = WordNetLemmatizer()
    text = text.lower()
    # text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    words = nltk.word_tokenize(text)
    words = [
        wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(word, "n"), "a"), "v")
        for word in words if word not in stopwords.words('english')
        ]

    embedding = np.zeros(wv.vector_size)
    for word in words:
        if word in wv:
            embedding += wv[word]
    return embedding / len(words)


def rank_by_word2vec(job_description, resume_filenames):
    resumes = [read_pdf(filename) for filename in resume_filenames]
    query_embedding = get_word2vec_embedding(job_description)
    document_embeddings = [get_word2vec_embedding(resume) for resume in resumes]
    document_embeddings = [de for de in document_embeddings if de is not None]
    similarities = cosine_similarity([query_embedding], document_embeddings)[0]  * 100

    resume_filenames = [filename.split("/")[-1] for filename in resume_filenames]
    similarity_scores = list(zip(resume_filenames, similarities))

    # Rank the CVs based on similarity scores
    ranked_cvs = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Print the ranked CVs
    for cv, score in ranked_cvs:
        print(f"CV: {cv} - Similarity Score: {score}")

    return ranked_cvs


def rank_by_tfidf(job_description, resume_filenames):
    resumes = [read_pdf(filename) for filename in resume_filenames]
    for i, resume in enumerate(resumes):
        print(resume_filenames[i], "-> ", resume, "\n\n\n")
    # Preprocess the text data
    # stopwords = set(stopwords.words('english'))
    vectorizer = TfidfVectorizer(stop_words="english")
    job_description_vector = vectorizer.fit_transform([job_description])
    resume_vectors = vectorizer.transform(resumes)

    # Calculate cosine similarity between job description and each resume
    cosine_similarities = cosine_similarity(job_description_vector, resume_vectors).flatten() * 100
    resume_filenames = [filename.split("/")[-1] for filename in resume_filenames]

    similarity_scores = list(zip(resume_filenames, cosine_similarities))

    # Rank the CVs based on similarity scores
    ranked_cvs = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Print the ranked CVs
    for cv, score in ranked_cvs:
        print(f"CV: {cv} - Similarity Score: {score}")

    return ranked_cvs

def rank_by_bm25(job_description, resume_filenames):
    return []
    # resumes = [read_pdf(filename) for filename in resume_filenames]
    # # Preprocess the text data
    # # stopwords = set(stopwords.words('english'))
    # tokenized_corpus = [re.sub(r"[^a-z0-9 ]", "", document.lower()).split(" ") for document in resumes]
    # bm25 = BM25Okapi(tokenized_corpus)

    # tokenized_query = job_description.split(" ")

    # doc_scores = np.array(bm25.get_scores(tokenized_query))
    # resume_filenames = [filename.split("/")[-1] for filename in resume_filenames]

    # similarity_scores = list(zip(resume_filenames, doc_scores))

    # # Rank the CVs based on similarity scores
    # ranked_cvs = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # # Print the ranked CVs
    # for cv, score in ranked_cvs:
    #     print(f"CV: {cv} - Similarity Score: {score}")

    # return ranked_cvs
