from click import clear
from fastapi import FastAPI
import random

app = FastAPI()

quotes = [
    "working hard is essiential to success.",
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Act as if what you do makes a difference. It does.",
    "Do what you can, with what you have, where you are.",
    "The best way to predict the future is to create it.",
    "Happiness depends upon ourselves.",
    "Opportunities don't happen. You create them.",
    "Don’t let yesterday take up too much of today."
]

@app.get("/quote")
def get_random_quote():
    return {"quote": random.choice(quotes)}
