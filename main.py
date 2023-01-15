# Fast Api server implemetation, which receives files and transcribes them

from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from utils import transcribe


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/files/")
async def create_file(file: bytes = File()):
    transcribed = transcribe(file)
    # TODO: Checks that file is a sound file

    return transcribed #{"file_size": len(file)}
