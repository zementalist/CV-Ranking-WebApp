import uvicorn

from fastapi import FastAPI, HTTPException, Query, Depends, Body, UploadFile, Form, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from datetime import datetime, timedelta

import os
import time
import unicodedata

from typing import Annotated, List, Optional
from math import nan

from resume import rank_by_tfidf, rank_by_word2vec,rank_by_bm25,  read_text_file, read_pdf


app = FastAPI()
ActionFactory = None
app.mount("/assets", StaticFiles(directory="portal\\dist\\assets"), name="assets")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])


@app.get("/")
def home():
    response= FileResponse("portal\dist\index.html")
    return response


cvs_path = "./cvs/"
allowed_extensions = [".pdf"]
job_description_path = "job.txt"

@app.get("/rank/{algorithm}")
def rank(algorithm:str):
    
    
    
    resume_filenames = [cvs_path + path for path in os.listdir(cvs_path) if os.path.splitext(path)[1] in allowed_extensions]
    
    job_description = read_text_file(job_description_path)
    

    if algorithm == "tfidf":
        cvs_ranked = rank_by_tfidf(job_description, resume_filenames)

    elif algorithm == 'word2vec':
        cvs_ranked = rank_by_word2vec(job_description, resume_filenames)

    elif algorithm == 'bm25':
        cvs_ranked = rank_by_bm25(job_description, resume_filenames)
    
    return {"data":dict(cvs_ranked)}

