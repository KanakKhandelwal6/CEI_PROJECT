import ast
import pandas as pd
from datasets import Dataset
from ragas import evaluate

# Metrics
from ragas.metrics import (
    Faithfulness,
    AnswerRelevancy,
    ContextPrecision,
    ContextRecall,
)

# Load results.csv

df = pd.read_csv("evaluation/res.csv")

# Convert string representation of list back to list
df["contexts"] = df["contexts"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else x
)

# Create HuggingFace Dataset


dataset = Dataset.from_dict(
    {
        "question": df["question"].tolist(),
        "answer": df["answer"].tolist(),
        "contexts": df["contexts"].tolist(),
        "ground_truth": df["ground_truth"].tolist(),
    }
)

# Run Evaluation


result = evaluate(
    dataset=dataset,
    metrics=[
        Faithfulness(),
        AnswerRelevancy(),
        ContextPrecision(),
        ContextRecall(),
    ],
)


# Print Scores

print("\n= RAGAS RESULTS =\n")

print(result)


# Save Scores

scores = result.to_pandas()

scores.to_csv(
    "evaluation/ragas_scores.csv",
    index=False
)

print("\nScores saved to evaluation/ragas_scores.csv")