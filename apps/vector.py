import joblib
import numpy as np
import faiss
import os
def load_embeddings():
    embeddings = joblib.load("data/embeddings/embeddings.pkl")

    return embeddings


def extract_vectors(embeddings):

    vectors = []

    metadata = []

    for item in embeddings:

        vectors.append(item["embedding"])

        metadata.append(item["metadata"])

    vectors = np.array(vectors).astype("float32")

    return vectors, metadata


def create_faiss_index(vector_dimension):
    index = faiss.IndexFlatL2(vector_dimension)
    return index

def add_vector(index,vectors):
    index.add(vectors)
    return index


def save_index(index):

    os.makedirs(
        "data/faiss",
        exist_ok=True
    )

    faiss.write_index(
        index,
        "data/faiss/faiss.index"
    )

def load_index():
    index = faiss.read_index("data/faiss/faiss.index")
    return index


def save_metadata(metadata):

    os.makedirs("data/faiss", exist_ok=True)

    joblib.dump(
        metadata,
        "data/faiss/metadata.pkl"
    )