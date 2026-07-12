import sys
import os
import pandas as pd

# Allow imports from the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from apps.retriever import (
    load_faiss_index,
    load_metadata,
    embed_query,
    search_documents,
    retrieve_context,
)

from apps.gene import gene_ans


def run_evaluation():

    # Load benchmark questions
    df = pd.read_csv("evaluation/questions.csv")

    index = load_faiss_index()
    metadata = load_metadata()

    results = []

    total = len(df)

    for i, row in df.iloc[3:10].iterrows():

        question = row["question"]
        ground_truth = row["ground_truth"]

        print(f"[{i+1}/{total}] {question}")

        # Embed query
        query_vector = embed_query(question)

        # Retrieve
        distances, indices = search_documents(
            index,
            query_vector,
            top_k=5
        )

        docs = retrieve_context(indices, metadata)

        # Build context list
        contexts = []

        for doc in docs:
            contexts.append(doc["title"] + "\n\n" + doc["content"])

        # Generate answer
        answer = gene_ans(question, docs)

        results.append({
            "question": question,
            "ground_truth": ground_truth,
            "answer": answer,
            "contexts": contexts
        })

    results_df = pd.DataFrame(results)

    results_df.to_csv(
        "evaluation/results.csv",
        index=False
    )

    print("\nEvaluation dataset created successfully!")
    print("Saved to evaluation/results.csv")


if __name__ == "__main__":
    run_evaluation()