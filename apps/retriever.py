import faiss
import joblib
from apps.embedding import load_embedding_model
import numpy as np 




def load_faiss_index():

    return faiss.read_index(
        "data/faiss/faiss.index"
    )

def load_metadata():

    return joblib.load(
        "data/faiss/metadata.pkl"
    )


def embed_query(question):

    model = load_embedding_model()

    vector = model.embed_query(question)

    return vector


def search_documents(index, query_vector, top_k=5,threshold = 1.0):

    query_vector = np.array(
        [query_vector]
    ).astype("float32")

    distances, indices = index.search(
        query_vector,
        top_k
    )

    filtered_indices = []
    filtered_distances = []

    for distance, idx in zip(distances[0], indices[0]):

        if distance <= threshold:
            filtered_indices.append(idx)
            filtered_distances.append(distance)

    return filtered_distances, filtered_indices


def retrieve_context(indices, metadata):

    documents = []

    for idx in indices:

        documents.append(metadata[idx])

    return documents