import json 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from confi import GOOGLE_API_KEY
from langchain_huggingface import HuggingFaceEmbeddings
import joblib
import os
import time
def load_docu(filepath):
    with open(filepath,"r",encoding="utf-8") as file:
        documents = json.load(file)

    return documents


def load_embedding_model():
    embedding_model = GoogleGenerativeAIEmbeddings(
        model  = "models/gemini-embedding-2",
        google_api_key = GOOGLE_API_KEY
    )

    return embedding_model


def create_embedding(model,documents):
    text = documents["title"]+"\n\n"+documents["content"]
    embedding = model.embed_query(text)
    return embedding

def generate_embeddings(documents, batch_size=50):

    model = load_embedding_model()

    embeddings = []

    for i in range(0, len(documents), batch_size):

        batch = documents[i:i + batch_size]

        texts = [
            doc["title"] + "\n\n" + doc["content"]
            for doc in batch
        ]

        vectors = model.embed_documents(texts)

        for doc, vector in zip(batch, vectors):

            embeddings.append({

                "id": doc["id"],

                "embedding": vector,

                "metadata": doc

            })

        print(
            f"Processed {min(i + batch_size, len(documents))}/{len(documents)}"
        )

    return embeddings


def save_embeddings(embeddings):
    os.makedirs("data/embeddings", exist_ok=True)

    joblib.dump(
        embeddings,
        "data/embeddings/embeddings.pkl"
    )

    print("Embeddings Saved Successfully")
    