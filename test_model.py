from apps.gene import gene_ans

docs = [
    {
        "title": "Test",
        "content": "This is a test document."
    }
]

print(gene_ans("What is this?", docs))